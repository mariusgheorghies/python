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
from kubernetes.client.models.v1_status import V1Status  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1Status(unittest.TestCase):
    """V1Status unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1Status
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_status.V1Status()  # noqa: E501
        if include_optional :
            return V1Status(
                api_version = '0', 
                code = 56, 
                details = kubernetes.client.models.v1/status_details.v1.StatusDetails(
                    causes = [
                        kubernetes.client.models.v1/status_cause.v1.StatusCause(
                            field = '0', 
                            message = '0', 
                            reason = '0', )
                        ], 
                    group = '0', 
                    kind = '0', 
                    name = '0', 
                    retry_after_seconds = 56, 
                    uid = '0', ), 
                kind = '0', 
                message = '0', 
                metadata = kubernetes.client.models.v1/list_meta.v1.ListMeta(
                    continue = '0', 
                    remaining_item_count = 56, 
                    resource_version = '0', 
                    self_link = '0', ), 
                reason = '0', 
                status = '0'
            )
        else :
            return V1Status(
        )

    def testV1Status(self):
        """Test V1Status"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
