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
from kubernetes.client.models.v1_node_spec import V1NodeSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1NodeSpec(unittest.TestCase):
    """V1NodeSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1NodeSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_node_spec.V1NodeSpec()  # noqa: E501
        if include_optional :
            return V1NodeSpec(
                config_source = kubernetes.client.models.v1/node_config_source.v1.NodeConfigSource(
                    config_map = kubernetes.client.models.v1/config_map_node_config_source.v1.ConfigMapNodeConfigSource(
                        kubelet_config_key = '0', 
                        name = '0', 
                        namespace = '0', 
                        resource_version = '0', 
                        uid = '0', ), ), 
                external_id = '0', 
                pod_cidr = '0', 
                pod_cid_rs = [
                    '0'
                    ], 
                provider_id = '0', 
                taints = [
                    kubernetes.client.models.v1/taint.v1.Taint(
                        effect = '0', 
                        key = '0', 
                        time_added = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value = '0', )
                    ], 
                unschedulable = True
            )
        else :
            return V1NodeSpec(
        )

    def testV1NodeSpec(self):
        """Test V1NodeSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
