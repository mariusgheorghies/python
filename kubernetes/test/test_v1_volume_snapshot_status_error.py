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
from kubernetes.client.models.v1_volume_snapshot_status_error import V1VolumeSnapshotStatusError  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1VolumeSnapshotStatusError(unittest.TestCase):
    """V1VolumeSnapshotStatusError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1VolumeSnapshotStatusError
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_volume_snapshot_status_error.V1VolumeSnapshotStatusError()  # noqa: E501
        if include_optional :
            return V1VolumeSnapshotStatusError(
                message = '0', 
                time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return V1VolumeSnapshotStatusError(
        )

    def testV1VolumeSnapshotStatusError(self):
        """Test V1VolumeSnapshotStatusError"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()