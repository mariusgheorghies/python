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
from kubernetes.client.models.io_cert_manager_acme_v1_order import IoCertManagerAcmeV1Order  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoCertManagerAcmeV1Order(unittest.TestCase):
    """IoCertManagerAcmeV1Order unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoCertManagerAcmeV1Order
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_cert_manager_acme_v1_order.IoCertManagerAcmeV1Order()  # noqa: E501
        if include_optional :
            return IoCertManagerAcmeV1Order(
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
                spec = kubernetes.client.models.io_cert_manager_acme_v1_order_spec.io_cert_manager_acme_v1_Order_spec(
                    common_name = '0', 
                    dns_names = [
                        '0'
                        ], 
                    duration = '0', 
                    ip_addresses = [
                        '0'
                        ], 
                    issuer_ref = kubernetes.client.models.io_cert_manager_acme_v1_order_spec_issuer_ref.io_cert_manager_acme_v1_Order_spec_issuerRef(
                        group = '0', 
                        kind = '0', 
                        name = '0', ), 
                    request = 'YQ==', ), 
                status = kubernetes.client.models.io_cert_manager_acme_v1_order_status.io_cert_manager_acme_v1_Order_status(
                    authorizations = [
                        kubernetes.client.models.io_cert_manager_acme_v1_order_status_authorizations.io_cert_manager_acme_v1_Order_status_authorizations(
                            challenges = [
                                kubernetes.client.models.io_cert_manager_acme_v1_order_status_challenges.io_cert_manager_acme_v1_Order_status_challenges(
                                    token = '0', 
                                    type = '0', 
                                    url = '0', )
                                ], 
                            identifier = '0', 
                            initial_state = 'valid', 
                            url = '0', 
                            wildcard = True, )
                        ], 
                    certificate = 'YQ==', 
                    failure_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    finalize_url = '0', 
                    reason = '0', 
                    state = 'valid', 
                    url = '0', )
            )
        else :
            return IoCertManagerAcmeV1Order(
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
                spec = kubernetes.client.models.io_cert_manager_acme_v1_order_spec.io_cert_manager_acme_v1_Order_spec(
                    common_name = '0', 
                    dns_names = [
                        '0'
                        ], 
                    duration = '0', 
                    ip_addresses = [
                        '0'
                        ], 
                    issuer_ref = kubernetes.client.models.io_cert_manager_acme_v1_order_spec_issuer_ref.io_cert_manager_acme_v1_Order_spec_issuerRef(
                        group = '0', 
                        kind = '0', 
                        name = '0', ), 
                    request = 'YQ==', ),
        )

    def testIoCertManagerAcmeV1Order(self):
        """Test IoCertManagerAcmeV1Order"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
