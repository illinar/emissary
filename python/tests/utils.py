import logging
import os
import subprocess
import requests
import socket
import tempfile
import time
from collections import namedtuple
from retry import retry

import json
import yaml

from ambassador import Cache, IR
from ambassador.compile import Compile
from ambassador.utils import NullSecretHandler
from kat.utils import namespace_manifest
from kat.harness import load_manifest, CLEARTEXT_HOST_YAML

logger = logging.getLogger("ambassador")

httpbin_manifests ="""
---
apiVersion: v1
kind: Service
metadata:
  name: httpbin
spec:
  type: ClusterIP
  selector:
    service: httpbin
  ports:
  - port: 80
    targetPort: http
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: httpbin
spec:
  replicas: 1
  selector:
    matchLabels:
      service: httpbin
  template:
    metadata:
      labels:
        service: httpbin
    spec:
      containers:
      - name: httpbin
        image: kennethreitz/httpbin
        ports:
        - name: http
          containerPort: 80
"""

qotm_manifests = """
---
apiVersion: v1
kind: Service
metadata:
  name: qotm
spec:
  selector:
    service: qotm
  ports:
    - port: 80
      targetPort: http-api
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: qotm
spec:
  selector:
    matchLabels:
      service: qotm
  replicas: 1
  strategy:
    type: RollingUpdate
  template:
    metadata:
      annotations:
        sidecar.istio.io/inject: "false"
      labels:
        service: qotm
    spec:
      serviceAccountName: ambassador
      containers:
      - name: qotm
        image: docker.io/datawire/qotm:1.3
        ports:
        - name: http-api
          containerPort: 5000
"""


def run_and_assert(command, communicate=True):
    print(f"Running command {command}")
    output = subprocess.Popen(command, stdout=subprocess.PIPE)
    if communicate:
        stdout, stderr = output.communicate()
        print('STDOUT', stdout.decode("utf-8") if stdout is not None else None)
        print('STDERR', stderr.decode("utf-8") if stderr is not None else None)
        assert output.returncode == 0
        return stdout.decode("utf-8") if stdout is not None else None
    return None


def meta_action_kube_artifacts(namespace, artifacts, action):
    temp_file = tempfile.NamedTemporaryFile()
    temp_file.write(artifacts.encode())
    temp_file.flush()

    command = ['kubectl', action, '-f', temp_file.name]
    if namespace is None:
        namespace = 'default'

    if namespace is not None:
        command.extend(['-n', namespace])

    run_and_assert(command)
    temp_file.close()


def apply_kube_artifacts(namespace, artifacts):
    meta_action_kube_artifacts(namespace=namespace, artifacts=artifacts, action='apply')


def delete_kube_artifacts(namespace, artifacts):
    meta_action_kube_artifacts(namespace=namespace, artifacts=artifacts, action='delete')


def install_ambassador(namespace, envs=None):
    """
    :param namespace: namespace to install Ambassador in
    :param envs: [
      {
        'name': 'ENV_NAME',
        'value': 'ENV_VALUE'
      },
      ...
      ...
    ]
    """

    if envs is None:
        envs = []

    # Create namespace to install Ambassador
    create_namespace(namespace)

    # Create Ambassador CRDs
    apply_kube_artifacts(namespace=namespace, artifacts=load_manifest('crds'))

    # Proceed to install Ambassador now
    final_yaml = []

    serviceAccountExtra = ''
    if os.environ.get("DEV_USE_IMAGEPULLSECRET", False):
        serviceAccountExtra = """
imagePullSecrets:
- name: dev-image-pull-secret
"""

    ambassador_yaml = list(yaml.safe_load_all((
        load_manifest('rbac_cluster_scope')+
        load_manifest('ambassador')+
        (CLEARTEXT_HOST_YAML % namespace)
    ).format(
        capabilities_block="",
        envs="",
        extra_ports="",
        serviceAccountExtra=serviceAccountExtra,
        image=os.environ["AMBASSADOR_DOCKER_IMAGE"],
        self=namedtuple('self', 'namespace path ambassador_id')(
            namespace,
            namedtuple('path', 'k8s')(
                'ambassador'),
            'default',
        ),
    )))

    for manifest in ambassador_yaml:
        if manifest.get('kind', '') == 'Pod' and manifest.get('metadata', {}).get('name', '') == 'ambassador':

            # Don't set AMBASSADOR_ID={self.k8s.path}
            for envvar in manifest['spec']['containers'][0]['env']:
                if envvar.get('name', '') == 'AMBASSADOR_ID':
                    envvar['value'] = 'default'

            # add new envs, if any
            manifest['spec']['containers'][0]['env'].extend(envs)

    apply_kube_artifacts(namespace=namespace, artifacts=yaml.safe_dump_all(ambassador_yaml))


def create_namespace(namespace):
    apply_kube_artifacts(namespace=namespace, artifacts=namespace_manifest(namespace))


def create_qotm_mapping(namespace):
    qotm_mapping = f"""
---
apiVersion: getambassador.io/v2
kind: Mapping
metadata:
  name:  qotm-mapping
  namespace: {namespace}
spec:
  prefix: /qotm/
  service: qotm
"""

    apply_kube_artifacts(namespace=namespace, artifacts=qotm_mapping)

def create_httpbin_mapping(namespace):
    httpbin_mapping = f"""
---
apiVersion: getambassador.io/v2
kind: Mapping
metadata:
  name:  httpbin-mapping
  namespace: {namespace}
spec:
  prefix: /httpbin/
  rewrite: /
  service: httpbin
"""

    apply_kube_artifacts(namespace=namespace, artifacts=httpbin_mapping)


def get_code_with_retry(req, headers={}):
    for attempts in range(10):
        try:
            resp = requests.get(req, headers=headers, timeout=10)
            if resp.status_code < 500:
                return resp.status_code
            print(f"get_code_with_retry: 5xx code {resp.status_code}, retrying...")
        except requests.exceptions.ConnectionError as e:
            print(f"get_code_with_retry: ConnectionError {e}, attempt {attempts+1}")
        except socket.timeout as e:
            print(f"get_code_with_retry: socket.timeout {e}, attempt {attempts+1}")
        except Exception as e:
            print(f"get_code_with_retry: generic exception {e}, attempt {attempts+1}")
        time.sleep(5)
    return 503

def zipkin_tracing_service_manifest():
    return """
---
apiVersion: getambassador.io/v2
kind: TracingService
metadata:
  name: tracing
  namespace: ambassador
spec:
  service: zipkin:9411
  driver: zipkin
  config: {}
"""

def module_and_mapping_manifests(module_confs, mapping_confs):
    yaml = """
---
apiVersion: getambassador.io/v2
kind: Module
metadata:
  name: ambassador
  namespace: default
spec:
  config:"""
    if module_confs:
        for module_conf in module_confs:
            yaml = yaml + """
    {}
""".format(module_conf)
    else:
        yaml = yaml + " {}\n"

    yaml = yaml + """
---
apiVersion: getambassador.io/v2
kind: Mapping
metadata:
  name: ambassador
  namespace: default
spec:
  prefix: /httpbin/
  service: httpbin"""
    if mapping_confs:
        for mapping_conf in mapping_confs:
            yaml = yaml + """
  {}""".format(mapping_conf)
    return yaml

def _require_no_errors(ir: IR):
    assert ir.aconf.errors == {}

def _secret_handler():
    source_root = tempfile.TemporaryDirectory(prefix="null-secret-", suffix="-source")
    cache_dir = tempfile.TemporaryDirectory(prefix="null-secret-", suffix="-cache")
    return NullSecretHandler(logger, source_root.name, cache_dir.name, "fake")

def econf_compile(yaml):
    # Compile with and without a cache. Neither should produce errors.
    cache = Cache(logger)
    secret_handler = _secret_handler()
    r1 = Compile(logger, yaml, k8s=True, secret_handler=secret_handler)
    r2 = Compile(logger, yaml, k8s=True, secret_handler=secret_handler, cache=cache)
    _require_no_errors(r1["ir"])
    _require_no_errors(r2["ir"])

    # Both should produce equal Envoy config as sorted json.
    r1j = json.dumps(r1['v2'].as_dict(), sort_keys=True, indent=2)
    r2j = json.dumps(r2['v2'].as_dict(), sort_keys=True, indent=2)
    assert r1j == r2j

    # Now we can return the Envoy config as a dictionary
    return r1['v2'].as_dict()

def econf_foreach_hcm(econf, fn):
    found_hcm = False
    for listener in econf['static_resources']['listeners']:
        # There's only one filter chain...
        filter_chains = listener['filter_chains']
        assert len(filter_chains) == 1

        # ...and one filter on that chain.
        filters = filter_chains[0]['filters']
        assert len(filters) == 1

        # The http connection manager is the only filter on the chain from the one and only vhost.
        hcm = filters[0]
        assert hcm['name'] == 'envoy.filters.network.http_connection_manager'
        typed_config = hcm['typed_config']
        assert typed_config['@type'] == 'type.googleapis.com/envoy.config.filter.network.http_connection_manager.v2.HttpConnectionManager'

        r = fn(typed_config)
        if not r:
            break

def econf_foreach_cluster(econf, fn, name='cluster_httpbin_default'):
    for cluster in econf['static_resources']['clusters']:
        if cluster['name'] != name:
            continue

        r = fn(cluster)
        if not r:
            break