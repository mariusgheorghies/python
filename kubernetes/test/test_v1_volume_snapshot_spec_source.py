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
from kubernetes.client.models.v1_volume_snapshot_spec_source import V1VolumeSnapshotSpecSource  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1VolumeSnapshotSpecSource(unittest.TestCase):
    """V1VolumeSnapshotSpecSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1VolumeSnapshotSpecSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_volume_snapshot_spec_source.V1VolumeSnapshotSpecSource()  # noqa: E501
        if include_optional :
            return V1VolumeSnapshotSpecSource(
                persistent_volume_claim_name = '0', 
                volume_snapshot_content_name = '0'
            )
        else :
            return V1VolumeSnapshotSpecSource(
        )

    def testV1VolumeSnapshotSpecSource(self):
        """Test V1VolumeSnapshotSpecSource"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()