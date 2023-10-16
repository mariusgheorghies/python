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
from kubernetes.client.models.io_cert_manager_v1_issuer_status import IoCertManagerV1IssuerStatus  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoCertManagerV1IssuerStatus(unittest.TestCase):
    """IoCertManagerV1IssuerStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoCertManagerV1IssuerStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_cert_manager_v1_issuer_status.IoCertManagerV1IssuerStatus()  # noqa: E501
        if include_optional :
            return IoCertManagerV1IssuerStatus(
                acme = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_status_acme.io_cert_manager_v1_ClusterIssuer_status_acme(
                    last_registered_email = '0', 
                    uri = '0', ), 
                conditions = [
                    kubernetes.client.models.io_cert_manager_v1_cluster_issuer_status_conditions.io_cert_manager_v1_ClusterIssuer_status_conditions(
                        last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '0', 
                        observed_generation = 56, 
                        reason = '0', 
                        status = 'True', 
                        type = '0', )
                    ]
            )
        else :
            return IoCertManagerV1IssuerStatus(
        )

    def testIoCertManagerV1IssuerStatus(self):
        """Test IoCertManagerV1IssuerStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()