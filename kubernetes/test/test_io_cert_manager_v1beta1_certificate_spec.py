# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.20.7
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.io_cert_manager_v1beta1_certificate_spec import IoCertManagerV1beta1CertificateSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoCertManagerV1beta1CertificateSpec(unittest.TestCase):
    """IoCertManagerV1beta1CertificateSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoCertManagerV1beta1CertificateSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_cert_manager_v1beta1_certificate_spec.IoCertManagerV1beta1CertificateSpec()  # noqa: E501
        if include_optional :
            return IoCertManagerV1beta1CertificateSpec(
                common_name = '0', 
                dns_names = [
                    '0'
                    ], 
                duration = '0', 
                email_sa_ns = [
                    '0'
                    ], 
                encode_usages_in_request = True, 
                ip_addresses = [
                    '0'
                    ], 
                is_ca = True, 
                issuer_ref = kubernetes.client.models.io_cert_manager_v1_certificate_spec_issuer_ref.io_cert_manager_v1_Certificate_spec_issuerRef(
                    group = '0', 
                    kind = '0', 
                    name = '0', ), 
                keystores = kubernetes.client.models.io_cert_manager_v1alpha2_certificate_spec_keystores.io_cert_manager_v1alpha2_Certificate_spec_keystores(
                    jks = kubernetes.client.models.io_cert_manager_v1alpha2_certificate_spec_keystores_jks.io_cert_manager_v1alpha2_Certificate_spec_keystores_jks(
                        create = True, 
                        password_secret_ref = kubernetes.client.models.io_cert_manager_v1_certificate_spec_keystores_jks_password_secret_ref.io_cert_manager_v1_Certificate_spec_keystores_jks_passwordSecretRef(
                            key = '0', 
                            name = '0', ), ), 
                    pkcs12 = kubernetes.client.models.io_cert_manager_v1alpha2_certificate_spec_keystores_pkcs12.io_cert_manager_v1alpha2_Certificate_spec_keystores_pkcs12(
                        create = True, 
                        password_secret_ref = kubernetes.client.models.io_cert_manager_v1_certificate_spec_keystores_pkcs12_password_secret_ref.io_cert_manager_v1_Certificate_spec_keystores_pkcs12_passwordSecretRef(
                            key = '0', 
                            name = '0', ), ), ), 
                private_key = kubernetes.client.models.io_cert_manager_v1beta1_certificate_spec_private_key.io_cert_manager_v1beta1_Certificate_spec_privateKey(
                    algorithm = 'RSA', 
                    encoding = 'PKCS1', 
                    rotation_policy = '0', 
                    size = 56, ), 
                renew_before = '0', 
                revision_history_limit = 56, 
                secret_name = '0', 
                secret_template = kubernetes.client.models.io_cert_manager_v1_certificate_spec_secret_template.io_cert_manager_v1_Certificate_spec_secretTemplate(
                    annotations = {
                        'key' : '0'
                        }, 
                    labels = {
                        'key' : '0'
                        }, ), 
                subject = kubernetes.client.models.io_cert_manager_v1_certificate_spec_subject.io_cert_manager_v1_Certificate_spec_subject(
                    countries = [
                        '0'
                        ], 
                    localities = [
                        '0'
                        ], 
                    organizational_units = [
                        '0'
                        ], 
                    organizations = [
                        '0'
                        ], 
                    postal_codes = [
                        '0'
                        ], 
                    provinces = [
                        '0'
                        ], 
                    serial_number = '0', 
                    street_addresses = [
                        '0'
                        ], ), 
                uri_sa_ns = [
                    '0'
                    ], 
                usages = [
                    'signing'
                    ]
            )
        else :
            return IoCertManagerV1beta1CertificateSpec(
                issuer_ref = kubernetes.client.models.io_cert_manager_v1_certificate_spec_issuer_ref.io_cert_manager_v1_Certificate_spec_issuerRef(
                    group = '0', 
                    kind = '0', 
                    name = '0', ),
                secret_name = '0',
        )

    def testIoCertManagerV1beta1CertificateSpec(self):
        """Test IoCertManagerV1beta1CertificateSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
