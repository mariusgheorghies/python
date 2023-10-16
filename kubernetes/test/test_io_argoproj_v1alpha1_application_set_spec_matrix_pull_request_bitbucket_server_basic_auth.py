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
from kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_matrix_pull_request_bitbucket_server_basic_auth import IoArgoprojV1alpha1ApplicationSetSpecMatrixPullRequestBitbucketServerBasicAuth  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoArgoprojV1alpha1ApplicationSetSpecMatrixPullRequestBitbucketServerBasicAuth(unittest.TestCase):
    """IoArgoprojV1alpha1ApplicationSetSpecMatrixPullRequestBitbucketServerBasicAuth unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoArgoprojV1alpha1ApplicationSetSpecMatrixPullRequestBitbucketServerBasicAuth
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_matrix_pull_request_bitbucket_server_basic_auth.IoArgoprojV1alpha1ApplicationSetSpecMatrixPullRequestBitbucketServerBasicAuth()  # noqa: E501
        if include_optional :
            return IoArgoprojV1alpha1ApplicationSetSpecMatrixPullRequestBitbucketServerBasicAuth(
                password_ref = kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_matrix_pull_request_bitbucket_server_basic_auth_password_ref.io_argoproj_v1alpha1_ApplicationSet_spec_matrix_pullRequest_bitbucketServer_basicAuth_passwordRef(
                    key = '0', 
                    secret_name = '0', ), 
                username = '0'
            )
        else :
            return IoArgoprojV1alpha1ApplicationSetSpecMatrixPullRequestBitbucketServerBasicAuth(
                password_ref = kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_matrix_pull_request_bitbucket_server_basic_auth_password_ref.io_argoproj_v1alpha1_ApplicationSet_spec_matrix_pullRequest_bitbucketServer_basicAuth_passwordRef(
                    key = '0', 
                    secret_name = '0', ),
                username = '0',
        )

    def testIoArgoprojV1alpha1ApplicationSetSpecMatrixPullRequestBitbucketServerBasicAuth(self):
        """Test IoArgoprojV1alpha1ApplicationSetSpecMatrixPullRequestBitbucketServerBasicAuth"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
