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
from kubernetes.client.models.v1_volume_snapshot_content_spec_volume_snapshot_ref import V1VolumeSnapshotContentSpecVolumeSnapshotRef  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1VolumeSnapshotContentSpecVolumeSnapshotRef(unittest.TestCase):
    """V1VolumeSnapshotContentSpecVolumeSnapshotRef unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1VolumeSnapshotContentSpecVolumeSnapshotRef
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_volume_snapshot_content_spec_volume_snapshot_ref.V1VolumeSnapshotContentSpecVolumeSnapshotRef()  # noqa: E501
        if include_optional :
            return V1VolumeSnapshotContentSpecVolumeSnapshotRef(
                api_version = '0', 
                field_path = '0', 
                kind = '0', 
                name = '0', 
                namespace = '0', 
                resource_version = '0', 
                uid = '0'
            )
        else :
            return V1VolumeSnapshotContentSpecVolumeSnapshotRef(
        )

    def testV1VolumeSnapshotContentSpecVolumeSnapshotRef(self):
        """Test V1VolumeSnapshotContentSpecVolumeSnapshotRef"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()