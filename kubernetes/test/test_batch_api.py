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
from kubernetes.client.api.batch_api import BatchApi  # noqa: E501
from kubernetes.client.rest import ApiException


class TestBatchApi(unittest.TestCase):
    """BatchApi unit test stubs"""

    def setUp(self):
        self.api = kubernetes.client.api.batch_api.BatchApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_api_group(self):
        """Test case for get_api_group

        """
        pass


if __name__ == '__main__':
    unittest.main()
