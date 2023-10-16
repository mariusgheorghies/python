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
from kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_strategy_rolling_sync_steps import IoArgoprojV1alpha1ApplicationSetSpecStrategyRollingSyncSteps  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoArgoprojV1alpha1ApplicationSetSpecStrategyRollingSyncSteps(unittest.TestCase):
    """IoArgoprojV1alpha1ApplicationSetSpecStrategyRollingSyncSteps unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoArgoprojV1alpha1ApplicationSetSpecStrategyRollingSyncSteps
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_strategy_rolling_sync_steps.IoArgoprojV1alpha1ApplicationSetSpecStrategyRollingSyncSteps()  # noqa: E501
        if include_optional :
            return IoArgoprojV1alpha1ApplicationSetSpecStrategyRollingSyncSteps(
                match_expressions = [
                    kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_strategy_rolling_sync_match_expressions.io_argoproj_v1alpha1_ApplicationSet_spec_strategy_rollingSync_matchExpressions(
                        key = '0', 
                        operator = '0', 
                        values = [
                            '0'
                            ], )
                    ], 
                max_update = kubernetes.client.models.max_update.maxUpdate()
            )
        else :
            return IoArgoprojV1alpha1ApplicationSetSpecStrategyRollingSyncSteps(
        )

    def testIoArgoprojV1alpha1ApplicationSetSpecStrategyRollingSyncSteps(self):
        """Test IoArgoprojV1alpha1ApplicationSetSpecStrategyRollingSyncSteps"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
