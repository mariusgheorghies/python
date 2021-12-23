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
from kubernetes.client.models.io_xk8s_cluster_controlplane_v1alpha3_aws_managed_control_plane_spec_iam_authenticator_config_map_roles import IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecIamAuthenticatorConfigMapRoles  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecIamAuthenticatorConfigMapRoles(unittest.TestCase):
    """IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecIamAuthenticatorConfigMapRoles unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecIamAuthenticatorConfigMapRoles
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_xk8s_cluster_controlplane_v1alpha3_aws_managed_control_plane_spec_iam_authenticator_config_map_roles.IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecIamAuthenticatorConfigMapRoles()  # noqa: E501
        if include_optional :
            return IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecIamAuthenticatorConfigMapRoles(
                groups = [
                    '0'
                    ], 
                rolearn = '0123456789101112131415161718192021222324252627282930', 
                username = '0'
            )
        else :
            return IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecIamAuthenticatorConfigMapRoles(
                groups = [
                    '0'
                    ],
                rolearn = '0123456789101112131415161718192021222324252627282930',
                username = '0',
        )

    def testIoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecIamAuthenticatorConfigMapRoles(self):
        """Test IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecIamAuthenticatorConfigMapRoles"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
