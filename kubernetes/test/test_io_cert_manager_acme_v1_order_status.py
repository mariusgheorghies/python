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
from kubernetes.client.models.io_cert_manager_acme_v1_order_status import IoCertManagerAcmeV1OrderStatus  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoCertManagerAcmeV1OrderStatus(unittest.TestCase):
    """IoCertManagerAcmeV1OrderStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoCertManagerAcmeV1OrderStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_cert_manager_acme_v1_order_status.IoCertManagerAcmeV1OrderStatus()  # noqa: E501
        if include_optional :
            return IoCertManagerAcmeV1OrderStatus(
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
                url = '0'
            )
        else :
            return IoCertManagerAcmeV1OrderStatus(
        )

    def testIoCertManagerAcmeV1OrderStatus(self):
        """Test IoCertManagerAcmeV1OrderStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
