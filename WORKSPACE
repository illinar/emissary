load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

http_archive(
    name = "io_bazel_rules_go",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/rules_go/releases/download/v0.21.2/rules_go-v0.21.2.tar.gz",
        "https://github.com/bazelbuild/rules_go/releases/download/v0.21.2/rules_go-v0.21.2.tar.gz",
    ],
    sha256 = "f99a9d76e972e0c8f935b2fe6d0d9d778f67c760c6d2400e23fc2e469016e2bd",
)
load("@io_bazel_rules_go//go:deps.bzl", "go_rules_dependencies", "go_register_toolchains")
go_rules_dependencies()
go_register_toolchains()

http_archive(
    name = "bazel_gazelle",
    urls = [
        "https://storage.googleapis.com/bazel-mirror/github.com/bazelbuild/bazel-gazelle/releases/download/v0.20.0/bazel-gazelle-v0.20.0.tar.gz",
        "https://github.com/bazelbuild/bazel-gazelle/releases/download/v0.20.0/bazel-gazelle-v0.20.0.tar.gz",
    ],
    sha256 = "d8c45ee70ec39a57e7a05e5027c32b1576cc7f16d9dd37135b0eddde45cf1b10",
)
load("@bazel_gazelle//:deps.bzl", "gazelle_dependencies")
gazelle_dependencies()

git_repository(
    name = "rules_python",
    remote = "https://github.com/bazelbuild/rules_python.git",
    commit = "38f86fb55b698c51e8510c807489c9f4e047480e",
)
load("@rules_python//python:repositories.bzl", "py_repositories")
py_repositories()
load("@rules_python//python:pip.bzl", "pip_repositories", "pip3_import")
pip_repositories()
pip3_import(
    name = "ambassador_cheeseshop",
    requirements = "//builder:requirements.txt",
)
load("@ambassador_cheeseshop//:requirements.bzl", "pip_install")
pip_install()
