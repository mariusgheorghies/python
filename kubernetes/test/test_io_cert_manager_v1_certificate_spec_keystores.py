# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.25.12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.io_cert_manager_v1_certificate_spec_keystores import IoCertManagerV1CertificateSpecKeystores  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoCertManagerV1CertificateSpecKeystores(unittest.TestCase):
    """IoCertManagerV1CertificateSpecKeystores unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoCertManagerV1CertificateSpecKeystores
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_cert_manager_v1_certificate_spec_keystores.IoCertManagerV1CertificateSpecKeystores()  # noqa: E501
        if include_optional :
            return IoCertManagerV1CertificateSpecKeystores(
                jks = kubernetes.client.models.io_cert_manager_v1_certificate_spec_keystores_jks.io_cert_manager_v1_Certificate_spec_keystores_jks(
                    create = True, 
                    password_secret_ref = kubernetes.client.models.io_cert_manager_v1_certificate_spec_keystores_jks_password_secret_ref.io_cert_manager_v1_Certificate_spec_keystores_jks_passwordSecretRef(
                        key = '0', 
                        name = '0', ), ), 
                pkcs12 = kubernetes.client.models.io_cert_manager_v1_certificate_spec_keystores_pkcs12.io_cert_manager_v1_Certificate_spec_keystores_pkcs12(
                    create = True, 
                    password_secret_ref = kubernetes.client.models.io_cert_manager_v1_certificate_spec_keystores_pkcs12_password_secret_ref.io_cert_manager_v1_Certificate_spec_keystores_pkcs12_passwordSecretRef(
                        key = '0', 
                        name = '0', ), )
            )
        else :
            return IoCertManagerV1CertificateSpecKeystores(
        )

    def testIoCertManagerV1CertificateSpecKeystores(self):
        """Test IoCertManagerV1CertificateSpecKeystores"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
