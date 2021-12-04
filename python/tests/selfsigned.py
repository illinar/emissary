# Code generated by selfsigned.py.gen. DO NOT EDIT.

from base64 import b64encode
from typing import Dict, List, NamedTuple, Optional

class Cert(NamedTuple):
    names: List[str]
    pubcert: str
    privkey: str

    @property
    def k8s_crt(self) -> str:
        return b64encode((self.pubcert+"\n").encode('utf-8')).decode('utf-8')

    @property
    def k8s_key(self) -> str:
        return b64encode((self.privkey+"\n").encode('utf-8')).decode('utf-8')

def strip(s: str) -> str:
    return "\n".join(l.strip() for l in s.split("\n") if l.strip())

_TLSCerts: List[Cert] = [
    Cert(
        names=["master.datawire.io"],
        # Note: This cert is also used to sign several other certs in
        # this file (as the issuer).
        pubcert=strip("""
            -----BEGIN CERTIFICATE-----
            MIID8zCCAtugAwIBAgIRAIBtMsh/xwUcw6m3hSPuJP4wDQYJKoZIhvcNAQELBQAw
            eDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAk1BMQ8wDQYDVQQHEwZCb3N0b24xGDAW
            BgNVBAoTD0FtYmFzc2Fkb3IgTGFiczEUMBIGA1UECxMLRW5naW5lZXJpbmcxGzAZ
            BgNVBAMTEm1hc3Rlci5kYXRhd2lyZS5pbzAgFw0yMTExMTAxMzEyMDBaGA8yMDk5
            MTExMDEzMTIwMFoweDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAk1BMQ8wDQYDVQQH
            EwZCb3N0b24xGDAWBgNVBAoTD0FtYmFzc2Fkb3IgTGFiczEUMBIGA1UECxMLRW5n
            aW5lZXJpbmcxGzAZBgNVBAMTEm1hc3Rlci5kYXRhd2lyZS5pbzCCASIwDQYJKoZI
            hvcNAQEBBQADggEPADCCAQoCggEBAL+CoQfKiZmfRd3SkuPUW5nh/CU26owzuUjC
            75PxuOuOzb/UD+gml2nlSGnRi09PfNsqbLBXdON9YDOkb9sxB85l2wW1+so295Kr
            qd8Vn5U6oa5MDXLZ+pEd9jaH/JYjAjgB2XpPyoQXj4079WnU24qy3ZOfk6W3wWxc
            +ljKHLySqvRxwRlCwiZuagQcMfD8nn0vHOMEyj2QymOJ6bx5s0OZcJ72YAVQbYil
            4kJQ/obKkrEzMQPORu+q+3dEhuaauJnzOrECpHX/56spSaRYCIkFgoUGfdl+S7Qr
            lQ4AHCrbjDdZQAyw+3kEiIGDrJuYdWk6XwEAPevC50CXmZ0+3q0CAwEAAaN2MHQw
            DgYDVR0PAQH/BAQDAgKkMBMGA1UdJQQMMAoGCCsGAQUFBwMBMA8GA1UdEwEB/wQF
            MAMBAf8wHQYDVR0OBBYEFN0KfRluDdz4MNcFXcyH/6SRRiwXMB0GA1UdEQQWMBSC
            Em1hc3Rlci5kYXRhd2lyZS5pbzANBgkqhkiG9w0BAQsFAAOCAQEAvtan3vxT2lHk
            L0qoqHra54OhhDdBEEdQ1NngiyFY1He4HbHmAQi7MtMCDd8GwqKJsIhK9dZ9Q3Ux
            Z0BvYjB7q9U2i5Fc+KmkbJMsL6gp+Pm9txNq9gDMHz9SaVMqFuI7UyJ0V+M2V7E1
            6PWIyxW6MSq5fM6NEEkNgxgGO0479uw588FTc5p6mIfRjcpRMJEXBed3lymQ27+m
            MNOM/NS6vGdL9ajCqaw/QUV/kdTSfmiMowIo6ClabzIO47qi66sm/gZkUJ2BcLbj
            G3IqbkXudkWkvZ5XgZ6JnyjXg1ifR/1uaUYPcchO0JiWUu9KHwZiKCoQM+qECCgX
            /4YZh3ot2w==
            -----END CERTIFICATE-----
            """),
        privkey=strip("""
            -----BEGIN PRIVATE KEY-----
            MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC/gqEHyomZn0Xd
            0pLj1FuZ4fwlNuqMM7lIwu+T8bjrjs2/1A/oJpdp5Uhp0YtPT3zbKmywV3TjfWAz
            pG/bMQfOZdsFtfrKNveSq6nfFZ+VOqGuTA1y2fqRHfY2h/yWIwI4Adl6T8qEF4+N
            O/Vp1NuKst2Tn5Olt8FsXPpYyhy8kqr0ccEZQsImbmoEHDHw/J59LxzjBMo9kMpj
            iem8ebNDmXCe9mAFUG2IpeJCUP6GypKxMzEDzkbvqvt3RIbmmriZ8zqxAqR1/+er
            KUmkWAiJBYKFBn3Zfku0K5UOABwq24w3WUAMsPt5BIiBg6ybmHVpOl8BAD3rwudA
            l5mdPt6tAgMBAAECggEANAR+Ssh3sZNyfbr5jQqcSuL4Av+0m5pdBGd2fZ/Vk535
            QtaN74ez7t6JWbzB8yvrBPi0Bv3qUPQ4Ei7i9w2NSkGeSSHR2eUuP9eCz4ZnDzia
            u+YKbRzKE2qo+szbDci6jI3sDW3o2xIvOrSDh1h6vWSyDKv2hbewwQdMNJvJTGqt
            OKKDJ8DJbutrWs80uf26cRU9iqLwAUs7T9WtMoBEgoG1mu5P7fyW5Y+UAy+JXJso
            3yoypl8/VG9LDT28w41OaNUdQMyxH4zKDGtMbI8f8OJksvZZcuGHaDkE6h2i8mj8
            frMXLEH6TYHYEcljNJaRErDi1ZiMgfQciTZU5fd+PQKBgQD1klkI39REysdNbdD4
            Rdckh0fNVMr+cwRxrMuk/g85/mTXEsYTMrz5duFNnNLpAuNGLsSNHKpoMj6waQZO
            zSbX3O0oBTzYAtg8tIbv6cAsFC3VTADm5wKkbDh5xO7XLD3M8FDkOWzPVcLefA1s
            K2A2+KOmS+ssfQHrgR6bpC+IUwKBgQDHpJIDiPI4C3cabTaJkVcHIRhMb8YatkRu
            h3jr/qocRTAcerd4m+t/MsQVXJnCj/Y77Fz7l2IlIEyeZsbejs1myJ8wQR9SozCA
            8EIgyARyTvx/oRG4slQokl3FI9dIlteiB9VK9yjeaidd8zShXjtpoyOqC8RJjidM
            dwz80W8c/wKBgH2d4xV7CaY25ERjTGXzs93npX8PRNdsFnXfojxACaHs08CAxfnE
            Fo61lQKSmgC/jWq1Oa3FYBX0vcSXtLZSkvAQ/u9d3oXQzrQe1Hec5sSlfdyCCGQU
            /3EEOs9vQY2n/+T5eSeFiHd2szwD0QnoFkuIXI4Qf7g+KeFCJ1oOXpIpAoGAR0bE
            Mqrj/4poXXD8daUEMzFnoXKOgd7tE6EeVPM4/JrfEGvnsRHJxEH1q8LByqrnOIGs
            uM5VZffgIvWCrtbBEp8x5mJ5smE84evlUBrZK45zq4Vv9EcGsO2AuO+Q3wOrvNeb
            GQag+rdfkrVP5wTjpVVvWDiXPcOY2D3wzxpe1zUCgYApD9hCJOLo7TwOFRT0B5CV
            LnaW4aeMx9RbcehZzsih7sFmfaZI6V4l86CEdp7kLnZSPYr5d7rPlr/adGcMj9bF
            SVx+QqH6cMtBK6tSdjJT2KuOfqkzA7tK6SzmApaZTZiz8XM3MooYDj86EJ93l8EH
            xvKPa17iyHPUWNTHy9NuTA==
            -----END PRIVATE KEY-----
            """)
    ),

    Cert(
        names=["presto.example.com"],
        # Note:
        #  1. This cert is signed by the "master.datawire.io" cert
        #     (rather than being self-signed).
        #  2. This cert is a client cert (rather than being a server
        #     cert).
        pubcert=strip("""
            -----BEGIN CERTIFICATE-----
            MIID8TCCAtmgAwIBAgIQHjsjEOZ4SEEVcrnClDnBPjANBgkqhkiG9w0BAQsFADB4
            MQswCQYDVQQGEwJVUzELMAkGA1UECBMCTUExDzANBgNVBAcTBkJvc3RvbjEYMBYG
            A1UEChMPQW1iYXNzYWRvciBMYWJzMRQwEgYDVQQLEwtFbmdpbmVlcmluZzEbMBkG
            A1UEAxMSbWFzdGVyLmRhdGF3aXJlLmlvMCAXDTIxMTExMDEzMTIwMFoYDzIwOTkx
            MTEwMTMxMjAwWjB4MQswCQYDVQQGEwJVUzELMAkGA1UECBMCTUExDzANBgNVBAcT
            BkJvc3RvbjEYMBYGA1UEChMPQW1iYXNzYWRvciBMYWJzMRQwEgYDVQQLEwtFbmdp
            bmVlcmluZzEbMBkGA1UEAxMScHJlc3RvLmV4YW1wbGUuY29tMIIBIjANBgkqhkiG
            9w0BAQEFAAOCAQ8AMIIBCgKCAQEA4yhKmfYaRGrKMKLwoIi+fWxccRXjBVDjL759
            j4xY2WmdZsA0OGkuhPnU92Z7vMrEW2Ior1DeJkJURtmW7thZYhiBJZom2WLJ8nhW
            dOU3shoQWmPmapmSkRgXkx8BCXDPPbrrCjS3eQZmLD2SILxaA98DmIb07N1tliGM
            +cwyQo0e9ptBlaMrAOxKJcVx58LXP1Rr4+lctLe198kJ1Fw9vwBpQW8UdrSuMQdh
            6lc+OUoEq7F2jJYuWzaaanAMDRiRt+p0jKeyAUp+ZfMhvqBxg76I/rehGANkaAHq
            tEJJrjyOjUmi/tafCjUCHGk5Xjp74EKakdn1nzqI1Uv7Xc421QIDAQABo3UwczAO
            BgNVHQ8BAf8EBAMCBaAwEwYDVR0lBAwwCgYIKwYBBQUHAwIwDAYDVR0TAQH/BAIw
            ADAfBgNVHSMEGDAWgBTdCn0Zbg3c+DDXBV3Mh/+kkUYsFzAdBgNVHREEFjAUghJw
            cmVzdG8uZXhhbXBsZS5jb20wDQYJKoZIhvcNAQELBQADggEBAE1OJ+e2seALd1uO
            qB3cQ2Fd2R+sm6pSkitngoaWlmAOsiunT3Qa1H+UWsZdBOv7RQ9JbgmRzsgAMKnR
            PwnGzDcJ9miBs/qY1LpGEeIziL5/BZ1QimhTvsLzbmdMBdFpZtYNTfGMxuoI2p3R
            r8pMcAb9P1EFZ8xVtf0KH6Wttq5Z8OHtvkE8W8u+I/FEjdwuu2Uurjx6AamS5Tw/
            HmM305OUzE7q0PrFsCBpkkIoc0KOIY0Nrx9B9y0mTRaWpvf0gri1NQuc+a4koFCD
            zdOaXfE5YKLIQyYBhVnblHbHpPO7PXyC5UqEpHvTaECFi/6eR1BZVCrrgMxCc9s5
            J03slWw=
            -----END CERTIFICATE-----
            """),
        privkey=strip("""
            -----BEGIN PRIVATE KEY-----
            MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDjKEqZ9hpEasow
            ovCgiL59bFxxFeMFUOMvvn2PjFjZaZ1mwDQ4aS6E+dT3Znu8ysRbYiivUN4mQlRG
            2Zbu2FliGIElmibZYsnyeFZ05TeyGhBaY+ZqmZKRGBeTHwEJcM89uusKNLd5BmYs
            PZIgvFoD3wOYhvTs3W2WIYz5zDJCjR72m0GVoysA7EolxXHnwtc/VGvj6Vy0t7X3
            yQnUXD2/AGlBbxR2tK4xB2HqVz45SgSrsXaMli5bNppqcAwNGJG36nSMp7IBSn5l
            8yG+oHGDvoj+t6EYA2RoAeq0QkmuPI6NSaL+1p8KNQIcaTleOnvgQpqR2fWfOojV
            S/tdzjbVAgMBAAECggEANj6O4gk06JWfxtGCKLO+2XCg+phBaCmStvoEPd1D8lcY
            MUtArR/g7fxC8PlWHxVEopXkJUloYzZ/rZOUSWD8p0I2xOX01QCUPQSjkLKUBEHZ
            Gdy1T0txBpj8ODO1Ka34r0MNkZhZH9t5VqM1W//edwIwd6HypwWRf8JvSc+LSPy6
            4AofNr83rebDD62ZfW6qG+MR4Gh3DKST45sYoTtII7e/TWZPhcgO8zkaq+EIm6bc
            YYlJM1yxbnEEV9mCDlsRWf+RU0ZwGC8noGm9iP9lkrLlF2++CLEllpMexD1bP/67
            MzTWAz/GKo2ByMImbnFgYycf+gBHIpV5AzZ1fTd/gQKBgQDoAhuK2DjWWiUsnKGq
            mGp88y9pQscmA+14XKBQpNDG7/7zRQ2heYDQT83M0ZKFex/GRz1pN/bNUCFZEvqQ
            5gXJa+Omq5miRHlFKkhQdezwW04FcgUI8uGCT2dmlaK48NKVXRmLpPHpIvOOW4Cl
            s3CY0iRwJyKWMdsGcwezgbY3pQKBgQD6pcTJ7gYVOvCVRI6TeLH36ZXy1hg+hjNI
            K5UjoxkRV00M0akMdOqBmcXmzet7UwepqRih6hol3/Tama2GRzbnwIMRwBTYC5ve
            D8XwjE8oAZkuz4Wm08gsGn1P0VjPTYbXffwvKrAtxKXZ2tIEKqUAuDbpuDcsmxEh
            E4deeLhbcQKBgQCeXBnqmo2pGdy3562doO1GnkMlSPRf6VxkxGyUvvrWXygZam/U
            YPfguCgT/pRRUeotT6EGObHXEDPC9eZbkvYuNtsrf4OdM7nG0QaNDQEOSnQl2V7A
            bfApHwPIDKkGLTK/ys1N+Oc6J6Yw7BoSgDmBxiYi+0NrW1pRu6BtEUOMFQKBgFgr
            pBQcpQsm1qbLnRQHayN4igUIhzLHZpbGrgoBP7o36aTOxBbbsfqxK0rLuUCCrrli
            AIZEobodFDcpxD7uIkRYFkNSPILbYpM1HT5HPTknhslOuwc6jLnm/5nqXMFf1kVL
            zkCRVbRj7qu6LBLHJZAhPT/uS4pnahkmk4IKGWAhAoGASPPltWWBKaBUkgahC3t/
            PyXpeANVcHCrEnWCru5sWDc2zo9YvzVmYz8E3/cnHE4C9EMBxGDvQVsjEOLIIIuM
            fNnQ+OIW34GWz7pojjvVgirlFVmrT9gV6OXJBmh9aGvQN0En8qxZVQouo/UUkwoO
            4gpH/If2ar0U3JDIU+d87o0=
            -----END PRIVATE KEY-----
            """)
    ),

    Cert(
        names=["ratelimit.datawire.io"],
        pubcert=strip("""
            -----BEGIN CERTIFICATE-----
            MIID2jCCAsKgAwIBAgIRAKlRg3DeRR97bt/PNtG2qw0wDQYJKoZIhvcNAQELBQAw
            ezELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAk1BMQ8wDQYDVQQHEwZCb3N0b24xGDAW
            BgNVBAoTD0FtYmFzc2Fkb3IgTGFiczEUMBIGA1UECxMLRW5naW5lZXJpbmcxHjAc
            BgNVBAMTFXJhdGVsaW1pdC5kYXRhd2lyZS5pbzAgFw0yMTExMTAxMzEyMDBaGA8y
            MDk5MTExMDEzMTIwMFowezELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAk1BMQ8wDQYD
            VQQHEwZCb3N0b24xGDAWBgNVBAoTD0FtYmFzc2Fkb3IgTGFiczEUMBIGA1UECxML
            RW5naW5lZXJpbmcxHjAcBgNVBAMTFXJhdGVsaW1pdC5kYXRhd2lyZS5pbzCCASIw
            DQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALypYKoQpEKbSyG3rVM2ddDt3XqD
            ra6nfBmZ8YqW03dLE0XY8hED2KPruX281SKSU5vgGmA0IRUfelxFxS2Rznrk3CGb
            lsBBka8GEXQF6TRtcHb1CQHZqeylPBAeuXaMXrwR8fcKXspu+9BHzjkd7w9Fbp7F
            6cubtPMGSPzpxhF7FJ+SEuWEzKSonWKa93rk4+ytIcuVZeWmdirZbpuP6Bel05Cu
            i9Vs6Qia68AQ5tQvsKQoWUkFSJANeY7WMzqEgt+BG0hKt658otVOAJdyFPEA96j7
            6CFjS9VXxcD18BruPWdil/6gprQhc/XVRU4cUrOOqPmoKhtmDekLY6Cka9MCAwEA
            AaNXMFUwDgYDVR0PAQH/BAQDAgWgMBMGA1UdJQQMMAoGCCsGAQUFBwMBMAwGA1Ud
            EwEB/wQCMAAwIAYDVR0RBBkwF4IVcmF0ZWxpbWl0LmRhdGF3aXJlLmlvMA0GCSqG
            SIb3DQEBCwUAA4IBAQCIZJnPY9NkOY0w8GaVDHrkHIREU8r/B2cv3dNn0k9ktvlC
            0rgUvg7ZDzsr7h+uWI5VgxED1KpnQbDcHMQL2Wk0+z5xJgP+wj1ueSCniJGeOUEH
            zWZQ4rfs8jUFkBT+Is12YX+YEOGYP71+EzmbGK3glRfbI+NrtJuv+vpiZKcQzHfq
            V3IpUKpEJ0o4XVUuBKtnVXcWrR+KlJQCY2vC5eSMstjgC5YKVBRiVqbyIGA/ThDq
            BpKO3eeUmF2SWhIzCCgLq49iTaBpSzw7mFZdQsOTyXQVVppOmcjqTiF3j8FaVTE5
            WWblE/fD+ZXIPEMxs9te3T9/DIKDM8AyxoJ1Jh7K
            -----END CERTIFICATE-----
            """),
        privkey=strip("""
            -----BEGIN PRIVATE KEY-----
            MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC8qWCqEKRCm0sh
            t61TNnXQ7d16g62up3wZmfGKltN3SxNF2PIRA9ij67l9vNUiklOb4BpgNCEVH3pc
            RcUtkc565Nwhm5bAQZGvBhF0Bek0bXB29QkB2anspTwQHrl2jF68EfH3Cl7KbvvQ
            R845He8PRW6exenLm7TzBkj86cYRexSfkhLlhMykqJ1imvd65OPsrSHLlWXlpnYq
            2W6bj+gXpdOQrovVbOkImuvAEObUL7CkKFlJBUiQDXmO1jM6hILfgRtISreufKLV
            TgCXchTxAPeo++ghY0vVV8XA9fAa7j1nYpf+oKa0IXP11UVOHFKzjqj5qCobZg3p
            C2OgpGvTAgMBAAECggEBAJ+xd6M8pu3CaZxGz63qIVwSnDDCGVgHaSJ6jlxTQvht
            UgkDlBMXAF/wfniSSI8U8TS2Q10/gulQVdCZNkhWbULVSgggnUBrwBc4ublN75Jz
            OIlY7KDmT9GCJA85Ep/oPaBQSFJmMsqDmx84SLVMQzjX+sTmnfm8+TPlFA8RCplr
            83S8PqVVGGh0RdMyFh0Tsv5wqWodxv09vmUgeq42S76NsSg8A6HrVP15EAZcEHiM
            zOSUYqh58EEDXHOscMy/8bUGY07EHXZmvsTCMDd3Dsx/7QJ4o1AiS0y5JXaMxDyB
            JSUyQv6zIwzNNyJ7lwqZ9J56B1xcNJoDAw3gCz9/KXECgYEA338WkkQgJrROXepz
            508IP7W1p8jp4/1U+MWRjpriwdhuAXnzB4odPL1SYfFPHfgG8RYBMNQAJDkeIoSt
            xrAJhHkFlJOYzCNos3Aeo8sjqzchWZRnjuJSodRhSShWtJJmuufR55bhYPAr/12h
            nwpwS0HWdGvK3v5wPtCksCmfwUcCgYEA2BleKiIQQSBoW853vemHrIVKTaGULeU7
            degM2lnZBuGKbSxaFxvipj64wORrFm54JxOnCXXWuSJM8tRmoQPA10M3SmUHN/Fu
            v529QMm5sjB17EfQeIymhuFxHm2xvk9mul9WnaozBX29OrVMlwQoqyMzZu1fsXog
            AsIb6wUKZxUCgYBDrtIgE3+FGR+Oc30MNLPzz0ym9kJWqBZ+jB5riF5Zg/i0e8Ds
            rJf0GAWF4bUrBzza7+YGan1setu0amfR/uey9Y+KEjS4xZRkmvS8d71ikXyJC1dd
            Pw71MUMRC6VOY/O2cJPxxZCVccZxPGLArkGZmOOgODCk3XsSms71BnX56wKBgHN+
            S1dVUT6dZWj7lf+H2h0YN7f5zUoiI39Gf+gK8PS+gc8LTzLekmmrR+6/pYQdklXA
            KRvjQNk9PcbiQd94NA5YPCqkiBEcFcaPNWB076wOPlgDoaVr9mxL/Lr4gXBm205s
            OcyV9CLRKts/nilv7ZRZgdVWtDgUPxt6RpV64i5pAoGAGGIwDJAK8ctCtwnbRhJy
            xVHwVcdVjFAEZj0Ytw34FCV6OpJfztvkThA7uqg9yNMwHBdx1vge6Xzxy4rniEtE
            DyFlHyWTrFwoDBYy4d7cNgDJnaIN2qBY36GDyL2x7/DyKd5+CQN07XWuOmnGrzIo
            6ABc+KN1kmXbr9VteFRagAI=
            -----END PRIVATE KEY-----
            """)
    ),

    Cert(
        names=["ambassador.example.com"],
        # Note: This cert is signed by the "master.datawire.io" cert
        # (rather than being self-signed).
        pubcert=strip("""
            -----BEGIN CERTIFICATE-----
            MIID+jCCAuKgAwIBAgIRAMQO4rSR9giQAjULkZVYJd0wDQYJKoZIhvcNAQELBQAw
            eDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAk1BMQ8wDQYDVQQHEwZCb3N0b24xGDAW
            BgNVBAoTD0FtYmFzc2Fkb3IgTGFiczEUMBIGA1UECxMLRW5naW5lZXJpbmcxGzAZ
            BgNVBAMTEm1hc3Rlci5kYXRhd2lyZS5pbzAgFw0yMTExMTAxMzEyMDBaGA8yMDk5
            MTExMDEzMTIwMFowfDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAk1BMQ8wDQYDVQQH
            EwZCb3N0b24xGDAWBgNVBAoTD0FtYmFzc2Fkb3IgTGFiczEUMBIGA1UECxMLRW5n
            aW5lZXJpbmcxHzAdBgNVBAMTFmFtYmFzc2Fkb3IuZXhhbXBsZS5jb20wggEiMA0G
            CSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC7IW+b05L3KzjY3p4OPsynN/8OGztO
            ANqVOXgjQfoe0eQ9KXSMRLccirWOgQHDUlnpuArPpwxmFx8avq2x/G0Ge3mmZx8m
            2uM7XN5wAHhjvnDAnM3Kpfpl3YlpiP7DkaGmbzut4HUew4xf2dDvsul9xKQ8/cAG
            jsypZKoaDLD+uNmRwrMu7GrHCiPtSEfd5Otw5UFcx2bFuFnbbAby1pjsu/FOwqHN
            vV4q3ZVIX9eshLKTj2/ODr61yWiLO8LDCBy3nUPoW5FXGCbhRnP/ev0TUvxhYDus
            TrokBvIXGX5xGbIIHSZ3U8REJP41iC06m7RdbkKEaF61pDyqOSTUtrNhAgMBAAGj
            eTB3MA4GA1UdDwEB/wQEAwIFoDATBgNVHSUEDDAKBggrBgEFBQcDATAMBgNVHRMB
            Af8EAjAAMB8GA1UdIwQYMBaAFN0KfRluDdz4MNcFXcyH/6SRRiwXMCEGA1UdEQQa
            MBiCFmFtYmFzc2Fkb3IuZXhhbXBsZS5jb20wDQYJKoZIhvcNAQELBQADggEBAG2o
            7XEVqjnQdIwoKX/ergbQtPxkyYTLrGDU6qSoLqiwrfEYnUam/oEwTrJtgee56WbT
            eVvemVFEgvSdUoPAW/oa05pZZx33B8kHdQn69DwVyCMdQotx71Izo46Bhk4VuxFo
            J6mBbCUOqdetEDOyehxXUNJRn8VtpDLXanT16tlz3JuJDPBFAk8OvQ6Y65vumedS
            EDpmx8pPi6amfuOPtZZqP60owXA6bv+icEdGrVpK0sErDwN8kj3fvMYzkVROPtZL
            4Z6y4bEGqhBtO+sdz3rTsh7+UOHC/CZgXgdDUK2An2DcjccWqZ0ENAOABEnNgGfA
            SrCA0+AQjzKx/eJwDcg=
            -----END CERTIFICATE-----
            """),
        privkey=strip("""
            -----BEGIN PRIVATE KEY-----
            MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC7IW+b05L3KzjY
            3p4OPsynN/8OGztOANqVOXgjQfoe0eQ9KXSMRLccirWOgQHDUlnpuArPpwxmFx8a
            vq2x/G0Ge3mmZx8m2uM7XN5wAHhjvnDAnM3Kpfpl3YlpiP7DkaGmbzut4HUew4xf
            2dDvsul9xKQ8/cAGjsypZKoaDLD+uNmRwrMu7GrHCiPtSEfd5Otw5UFcx2bFuFnb
            bAby1pjsu/FOwqHNvV4q3ZVIX9eshLKTj2/ODr61yWiLO8LDCBy3nUPoW5FXGCbh
            RnP/ev0TUvxhYDusTrokBvIXGX5xGbIIHSZ3U8REJP41iC06m7RdbkKEaF61pDyq
            OSTUtrNhAgMBAAECggEBAISoCFHEI8w6hLsg3ZUlqbjlNldOsLT0YAAnVGZSMDjG
            /HDrQWbqk5CVOG3EQHaxm3HW+TsJpf19aJxyDfo+Ax/0SmHPesL1qt57UGi/vJig
            +Zdh0XVWQnMSIIaDCm+jfp/Y/MqfcweTAqE0bSxvfZyd2PwvuoArnSR8ayW6V4LK
            WrLXgNMPzmbkmmWOBvIK4tX2cJD4BHy/7iNdRGD+Twtlbs8Oo+cLLoWh7JytbqNi
            hURbjnMB7gdFuox2MblC1FYnugdTdw4XyDe6dKdyKWJjGzbUxWwyy+yjrAxutfAc
            xwVDsRBLvww+Ptzf/eSOQPhrVzu7mhY3yXOmUnRRjkECgYEA63+uDb9IxL6HSIw9
            x4Bc5RQKmO1IoJohVE+/WezxaDkmUB+FSB7VF5XrSpDgY/x4ZR5OX0urS4/C+Xee
            PdnLxYH55eQqGvauVnC0sDA+k9o3TYTJmOfYY9uihQC9w3zRGtNxOFlQsVR92NBE
            4SzuSVtRr8DTOkhKiOlYBYpF2DkCgYEAy2vTIaI4QGSjAfBWfYWNmKvaVHZ6netW
            miTcwQu4qAQodEdnslsNVwZ/uMIktSZ5IEkpiAXxeGu0EWEpierY30NH+TY8BJZS
            I/pCzRVyyt9X/UAoj9yq4chyZXMXZVToN0W3YlVrIJoBdrhvZvwELHrbDZH4JrQw
            0AHsZq7xJGkCgYAC4q6cRoK6vmbj8av0HNOGjwdONmIUba8I3G1IyclvcHvSsYAt
            kQslXdXjNQE62GYVPxjQvBmeNGW8LsYGlfuUMPKB6ZjGec1LC9h67CxoHV1eGslp
            kTWqi49jN84bbhUV0g9qFFYTxihAltSxOZ610WOf1qn/5dDb+pf0gWw3qQKBgFd4
            rRgYXmHqJGIQC9D73dBZjY+mRsGjUeEEmtx0AtpUt2SQ09lQ5+KVC9TRvuEagxlL
            /IzeKWBjx9F1W1xP3SPcFZXnKVW7oeSQl6sCXxM3iOmAbjC2bdCa1f4jyFqtcRFb
            bCjfnCovrxNy6Yx6L/1Ecu9Z5kAWWasIOLRK46yJAoGBAKQ8kYHsTnb7redYqh0w
            oEsJ3Sq3CcMD9813RVMrcTneJwTo/c1aMvYYlz0gAGsaar78av4cvIiCz4YT9WHC
            f/0OyEC+Y9lQB1/ka8BSjpIfM2L0FWDHJUsGOKZ+C+KlGZpRgF8YDFZHdwmWOokL
            GhN8OjQwTBEo9hm21z14qvAC
            -----END PRIVATE KEY-----
            """)
    ),

    Cert(
        names=["tls-context-host-2"],
        pubcert=strip("""
            -----BEGIN CERTIFICATE-----
            MIID0TCCArmgAwIBAgIRAL/XZdKaUkBM0tuy0P4+UNEwDQYJKoZIhvcNAQELBQAw
            eDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAk1BMQ8wDQYDVQQHEwZCb3N0b24xGDAW
            BgNVBAoTD0FtYmFzc2Fkb3IgTGFiczEUMBIGA1UECxMLRW5naW5lZXJpbmcxGzAZ
            BgNVBAMTEnRscy1jb250ZXh0LWhvc3QtMjAgFw0yMTExMTAxMzEyMDBaGA8yMDk5
            MTExMDEzMTIwMFoweDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAk1BMQ8wDQYDVQQH
            EwZCb3N0b24xGDAWBgNVBAoTD0FtYmFzc2Fkb3IgTGFiczEUMBIGA1UECxMLRW5n
            aW5lZXJpbmcxGzAZBgNVBAMTEnRscy1jb250ZXh0LWhvc3QtMjCCASIwDQYJKoZI
            hvcNAQEBBQADggEPADCCAQoCggEBAK8SUPO0DNCdowxE43ptSscXXon5altJPfu0
            ZSo38e2ljRKfBDD2f/Wi2+yEAdZ9zB/TzPoSyMZt1YXbNI8FYYFwOCXqtPadOcvy
            zJUvCxmJtDK78RsvobskdBDryy0Vr5heGS8L/707n8cmXpat4JyjZRyyLUg0Rhws
            KxA5nZkS14jAbD3l8EcZ+ALMlLGBynu2PYYthfZ9yJx8CxUYYPReSFXXQauovMDT
            wzqHBvY2WLkU+cEWyYCaBo4yAsA5P5q34ZRVXn7ePbidnguJJ/34REGqJj3/13dP
            79qOtTB0NZQuajMvacEcdgkrN5rD5I+yPYckFrzGXkhObhxP4cMCAwEAAaNUMFIw
            DgYDVR0PAQH/BAQDAgWgMBMGA1UdJQQMMAoGCCsGAQUFBwMBMAwGA1UdEwEB/wQC
            MAAwHQYDVR0RBBYwFIISdGxzLWNvbnRleHQtaG9zdC0yMA0GCSqGSIb3DQEBCwUA
            A4IBAQAzG/5JEIFnh4+31pxdmHq7VawsPpLQzAWbRvZ4BG+6DI54jLGgU8ZDXIxw
            +2F6SgPiyxWHD6UbQEWlWkp+qWs1D9ribWWuT/AnKDtg6G1aOTm5yygKtyrmb8p1
            MujfSE17y7AgOF/3FcegZwZuHZxlQqwJZD6yTCiQYWBczVhPKXvlXIi4SkhnHX1b
            aRMRTWvHdNMclm8BA5zbTL8njhUCKkjNXSySjtyOc22f4K6A9GS3R1/fYDxKKgol
            aqFfLS8P0/niK+fGyBE8Lp6P9g63hS60bAOYxraJbGieFqbtKZH2H9von7e6Do3N
            c1ySbPcvlmzY90yzieRidmD4dNDb
            -----END CERTIFICATE-----
            """),
        privkey=strip("""
            -----BEGIN PRIVATE KEY-----
            MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCvElDztAzQnaMM
            RON6bUrHF16J+WpbST37tGUqN/HtpY0SnwQw9n/1otvshAHWfcwf08z6EsjGbdWF
            2zSPBWGBcDgl6rT2nTnL8syVLwsZibQyu/EbL6G7JHQQ68stFa+YXhkvC/+9O5/H
            Jl6WreCco2Ucsi1INEYcLCsQOZ2ZEteIwGw95fBHGfgCzJSxgcp7tj2GLYX2fcic
            fAsVGGD0XkhV10GrqLzA08M6hwb2Nli5FPnBFsmAmgaOMgLAOT+at+GUVV5+3j24
            nZ4LiSf9+ERBqiY9/9d3T+/ajrUwdDWULmozL2nBHHYJKzeaw+SPsj2HJBa8xl5I
            Tm4cT+HDAgMBAAECggEAcdo7gwFIhDK/4i66sNd6ldcAyEHHhO4wvQwn7jjLwHy1
            LbL0CtODi78JvtpqR48vvFMFLmwg3cp33cEcgRZCvua33RCx9t9wws13dl1NnqIK
            6iOHPOLRDt86C/cL/pnnw/MN9aab/fhUhDLTuLIDLFqmWu8Uu6wjHBctOjP95Zlj
            5JBkbHIjJkNVejbfEoBMKVFAFeNYoeuhv8NhBO3XwYVryTp9+PHAwd9a5EbBMryR
            nQA+XWi7H0iDXEPG/oBvmyh9Rbo+J8r9aBPDRbYZmCCVzihT1R/tiaHSozNHwh2F
            dUCpg1wFDRSmf2wKMFK3BPOMKvvxdN3FvyY95klmYQKBgQDXZDz2Ik+KJJmkCPyk
            VWTU7IddPJ1+I/xccirNRKJ1Dtm9zZQXd/gxrH3hFVyyRhYxOtUAbU85h7KUpOz0
            /bI/BZph9GbfUcYzZ8otCYyakNUARE6auhR6IWPF7Qu4LC+NHg+k6+JeWHOzn0BR
            ZXbJ6phe3U/ZNtayjratuT1P7QKBgQDQFA3GU5POen6frF+buyQOFJexwO23yHwp
            qgjGBHXYZBrp7LoA7ZtLOEcy4C0Pmn3IVvSt7EF38iemvYXntmvpeL1XwHdTv5lq
            I1x3myt63Vn2OWLu4RhA84PEmlI4pDo7s6msiAS/PSlTmqbSuIDWLAqO7dKgvzIK
            Kq8+L3fibwKBgHFldW7D24pIAJdKn+/IgWBT8mQU0Hmjam4lMQGGe90S53G0tJ2y
            bHmCbXc9ruKwYWijp5Yk9ku8dDkrpxDIK7pgMcoWSL6Tp7xSjS8u0tZhH7KXQ6bU
            BonR4FxIkx3wLUynIedaxH+VI7zSP6NavrJJDtUKwMoDw/6XgfduCah1AoGABke0
            qrm3ClJUJAmV0SNy0SH5+hlyk0tvw+on3aIg1GkhDtJgQsrpFvoZ3AU8Fu54wWUu
            eVlaGH6sh7HMqtOsqh1EybM7ZsGvpa5vigSa6Vho8K+GtuMAUmWHIpXtyVvbjhW8
            F0L7sbHs32MZid6btNsbbnjrFILwxbHIHD5ehe0CgYEAg/fe434Wmq+UykjhkYqy
            wu2oXSgG8PsdiE4jmtfQ6aUtbnWyWfl8GpzzAb+niNHrE4LdohC3virNdBKVuCcn
            Nwq6gHnTGSbrM+WAa78lvYD6arIW6fD8MvCQXWMN4J1FVk86H2vXhaSObOTls9+D
            OGSk6BLtLUX79aY4TfNg0yk=
            -----END PRIVATE KEY-----
            """)
    ),

    Cert(
        names=["tls-context-host-1"],
        pubcert=strip("""
            -----BEGIN CERTIFICATE-----
            MIID0TCCArmgAwIBAgIRAKLpGzzKxkWzv1M5uTQKopwwDQYJKoZIhvcNAQELBQAw
            eDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAk1BMQ8wDQYDVQQHEwZCb3N0b24xGDAW
            BgNVBAoTD0FtYmFzc2Fkb3IgTGFiczEUMBIGA1UECxMLRW5naW5lZXJpbmcxGzAZ
            BgNVBAMTEnRscy1jb250ZXh0LWhvc3QtMTAgFw0yMTExMTAxMzEyMDBaGA8yMDk5
            MTExMDEzMTIwMFoweDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAk1BMQ8wDQYDVQQH
            EwZCb3N0b24xGDAWBgNVBAoTD0FtYmFzc2Fkb3IgTGFiczEUMBIGA1UECxMLRW5n
            aW5lZXJpbmcxGzAZBgNVBAMTEnRscy1jb250ZXh0LWhvc3QtMTCCASIwDQYJKoZI
            hvcNAQEBBQADggEPADCCAQoCggEBALHxyYppaONKVQFrI4d1I7+xnmJ1Dj4jI6Ic
            utoEKTlLLZxFtI/Kjj+S4cPfUmV3Arm2vsG3ajZ5AMia50N264zpE3G9/w1riRrc
            OCZgbMnOm/Uy2nMcDEbNN1eW2AlXU5NVbwraHOk/EywiCgEZYPBPSrDRAntJpjo6
            0Oe+yve98yMCvmJOsdIuxExojaAdfEo0o9on0/iy0cereeiegxjLO8QM7uwTDqSH
            +4dApzvy2PwwUEhUUZrNRdyp7tdW36IzTi7KeCWnX2++2yPNQTt7N3x3SNHf6gj1
            fjQ6jYXwGQ0bF95KV5HXbTMEIXRb3hDX2jYiX3cXNOapx5KIio0CAwEAAaNUMFIw
            DgYDVR0PAQH/BAQDAgWgMBMGA1UdJQQMMAoGCCsGAQUFBwMBMAwGA1UdEwEB/wQC
            MAAwHQYDVR0RBBYwFIISdGxzLWNvbnRleHQtaG9zdC0xMA0GCSqGSIb3DQEBCwUA
            A4IBAQAvdh1cc3sOkksjlSJYj8qRyC5kxFm79YTWga3zm8EsUz7I8gjULCfSeEmT
            aEu6wjFJWTxMBulU0jbu3QVNinQcOqxTEAXdMaP2/2akHZv/u0QHFsOH1K5b9X6w
            iszEJlwvH8pm0hczzQ9RNgCo8JcmPf+SWlhNsvIjXTaY4VaezoWd80US/90EZWEg
            CU7vaeTtUXiIkDFbnvoHnBfKtzFVPozdRK92Um5TqYAQhTfoLy1lZ37ehLtEi3/r
            YnZJ/kVvvj0xu0b3ABS4X7tdquIFpRH9TlHzytPoExDP0yK4rDTBReRltjmG7Mo8
            C5c5xkWcqYhep7KMpnkU02onYioc
            -----END CERTIFICATE-----
            """),
        privkey=strip("""
            -----BEGIN PRIVATE KEY-----
            MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCx8cmKaWjjSlUB
            ayOHdSO/sZ5idQ4+IyOiHLraBCk5Sy2cRbSPyo4/kuHD31JldwK5tr7Bt2o2eQDI
            mudDduuM6RNxvf8Na4ka3DgmYGzJzpv1MtpzHAxGzTdXltgJV1OTVW8K2hzpPxMs
            IgoBGWDwT0qw0QJ7SaY6OtDnvsr3vfMjAr5iTrHSLsRMaI2gHXxKNKPaJ9P4stHH
            q3nonoMYyzvEDO7sEw6kh/uHQKc78tj8MFBIVFGazUXcqe7XVt+iM04uynglp19v
            vtsjzUE7ezd8d0jR3+oI9X40Oo2F8BkNGxfeSleR120zBCF0W94Q19o2Il93FzTm
            qceSiIqNAgMBAAECggEBAJj5yQ6x4hcMbxnCFpA8Nxh0RTpVcYIfyWFzm3sT+rCj
            nblr/3diZnnm9ynh0j8iWfh4T3PQD4J28iKDcO+By6yfLzUoZp0N5pdt3OO5H606
            br8UEdLFuRQhFkO5jU4ygcn2t3i33AT1UbEuLjWVsM3HDOoHNT/yJ/KFX9TrJChn
            9nV9O7iaeBHMaLHHr2i3DCs5eFkNJfyXeW5qqrsLOPNwVc2LPg1DIwtG6trugpzS
            ZXdMI8/yVohuHMZu08eaknhJRhgDfPWCnr0oUy2EHQePw8k3ngsJOJlYDqdN5gsy
            bKGd88gRk57jgGbvZMAhdPVT75i9R76x9/8QCsFuHS0CgYEAwezbF+LAlETtEkHI
            v373OkYMoeKwsLI+VT2p7ypvYy2XbJTSoon8rUJv7VF1D8qnyIMSDGc0ltFX/Lqh
            QybhXQRk+Eup67k6QbZm+SQB5+dIo0sPTEuYpN3ftrAcirYlR5cZeJr6y1/7vXdl
            VziJPMXzopWHevxJyGjxlt1wkXsCgYEA6udlDcYtjYy6NRd+t3fK1oOg6h+I2DtN
            c3A859BmdWgXQ6oRbdh85TRykQ2N2Ax8PXr/IFL2bwsjytrVv24Stdo+ZFlETbJq
            an3pHjfnZk6usKs30RxHxYuOIm435SwcOZlmSreTKQLt/MZgVA15uM2NZT01+llT
            R6LyQ8/PwZcCgYBcPdKVEPlzTTnK1lmrpLPqFwnJMu/CjHYTy6n6JiAnd7cwIbXz
            NFlo/FIK+xUIdufJ+3ZpSen81wTYJNmx/Ft0CDQS2sKvakKooR9n4FW7vgqSCZD0
            RH0N5q+T0T8yR6OB4wBtmqIyfKxcmd8tVqoIq0vRCPkRadGarzhC/3+c4wKBgQC/
            5HFv1CHoTTrcHipc9BYWMQcl2sbuZVt63whSErNwW60NkIOWaVB16OdiSWFDScfA
            bZa2sC8yPTZrA2OzctcECZoIXcfndMVr4xmpnt+AeuxH1EbPozuaS8u7orA0nVkd
            UIv4o4gq64LAiMmuQCfcaMaGGn/a2Feo4Jrp/HxqVwKBgE+ShxXc3RtOFRFaca1w
            sVnXLttEBfYBmeOxEmHaruCBuRlwx4U35Dq5fx5MYoeoaMoyGm8kqknFPSNZywdk
            /DlPdOnqrlBhY3TdmVk60j7IM8182GKjcMImfFoMjot/oZlKxrq+PcsVoIHeOQL6
            b6gCAPn1RvigtZtc5EUILDfG
            -----END PRIVATE KEY-----
            """)
    ),

    Cert(
        names=["localhost"],
        pubcert=strip("""
            -----BEGIN CERTIFICATE-----
            MIIDtTCCAp2gAwIBAgIQBmwf1lv4+/h6sWcQkb0rdzANBgkqhkiG9w0BAQsFADBv
            MQswCQYDVQQGEwJVUzELMAkGA1UECBMCTUExDzANBgNVBAcTBkJvc3RvbjEYMBYG
            A1UEChMPQW1iYXNzYWRvciBMYWJzMRQwEgYDVQQLEwtFbmdpbmVlcmluZzESMBAG
            A1UEAxMJbG9jYWxob3N0MCAXDTIxMTExMDEzMTIwMFoYDzIwOTkxMTEwMTMxMjAw
            WjBvMQswCQYDVQQGEwJVUzELMAkGA1UECBMCTUExDzANBgNVBAcTBkJvc3RvbjEY
            MBYGA1UEChMPQW1iYXNzYWRvciBMYWJzMRQwEgYDVQQLEwtFbmdpbmVlcmluZzES
            MBAGA1UEAxMJbG9jYWxob3N0MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKC
            AQEAnqRejON4fDVxvJFvvteylUBDWAjKmQGX3ta09jvcdWp6fvYvIBJgS/A036Gx
            QCDijZjm9r0Ruq+StclqCKwC6Y3yAmaVsRclBhAcUCXhym2PFKV54268UHTlMGV8
            B23BggWq3kzlgCDRQ6xOdzC39OYm3HfdX7jyeGoEPOsFlsbVwNHAcO7FEShRhfnN
            VIG9vlYXogaSQPWoBu1HkfyO24rrLV0+FlhB6ddTjKi1JP5XSQAZX2zVRuocgFut
            3pt0SX47MqkO2/+CSEjVD42RosnyTobFsfLQFEAbhxaM1QhfFVxcfQXHWfvJhuNA
            m2P75gGj/vezqW1mXRpubFxqswIDAQABo0swSTAOBgNVHQ8BAf8EBAMCBaAwEwYD
            VR0lBAwwCgYIKwYBBQUHAwEwDAYDVR0TAQH/BAIwADAUBgNVHREEDTALgglsb2Nh
            bGhvc3QwDQYJKoZIhvcNAQELBQADggEBACGfmKYqlwHH7ZldKgHDrkK1obomlAU3
            2WQ43DHhSUsausgrTDwuXQ+3K6KpcyDwCJBXBPDVtouawfSaMfqKg3bjo+ttPwey
            xJsLvdk/U0djpBDJ4GwJFMYsPPBBwGkDFu0w1Xy4IEbVPmzOJ9Lnj8Uf+YIbWwqC
            BcTvz0BmIcZtkMXn9EdHWjQ1g/DodRkd3yeZjRMQ7WvcvUasOhG9CFGFjsC4ZDbv
            x2Pz354apCjhr2Dqvg21/9LQgm4zmJakw8HwagRv3eNunLXQYYBcPtfeEVgXyTz+
            G0w3VUUFGNg+m+Mu+CqS73826wC/xE4I/1pUdoKkU+AqqakggSEH6Wk=
            -----END CERTIFICATE-----
            """),
        privkey=strip("""
            -----BEGIN PRIVATE KEY-----
            MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCepF6M43h8NXG8
            kW++17KVQENYCMqZAZfe1rT2O9x1anp+9i8gEmBL8DTfobFAIOKNmOb2vRG6r5K1
            yWoIrALpjfICZpWxFyUGEBxQJeHKbY8UpXnjbrxQdOUwZXwHbcGCBareTOWAINFD
            rE53MLf05ibcd91fuPJ4agQ86wWWxtXA0cBw7sURKFGF+c1Ugb2+VheiBpJA9agG
            7UeR/I7biustXT4WWEHp11OMqLUk/ldJABlfbNVG6hyAW63em3RJfjsyqQ7b/4JI
            SNUPjZGiyfJOhsWx8tAUQBuHFozVCF8VXFx9BcdZ+8mG40CbY/vmAaP+97OpbWZd
            Gm5sXGqzAgMBAAECggEAUYFzjoEkGvS+bbpvJibd+q6cqvNBW+EkrPm02bmhp7XA
            H9DOH3UxgnJ0R91kGuWKYGOJboVvQXIJN1q3HqN5j5M9HpykFeslO3s1gLwlyIIH
            e/0UpZP0LoYQZpANbCeovuu4gSQS2YSC33j8i2I9cRZ6KtVuqEp2UQVvDflV0sOg
            Pm7MxqRlYQtaEGNyR91/ib6c6B07gfXfcbrLAk2I1V2zWZW5GtFfk3Xf4PjAlpYA
            Ip9d9u8tiXFKtSPhNmlowyE+dQDstKrv7FFYWfjp2lbodIeGQpr28KWW7MIuUc57
            xeioRTpf6y1kuGNaNHz0VN15Z7E2fOLMvmqurzGsIQKBgQDRUq0uI1wa70EDxE3J
            PxPiZ2aX81fTaVxhv9am5fl7Eb6lLu/V8nYqNZtWCUfwirQnzj5SK2RRO+OKmH9l
            M58g7QvRfDOh7MmLRGXS5+9nhmjPMvEv+7RPq4uwiPn9gSfI2NHJLcMpdRE7ojcG
            OZF6zxnusPrmEK5eilnw1WpAcQKBgQDCBItyI5h1OE3QXM6RAKrE0VW1Us6eu7sc
            wNNV6y5aORn+RdOQFQX303TT3X+7DP/FBJCVFvdKnO+P6wTT7+bmK6x65MIJDqEI
            gAa0+Xc5LZRGv0jGAzzit/Biy0EhLu+XOsBXpGyF9qLrdQuUhEUqi81sM2FGcA2I
            vtBL4dzvYwKBgQCNGY8Vh85hdZ+8u0m3+6YauprEmMs9/krAtYErNeCrHfYGARK4
            hF007LfOEimFMupn3rXRy+AuhhFG7q8Jd/evSTrrNi7T2vqsvyloNuIBRfBGo09D
            igcsoTVjhaIGSVaZI9aeJxPkUT6RlTJEJvAy+YHAjVpDVUFFBzvDhQi/cQKBgBk6
            kg9zhX2opqWzi8DbP1l8hxKfA/MsIjao9FI11L8ysaiY19vif/Yr7wMlyFhAZnnu
            EAbzB5ESOyyRuPz+Mx43C6SnXnvjBRmf3D9oORKcVK2mbgYhoacxl/agy4VPHySh
            JSXAYcRBwAmyHKFhWcUgjMPHIp0QMRJZDajwY9RVAoGAPLFojNBnu5smAsdZtkg8
            HbLFL8iPT96w8ZarCHH+XLywlzjG02c0XDQIC5QeopKRbg0NmJJImmwWIJGhjXC0
            dYfI6Lw45AhpQsANPM2dB5ak+3TJGr2RvpSIF6M0+CA69A+VL7NOeBt0acXZv9p7
            rSbwm9Ewfog/UaoT+fUUfcs=
            -----END PRIVATE KEY-----
            """)
    ),

    Cert(
        names=[
            "a.domain.com",
            "b.domain.com",
            "*.domain.com",
            #"localhost",  # don't clash with the other "localhost" cert
            "127.0.0.1",
            "0:0:0:0:0:0:0:1"
        ],
        # Note: This cert is signed by a cert not present in this file
        # (rather than being self-signed).
        pubcert=strip("""
            -----BEGIN CERTIFICATE-----
            MIIEADCCAuigAwIBAgIRAJ3dtx28bAfwdex3/R/ETrAwDQYJKoZIhvcNAQELBQAw
            cjELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAk1BMQ8wDQYDVQQHEwZCb3N0b24xGDAW
            BgNVBAoTD0FtYmFzc2Fkb3IgTGFiczEUMBIGA1UECxMLRW5naW5lZXJpbmcxFTAT
            BgNVBAMTDGEuZG9tYWluLmNvbTAgFw0yMTExMTAxMzEyMDBaGA8yMDk5MTExMDEz
            MTIwMFowcjELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAk1BMQ8wDQYDVQQHEwZCb3N0
            b24xGDAWBgNVBAoTD0FtYmFzc2Fkb3IgTGFiczEUMBIGA1UECxMLRW5naW5lZXJp
            bmcxFTATBgNVBAMTDGEuZG9tYWluLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEP
            ADCCAQoCggEBAOBpsKtx/b4PEReo2nZj6aaXW7leNtpZlfy3XgfTKnuGsHicuDrf
            Pgcapqllm9o9H/F6Y9NhpBliJJmZk90S6UR/BlIWEKLMkXal78yQJU9cluvh0lmA
            e2FFTK3Yis1kWsGvbOEusnCerFXUbjWCLr9VfLo33oYiSbfo9r+f/o0Q0Q/QPevV
            Vmd9yuxGIeZlucno/TK4yicGW8awATH0JsvKfbEDf0drztgeFq8RynlkNxEH56Qw
            6tLS1rJ6CRY5yyYImwtA3/zyZzSTsSgm7EMYhPg4JSf0wuLTY1uOjfvidfIwhCGu
            Qxy8h8Z0eAQl0YigXersY2FL4MULD6PqrK0CAwEAAaOBjjCBizAOBgNVHQ8BAf8E
            BAMCBaAwEwYDVR0lBAwwCgYIKwYBBQUHAwEwDAYDVR0TAQH/BAIwADBWBgNVHREE
            TzBNggxhLmRvbWFpbi5jb22CDGIuZG9tYWluLmNvbYIMKi5kb21haW4uY29tggls
            b2NhbGhvc3SHBH8AAAGHEAAAAAAAAAAAAAAAAAAAAAEwDQYJKoZIhvcNAQELBQAD
            ggEBADdqgP0oBxv/wcctrpgdhfgzurWbUFE3VD3/540WFLmA6OrE5OsN8q3AVz7M
            5XtQDBJDQR7I7cGrXXdnJuvTi7RhO2JduAW+oO+ZtRN1yUk4bzmVJzNRAKNGxsPZ
            NGvPacZyEDwmIodqUUOXIQnmJyvKd7pHuQyPyNDZkuVyH/z7m0vutBXSm4DbZ/Ml
            Osh6zGQ9OUwy+4wCFi+PGDnHnGr4FuKzv1ZpSGiycA3l8aUu4qZ7a8gLtHe8UXa+
            W2OKptRz/ACOsjKEQjCwWXjOV5/LJwtI2qAM/BUEY/GiHeJoNT515bt/sh7yC4Cn
            pgEAi+5QCFXEtyrT2rtCGfzYZZY=
            -----END CERTIFICATE-----
            """),
        privkey=strip("""
            -----BEGIN PRIVATE KEY-----
            MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDgabCrcf2+DxEX
            qNp2Y+mml1u5XjbaWZX8t14H0yp7hrB4nLg63z4HGqapZZvaPR/xemPTYaQZYiSZ
            mZPdEulEfwZSFhCizJF2pe/MkCVPXJbr4dJZgHthRUyt2IrNZFrBr2zhLrJwnqxV
            1G41gi6/VXy6N96GIkm36Pa/n/6NENEP0D3r1VZnfcrsRiHmZbnJ6P0yuMonBlvG
            sAEx9CbLyn2xA39Ha87YHhavEcp5ZDcRB+ekMOrS0tayegkWOcsmCJsLQN/88mc0
            k7EoJuxDGIT4OCUn9MLi02Nbjo374nXyMIQhrkMcvIfGdHgEJdGIoF3q7GNhS+DF
            Cw+j6qytAgMBAAECggEAdAXQpGMT+B5cDOpswEbZtxqL/qN6IpuskvLOt6byUNkL
            BeCo0y82J4Ac6HmzATsW98b6M4BI0iLOn2cqbmLnnVU7FFd6FGFFV51lBFMGJyjM
            knm3QjTOFTU59qt838Hhtj+XQDjfYqB2ow1oSVvcBWoSSUi3UIwLpvzYDayPc6hk
            65Jq4tlA6iEfXtwmVIcn5k14lXXVMof9kIAPEoZCKl++RDaUCFwJBH4SI6yN+VkN
            aKKVRxL4dsk6AyubJ/dZW91VfBTaQUs4487s3sQ5Ybk0dCcRjoZw1lT0fYvfR/Hc
            2zCvuNndKz1luPB/wXNsQ2cPEuXXMOtE4tF9LKOqFQKBgQDjM0aC1jd1AzKwNtsW
            E3kS3tKi32d2jq+IekP0ITJZ5tbTXczIMZPvkZIUPz5bKtCnIhiUQd8TxHGI0DPX
            VwchFQcRxSsfWXf+4ilnAKqJc7ZLMSBzbIJOEVvQagP5ChNU5qfoqKICyE7UlbEZ
            Xrgp3SunaK+Js5rf3pKppcHtZwKBgQD82/YUWYBD1+vN3Np8sGhagcjlRw1WhhlW
            trEYei7ILrspP602Xy7gn77UequVKQiLZRgQrg+RRrcwKGvokYGrNpbEoD27sjzh
            5VThS4ZEcA9o1IHMDu81Yny6ZtI9F3TldIMP81fGaEekxa+q4XRpYl63LIeeND/0
            EB7WLLG0ywKBgQCW4Fklz53aTbpefL82xM21M1WLpXHusEhvCEqSF215eCsXCAZS
            t2G3SONKIMmG/0K6ipDp+2hplx2SLjkO+pMYa/9a1KWTVvWxxHycEzwstTPMcR5M
            qDVMJIjlOVHUEtXNnrLIdRvJXz3CPHn0EAuaeW5g6MsRVb02h3a7xACpZwKBgBCa
            JKMbaUeLEsl2ecX8Ey32HYmoS6Dltx4xaplP1GiCYPmJW8cZIsvO0UnEMCXgBtaY
            MadOtmj0eqynysX/X8MtF2MbnlIHluXCF/ue6NbvgKOCaG9Mf7pCmCvo+l7Wfm9e
            YgiXEqlNSX7xF+KhYPJWah+exdzGU3ij4lJvps9XAoGAGf/f9ob2tLmMacLISKdd
            OOuJz2jSzi+ZuoISiN2tQccBuwzf4cWPY27duUum8lD5+gFxZjUav1npQWrugtxT
            OqTouIFDHW+jluzNa++cT2FVM2Tj5G9uKwVxS3SfITfZEHRmfoxwWmrmn+wgz+do
            NuVfL7r0erO8V2bLW2ASEDs=
            -----END PRIVATE KEY-----
            """)
       ),

    Cert(
        names=["acook"],
        pubcert=strip("""
            -----BEGIN CERTIFICATE-----
            MIIDqjCCApKgAwIBAgIRAKcrynhenFaTcxKOdiGvT6QwDQYJKoZIhvcNAQELBQAw
            azELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAk1BMQ8wDQYDVQQHEwZCb3N0b24xGDAW
            BgNVBAoTD0FtYmFzc2Fkb3IgTGFiczEUMBIGA1UECxMLRW5naW5lZXJpbmcxDjAM
            BgNVBAMTBWFjb29rMCAXDTIxMTExMDEzMTIwMFoYDzIwOTkxMTEwMTMxMjAwWjBr
            MQswCQYDVQQGEwJVUzELMAkGA1UECBMCTUExDzANBgNVBAcTBkJvc3RvbjEYMBYG
            A1UEChMPQW1iYXNzYWRvciBMYWJzMRQwEgYDVQQLEwtFbmdpbmVlcmluZzEOMAwG
            A1UEAxMFYWNvb2swggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDAg4ss
            Hk+na8ygSofzl8O4hIcISKs61iFX002Vo4MxyLPbydxvKvekYHrA/CKbzJfNsECX
            0V1+waFPRhoDqZrkG2RBIl2pW4GwFl3eCbr9JyWKrSHA4XH7cLcAuGd5FmeOHKPb
            Hfn6dWVgBXws8ykSX3r/A3A5+l2xnE81jtYPOr4rtyYUCJF60yQ/w7FvSfXZIO8l
            hc6qncfzFm1Pg8SZPi9hhoL7/AzmQ+iuqG624VuanKppFDx5yq10X6guH6faVpbf
            ErrHOIP0N7KcZZjl0bnQdZVlVzXMe+Sra8xWuGqfjMmcL2LkzvtdkTv2AC+8rbNM
            iaa564JoTcj5znYDAgMBAAGjRzBFMA4GA1UdDwEB/wQEAwIFoDATBgNVHSUEDDAK
            BggrBgEFBQcDATAMBgNVHRMBAf8EAjAAMBAGA1UdEQQJMAeCBWFjb29rMA0GCSqG
            SIb3DQEBCwUAA4IBAQAdl8MopS5T3LSo50RPgf7+OiTsCy9V37QIGkctZTGK5s/9
            Xiv/XQ8r/wYs3RTMlE9IsjPHyTkQ01FxwUQTliSM+6fpnYaRfVLPZlYNnz1S4j1S
            pxiM6LcD/Ld0M5faRjCxMmLWqgzrwD6bhV/AS4zmLW3QSHiI8W4L+0q6zp3/4u0D
            lCR3ObLpjoZq0mLTHqJExGZAcioafgxzl5pwKy9YtUO3acYv8CuJOZzyqbpCKXTa
            f+n5Tslk+UdHlBb+4cm8VkExnZ+2+AWPrujvUzy60GW1tCWswfz9ZDaM4lLO4CyU
            1KEHBiKzK5s/c774GnHhGus3SoPsSCqENImvZb/x
            -----END CERTIFICATE-----
            """),
        privkey=strip("""
            -----BEGIN PRIVATE KEY-----
            MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDAg4ssHk+na8yg
            Sofzl8O4hIcISKs61iFX002Vo4MxyLPbydxvKvekYHrA/CKbzJfNsECX0V1+waFP
            RhoDqZrkG2RBIl2pW4GwFl3eCbr9JyWKrSHA4XH7cLcAuGd5FmeOHKPbHfn6dWVg
            BXws8ykSX3r/A3A5+l2xnE81jtYPOr4rtyYUCJF60yQ/w7FvSfXZIO8lhc6qncfz
            Fm1Pg8SZPi9hhoL7/AzmQ+iuqG624VuanKppFDx5yq10X6guH6faVpbfErrHOIP0
            N7KcZZjl0bnQdZVlVzXMe+Sra8xWuGqfjMmcL2LkzvtdkTv2AC+8rbNMiaa564Jo
            Tcj5znYDAgMBAAECggEANMrd+3dEeLEDKGHH7nEL5ynQreDfs/7Mnf0AJaz1aU2U
            pQ0yOfoadyVOBGYgR4FPj8Rpsjhj30LSLZ8XuzFjnHI2h/YYoTzKz7MSgrVAZfO6
            Q9E+lFo+m6lJRhVLqtUOCNapyIjr6FcROcfHSbxU4wjz/cK/n+ackvw+bH2DDiGf
            QsLH+sn8eLc231DvK4pCWwtybYJYXV06m1nqN6/TcxDbewmq2lma6qEFaLp3JEjb
            4TK5f1gY3Q3iLG/kwBK8R7E0w0VBzizkb5c8nTPdKN6B+NI5T3AhRwV2PkXHIrJV
            T1lKHzNJ2QiYmqqUoiACGLpTOpT5euJvoRw6jFaJAQKBgQDGOdJYKB0I4sLh+9zq
            K0MsBK4pzgk4gywTNY645EnsfcaY0Pj3FZY+56CTu+9B9KYwkVMCaqMptwsVyffJ
            G22eAQUY6xfbocGfPdi9K0VB2kH35+BPjXSWuMY+xTnNFYV+u8FmuHmk3w3EzFdJ
            jHE2k94f9CscgsRXQYeeivczoQKBgQD4n4g73aXNuemiSxVZv4iOYj1cqRFFa8tj
            mJnqS/khSD9CEYielp9kEfRL3SFyD6nfgwL3OF14VdNCvHAsVcPspE7dU53P4muh
            sy9SmAkAqCP49Vfgrz1gW1knz82Gkc0aPt1QMaKVONQp0JjTEIzrPxVCey3+gjGP
            RHYeAPkHIwKBgDgj7ifbjIWUu38HNwT3JboUxUK/wKrJs7TpCTfiJ/GbmaB0Jt7L
            tVaxgS/2HQgAAwVkUy8vBnDtD22nWs8RPpVuUoRBKOuiP1UbTgQdeirxZpeQi13c
            gTWitTrX3svvmXRQNrEh9Am2xo6DFQGWjgXYESPZolAb1QGlZISJdQOhAoGAcjb/
            o9joIYFl1ju9/DPkLNzuqZG1sHmbvw5Mrvjl4ydIgDaD168EXDlvTCazBa4ycM7D
            3wSS1ARBgCgHNCbWUfENldmi5uxyW59wfvX/NMEJfYZgL4TxokF0zLhHB6oVWhhF
            HWEf+oNX3DnK6zNwOWYKgzcJYyE2WUWvKYty25cCgYEAp9Q4W7Ob86NLpV4ly80m
            sqoTsyx3rjxWKxzxPPfV2OaLC7C5v+WPaewzsKmr4GKmAmJoXsSCUevYiO0vuWfh
            Kwa//xmc5pgnSmGaUE1XKN59iMJBYzC7CaljdxtuZSipLhZhZfWS3IZqnJYQyjI8
            mBtaOgOj5lu1xVKdSm/8Gp4=
            -----END PRIVATE KEY-----
            """)
        ),
]

TLSCerts: Dict[str, Cert] = { k: v for v in _TLSCerts for k in v.names }
