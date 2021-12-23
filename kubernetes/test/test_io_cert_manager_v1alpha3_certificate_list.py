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
from kubernetes.client.models.io_cert_manager_v1alpha3_certificate_list import IoCertManagerV1alpha3CertificateList  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoCertManagerV1alpha3CertificateList(unittest.TestCase):
    """IoCertManagerV1alpha3CertificateList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoCertManagerV1alpha3CertificateList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_cert_manager_v1alpha3_certificate_list.IoCertManagerV1alpha3CertificateList()  # noqa: E501
        if include_optional :
            return IoCertManagerV1alpha3CertificateList(
                api_version = '0', 
                items = [
                    kubernetes.client.models.io/cert_manager/v1alpha3/certificate.io.cert-manager.v1alpha3.Certificate(
                        api_version = '0', 
                        kind = '0', 
                        metadata = kubernetes.client.models.v1/object_meta_v2.v1.ObjectMeta_v2(
                            annotations = {
                                'key' : '0'
                                }, 
                            cluster_name = '0', 
                            creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            deletion_grace_period_seconds = 56, 
                            deletion_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            finalizers = [
                                '0'
                                ], 
                            generate_name = '0', 
                            generation = 56, 
                            labels = {
                                'key' : '0'
                                }, 
                            managed_fields = [
                                kubernetes.client.models.v1/managed_fields_entry.v1.ManagedFieldsEntry(
                                    api_version = '0', 
                                    fields_type = '0', 
                                    fields_v1 = kubernetes.client.models.fields_v1.fieldsV1(), 
                                    manager = '0', 
                                    operation = '0', 
                                    time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                ], 
                            name = '0', 
                            namespace = '0', 
                            owner_references = [
                                kubernetes.client.models.v1/owner_reference_v2.v1.OwnerReference_v2(
                                    api_version = '0', 
                                    block_owner_deletion = True, 
                                    controller = True, 
                                    kind = '0', 
                                    name = '0', 
                                    uid = '0', )
                                ], 
                            resource_version = '0', 
                            self_link = '0', 
                            uid = '0', ), 
                        spec = kubernetes.client.models.io_cert_manager_v1alpha3_certificate_spec.io_cert_manager_v1alpha3_Certificate_spec(
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
                            key_algorithm = 'rsa', 
                            key_encoding = 'pkcs1', 
                            key_size = 56, 
                            keystores = kubernetes.client.models.io_cert_manager_v1alpha3_certificate_spec_keystores.io_cert_manager_v1alpha3_Certificate_spec_keystores(
                                jks = kubernetes.client.models.io_cert_manager_v1alpha3_certificate_spec_keystores_jks.io_cert_manager_v1alpha3_Certificate_spec_keystores_jks(
                                    create = True, 
                                    password_secret_ref = kubernetes.client.models.io_cert_manager_v1_certificate_spec_keystores_jks_password_secret_ref.io_cert_manager_v1_Certificate_spec_keystores_jks_passwordSecretRef(
                                        key = '0', 
                                        name = '0', ), ), 
                                pkcs12 = kubernetes.client.models.io_cert_manager_v1alpha3_certificate_spec_keystores_pkcs12.io_cert_manager_v1alpha3_Certificate_spec_keystores_pkcs12(
                                    create = True, 
                                    password_secret_ref = kubernetes.client.models.io_cert_manager_v1_certificate_spec_keystores_pkcs12_password_secret_ref.io_cert_manager_v1_Certificate_spec_keystores_pkcs12_passwordSecretRef(
                                        key = '0', 
                                        name = '0', ), ), ), 
                            private_key = kubernetes.client.models.io_cert_manager_v1alpha2_certificate_spec_private_key.io_cert_manager_v1alpha2_Certificate_spec_privateKey(
                                rotation_policy = '0', ), 
                            renew_before = '0', 
                            revision_history_limit = 56, 
                            secret_name = '0', 
                            secret_template = kubernetes.client.models.io_cert_manager_v1_certificate_spec_secret_template.io_cert_manager_v1_Certificate_spec_secretTemplate(), 
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
                                ], ), 
                        status = kubernetes.client.models.io_cert_manager_v1_certificate_status.io_cert_manager_v1_Certificate_status(
                            conditions = [
                                kubernetes.client.models.io_cert_manager_v1_certificate_status_conditions.io_cert_manager_v1_Certificate_status_conditions(
                                    last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    message = '0', 
                                    observed_generation = 56, 
                                    reason = '0', 
                                    status = 'True', 
                                    type = '0', )
                                ], 
                            last_failure_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            next_private_key_secret_name = '0', 
                            not_after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            not_before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            renewal_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            revision = 56, ), )
                    ], 
                kind = '0', 
                metadata = kubernetes.client.models.v1/list_meta.v1.ListMeta(
                    continue = '0', 
                    remaining_item_count = 56, 
                    resource_version = '0', 
                    self_link = '0', )
            )
        else :
            return IoCertManagerV1alpha3CertificateList(
                items = [
                    kubernetes.client.models.io/cert_manager/v1alpha3/certificate.io.cert-manager.v1alpha3.Certificate(
                        api_version = '0', 
                        kind = '0', 
                        metadata = kubernetes.client.models.v1/object_meta_v2.v1.ObjectMeta_v2(
                            annotations = {
                                'key' : '0'
                                }, 
                            cluster_name = '0', 
                            creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            deletion_grace_period_seconds = 56, 
                            deletion_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            finalizers = [
                                '0'
                                ], 
                            generate_name = '0', 
                            generation = 56, 
                            labels = {
                                'key' : '0'
                                }, 
                            managed_fields = [
                                kubernetes.client.models.v1/managed_fields_entry.v1.ManagedFieldsEntry(
                                    api_version = '0', 
                                    fields_type = '0', 
                                    fields_v1 = kubernetes.client.models.fields_v1.fieldsV1(), 
                                    manager = '0', 
                                    operation = '0', 
                                    time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                ], 
                            name = '0', 
                            namespace = '0', 
                            owner_references = [
                                kubernetes.client.models.v1/owner_reference_v2.v1.OwnerReference_v2(
                                    api_version = '0', 
                                    block_owner_deletion = True, 
                                    controller = True, 
                                    kind = '0', 
                                    name = '0', 
                                    uid = '0', )
                                ], 
                            resource_version = '0', 
                            self_link = '0', 
                            uid = '0', ), 
                        spec = kubernetes.client.models.io_cert_manager_v1alpha3_certificate_spec.io_cert_manager_v1alpha3_Certificate_spec(
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
                            key_algorithm = 'rsa', 
                            key_encoding = 'pkcs1', 
                            key_size = 56, 
                            keystores = kubernetes.client.models.io_cert_manager_v1alpha3_certificate_spec_keystores.io_cert_manager_v1alpha3_Certificate_spec_keystores(
                                jks = kubernetes.client.models.io_cert_manager_v1alpha3_certificate_spec_keystores_jks.io_cert_manager_v1alpha3_Certificate_spec_keystores_jks(
                                    create = True, 
                                    password_secret_ref = kubernetes.client.models.io_cert_manager_v1_certificate_spec_keystores_jks_password_secret_ref.io_cert_manager_v1_Certificate_spec_keystores_jks_passwordSecretRef(
                                        key = '0', 
                                        name = '0', ), ), 
                                pkcs12 = kubernetes.client.models.io_cert_manager_v1alpha3_certificate_spec_keystores_pkcs12.io_cert_manager_v1alpha3_Certificate_spec_keystores_pkcs12(
                                    create = True, 
                                    password_secret_ref = kubernetes.client.models.io_cert_manager_v1_certificate_spec_keystores_pkcs12_password_secret_ref.io_cert_manager_v1_Certificate_spec_keystores_pkcs12_passwordSecretRef(
                                        key = '0', 
                                        name = '0', ), ), ), 
                            private_key = kubernetes.client.models.io_cert_manager_v1alpha2_certificate_spec_private_key.io_cert_manager_v1alpha2_Certificate_spec_privateKey(
                                rotation_policy = '0', ), 
                            renew_before = '0', 
                            revision_history_limit = 56, 
                            secret_name = '0', 
                            secret_template = kubernetes.client.models.io_cert_manager_v1_certificate_spec_secret_template.io_cert_manager_v1_Certificate_spec_secretTemplate(), 
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
                                ], ), 
                        status = kubernetes.client.models.io_cert_manager_v1_certificate_status.io_cert_manager_v1_Certificate_status(
                            conditions = [
                                kubernetes.client.models.io_cert_manager_v1_certificate_status_conditions.io_cert_manager_v1_Certificate_status_conditions(
                                    last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    message = '0', 
                                    observed_generation = 56, 
                                    reason = '0', 
                                    status = 'True', 
                                    type = '0', )
                                ], 
                            last_failure_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            next_private_key_secret_name = '0', 
                            not_after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            not_before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            renewal_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            revision = 56, ), )
                    ],
        )

    def testIoCertManagerV1alpha3CertificateList(self):
        """Test IoCertManagerV1alpha3CertificateList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
