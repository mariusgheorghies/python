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
from kubernetes.client.models.v1_pod_security_context import V1PodSecurityContext  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1PodSecurityContext(unittest.TestCase):
    """V1PodSecurityContext unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1PodSecurityContext
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_pod_security_context.V1PodSecurityContext()  # noqa: E501
        if include_optional :
            return V1PodSecurityContext(
                fs_group = 56, 
                fs_group_change_policy = '0', 
                run_as_group = 56, 
                run_as_non_root = True, 
                run_as_user = 56, 
                se_linux_options = kubernetes.client.models.v1/se_linux_options.v1.SELinuxOptions(
                    level = '0', 
                    role = '0', 
                    type = '0', 
                    user = '0', ), 
                seccomp_profile = kubernetes.client.models.v1/seccomp_profile.v1.SeccompProfile(
                    localhost_profile = '0', 
                    type = 'Localhost', ), 
                supplemental_groups = [
                    56
                    ], 
                sysctls = [
                    kubernetes.client.models.v1/sysctl.v1.Sysctl(
                        name = '0', 
                        value = '0', )
                    ], 
                windows_options = kubernetes.client.models.v1/windows_security_context_options.v1.WindowsSecurityContextOptions(
                    gmsa_credential_spec = '0', 
                    gmsa_credential_spec_name = '0', 
                    host_process = True, 
                    run_as_user_name = '0', )
            )
        else :
            return V1PodSecurityContext(
        )

    def testV1PodSecurityContext(self):
        """Test V1PodSecurityContext"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
