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
from kubernetes.client.models.io_tigera_operator_v1_api_server_status import IoTigeraOperatorV1APIServerStatus  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoTigeraOperatorV1APIServerStatus(unittest.TestCase):
    """IoTigeraOperatorV1APIServerStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoTigeraOperatorV1APIServerStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_tigera_operator_v1_api_server_status.IoTigeraOperatorV1APIServerStatus()  # noqa: E501
        if include_optional :
            return IoTigeraOperatorV1APIServerStatus(
                state = '0'
            )
        else :
            return IoTigeraOperatorV1APIServerStatus(
        )

    def testIoTigeraOperatorV1APIServerStatus(self):
        """Test IoTigeraOperatorV1APIServerStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()