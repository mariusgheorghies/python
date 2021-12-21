# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.20.7
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import kubernetes.client
from kubernetes.client.api.certificates_v1beta1_api import CertificatesV1beta1Api  # noqa: E501
from kubernetes.client.rest import ApiException


class TestCertificatesV1beta1Api(unittest.TestCase):
    """CertificatesV1beta1Api unit test stubs"""

    def setUp(self):
        self.api = kubernetes.client.api.certificates_v1beta1_api.CertificatesV1beta1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_certificate_signing_request(self):
        """Test case for create_certificate_signing_request

        """
        pass

    def test_delete_certificate_signing_request(self):
        """Test case for delete_certificate_signing_request

        """
        pass

    def test_delete_collection_certificate_signing_request(self):
        """Test case for delete_collection_certificate_signing_request

        """
        pass

    def test_get_api_resources(self):
        """Test case for get_api_resources

        """
        pass

    def test_list_certificate_signing_request(self):
        """Test case for list_certificate_signing_request

        """
        pass

    def test_patch_certificate_signing_request(self):
        """Test case for patch_certificate_signing_request

        """
        pass

    def test_patch_certificate_signing_request_approval(self):
        """Test case for patch_certificate_signing_request_approval

        """
        pass

    def test_patch_certificate_signing_request_status(self):
        """Test case for patch_certificate_signing_request_status

        """
        pass

    def test_read_certificate_signing_request(self):
        """Test case for read_certificate_signing_request

        """
        pass

    def test_read_certificate_signing_request_approval(self):
        """Test case for read_certificate_signing_request_approval

        """
        pass

    def test_read_certificate_signing_request_status(self):
        """Test case for read_certificate_signing_request_status

        """
        pass

    def test_replace_certificate_signing_request(self):
        """Test case for replace_certificate_signing_request

        """
        pass

    def test_replace_certificate_signing_request_approval(self):
        """Test case for replace_certificate_signing_request_approval

        """
        pass

    def test_replace_certificate_signing_request_status(self):
        """Test case for replace_certificate_signing_request_status

        """
        pass


if __name__ == '__main__':
    unittest.main()
