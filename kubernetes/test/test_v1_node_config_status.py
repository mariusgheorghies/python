# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.v1_node_config_status import V1NodeConfigStatus  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1NodeConfigStatus(unittest.TestCase):
    """V1NodeConfigStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1NodeConfigStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_node_config_status.V1NodeConfigStatus()  # noqa: E501
        if include_optional :
            return V1NodeConfigStatus(
                active = kubernetes.client.models.v1/node_config_source.v1.NodeConfigSource(
                    config_map = kubernetes.client.models.v1/config_map_node_config_source.v1.ConfigMapNodeConfigSource(
                        kubelet_config_key = '0', 
                        name = '0', 
                        namespace = '0', 
                        resource_version = '0', 
                        uid = '0', ), ), 
                assigned = kubernetes.client.models.v1/node_config_source.v1.NodeConfigSource(
                    config_map = kubernetes.client.models.v1/config_map_node_config_source.v1.ConfigMapNodeConfigSource(
                        kubelet_config_key = '0', 
                        name = '0', 
                        namespace = '0', 
                        resource_version = '0', 
                        uid = '0', ), ), 
                error = '0', 
                last_known_good = kubernetes.client.models.v1/node_config_source.v1.NodeConfigSource(
                    config_map = kubernetes.client.models.v1/config_map_node_config_source.v1.ConfigMapNodeConfigSource(
                        kubelet_config_key = '0', 
                        name = '0', 
                        namespace = '0', 
                        resource_version = '0', 
                        uid = '0', ), )
            )
        else :
            return V1NodeConfigStatus(
        )

    def testV1NodeConfigStatus(self):
        """Test V1NodeConfigStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
