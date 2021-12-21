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
from kubernetes.client.models.io_xk8s_cluster_v1alpha3_machine_deployment_spec_template_metadata import IoXK8sClusterV1alpha3MachineDeploymentSpecTemplateMetadata  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoXK8sClusterV1alpha3MachineDeploymentSpecTemplateMetadata(unittest.TestCase):
    """IoXK8sClusterV1alpha3MachineDeploymentSpecTemplateMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoXK8sClusterV1alpha3MachineDeploymentSpecTemplateMetadata
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_xk8s_cluster_v1alpha3_machine_deployment_spec_template_metadata.IoXK8sClusterV1alpha3MachineDeploymentSpecTemplateMetadata()  # noqa: E501
        if include_optional :
            return IoXK8sClusterV1alpha3MachineDeploymentSpecTemplateMetadata(
                annotations = {
                    'key' : '0'
                    }, 
                generate_name = '0', 
                labels = {
                    'key' : '0'
                    }, 
                name = '0', 
                namespace = '0', 
                owner_references = [
                    kubernetes.client.models.io_x_k8s_cluster_v1alpha3_machine_deployment_spec_template_metadata_owner_references.io_x_k8s_cluster_v1alpha3_MachineDeployment_spec_template_metadata_ownerReferences(
                        api_version = '0', 
                        block_owner_deletion = True, 
                        controller = True, 
                        kind = '0', 
                        name = '0', 
                        uid = '0', )
                    ]
            )
        else :
            return IoXK8sClusterV1alpha3MachineDeploymentSpecTemplateMetadata(
        )

    def testIoXK8sClusterV1alpha3MachineDeploymentSpecTemplateMetadata(self):
        """Test IoXK8sClusterV1alpha3MachineDeploymentSpecTemplateMetadata"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
