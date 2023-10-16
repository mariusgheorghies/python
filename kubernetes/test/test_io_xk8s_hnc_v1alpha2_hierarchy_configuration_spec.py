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
from kubernetes.client.models.io_xk8s_hnc_v1alpha2_hierarchy_configuration_spec import IoXK8sHncV1alpha2HierarchyConfigurationSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoXK8sHncV1alpha2HierarchyConfigurationSpec(unittest.TestCase):
    """IoXK8sHncV1alpha2HierarchyConfigurationSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoXK8sHncV1alpha2HierarchyConfigurationSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_xk8s_hnc_v1alpha2_hierarchy_configuration_spec.IoXK8sHncV1alpha2HierarchyConfigurationSpec()  # noqa: E501
        if include_optional :
            return IoXK8sHncV1alpha2HierarchyConfigurationSpec(
                allow_cascading_deletion = True, 
                parent = '0'
            )
        else :
            return IoXK8sHncV1alpha2HierarchyConfigurationSpec(
        )

    def testIoXK8sHncV1alpha2HierarchyConfigurationSpec(self):
        """Test IoXK8sHncV1alpha2HierarchyConfigurationSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()