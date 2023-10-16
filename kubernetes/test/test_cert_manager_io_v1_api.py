# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.25.12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import kubernetes.client
from kubernetes.client.api.cert_manager_io_v1_api import CertManagerIoV1Api  # noqa: E501
from kubernetes.client.rest import ApiException


class TestCertManagerIoV1Api(unittest.TestCase):
    """CertManagerIoV1Api unit test stubs"""

    def setUp(self):
        self.api = kubernetes.client.api.cert_manager_io_v1_api.CertManagerIoV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_cluster_issuer(self):
        """Test case for create_cluster_issuer

        """
        pass

    def test_create_namespaced_certificate(self):
        """Test case for create_namespaced_certificate

        """
        pass

    def test_create_namespaced_certificate_request(self):
        """Test case for create_namespaced_certificate_request

        """
        pass

    def test_create_namespaced_issuer(self):
        """Test case for create_namespaced_issuer

        """
        pass

    def test_delete_cluster_issuer(self):
        """Test case for delete_cluster_issuer

        """
        pass

    def test_delete_collection_cluster_issuer(self):
        """Test case for delete_collection_cluster_issuer

        """
        pass

    def test_delete_collection_namespaced_certificate(self):
        """Test case for delete_collection_namespaced_certificate

        """
        pass

    def test_delete_collection_namespaced_certificate_request(self):
        """Test case for delete_collection_namespaced_certificate_request

        """
        pass

    def test_delete_collection_namespaced_issuer(self):
        """Test case for delete_collection_namespaced_issuer

        """
        pass

    def test_delete_namespaced_certificate(self):
        """Test case for delete_namespaced_certificate

        """
        pass

    def test_delete_namespaced_certificate_request(self):
        """Test case for delete_namespaced_certificate_request

        """
        pass

    def test_delete_namespaced_issuer(self):
        """Test case for delete_namespaced_issuer

        """
        pass

    def test_list_certificate_for_all_namespaces(self):
        """Test case for list_certificate_for_all_namespaces

        """
        pass

    def test_list_certificate_request_for_all_namespaces(self):
        """Test case for list_certificate_request_for_all_namespaces

        """
        pass

    def test_list_cluster_issuer(self):
        """Test case for list_cluster_issuer

        """
        pass

    def test_list_issuer_for_all_namespaces(self):
        """Test case for list_issuer_for_all_namespaces

        """
        pass

    def test_list_namespaced_certificate(self):
        """Test case for list_namespaced_certificate

        """
        pass

    def test_list_namespaced_certificate_request(self):
        """Test case for list_namespaced_certificate_request

        """
        pass

    def test_list_namespaced_issuer(self):
        """Test case for list_namespaced_issuer

        """
        pass

    def test_patch_cluster_issuer(self):
        """Test case for patch_cluster_issuer

        """
        pass

    def test_patch_cluster_issuer_status(self):
        """Test case for patch_cluster_issuer_status

        """
        pass

    def test_patch_namespaced_certificate(self):
        """Test case for patch_namespaced_certificate

        """
        pass

    def test_patch_namespaced_certificate_request(self):
        """Test case for patch_namespaced_certificate_request

        """
        pass

    def test_patch_namespaced_certificate_request_status(self):
        """Test case for patch_namespaced_certificate_request_status

        """
        pass

    def test_patch_namespaced_certificate_status(self):
        """Test case for patch_namespaced_certificate_status

        """
        pass

    def test_patch_namespaced_issuer(self):
        """Test case for patch_namespaced_issuer

        """
        pass

    def test_patch_namespaced_issuer_status(self):
        """Test case for patch_namespaced_issuer_status

        """
        pass

    def test_read_cluster_issuer(self):
        """Test case for read_cluster_issuer

        """
        pass

    def test_read_cluster_issuer_status(self):
        """Test case for read_cluster_issuer_status

        """
        pass

    def test_read_namespaced_certificate(self):
        """Test case for read_namespaced_certificate

        """
        pass

    def test_read_namespaced_certificate_request(self):
        """Test case for read_namespaced_certificate_request

        """
        pass

    def test_read_namespaced_certificate_request_status(self):
        """Test case for read_namespaced_certificate_request_status

        """
        pass

    def test_read_namespaced_certificate_status(self):
        """Test case for read_namespaced_certificate_status

        """
        pass

    def test_read_namespaced_issuer(self):
        """Test case for read_namespaced_issuer

        """
        pass

    def test_read_namespaced_issuer_status(self):
        """Test case for read_namespaced_issuer_status

        """
        pass

    def test_replace_cluster_issuer(self):
        """Test case for replace_cluster_issuer

        """
        pass

    def test_replace_cluster_issuer_status(self):
        """Test case for replace_cluster_issuer_status

        """
        pass

    def test_replace_namespaced_certificate(self):
        """Test case for replace_namespaced_certificate

        """
        pass

    def test_replace_namespaced_certificate_request(self):
        """Test case for replace_namespaced_certificate_request

        """
        pass

    def test_replace_namespaced_certificate_request_status(self):
        """Test case for replace_namespaced_certificate_request_status

        """
        pass

    def test_replace_namespaced_certificate_status(self):
        """Test case for replace_namespaced_certificate_status

        """
        pass

    def test_replace_namespaced_issuer(self):
        """Test case for replace_namespaced_issuer

        """
        pass

    def test_replace_namespaced_issuer_status(self):
        """Test case for replace_namespaced_issuer_status

        """
        pass


if __name__ == '__main__':
    unittest.main()