# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.v2beta1_horizontal_pod_autoscaler_status import V2beta1HorizontalPodAutoscalerStatus  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV2beta1HorizontalPodAutoscalerStatus(unittest.TestCase):
    """V2beta1HorizontalPodAutoscalerStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V2beta1HorizontalPodAutoscalerStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v2beta1_horizontal_pod_autoscaler_status.V2beta1HorizontalPodAutoscalerStatus()  # noqa: E501
        if include_optional :
            return V2beta1HorizontalPodAutoscalerStatus(
                conditions = [
                    kubernetes.client.models.v2beta1/horizontal_pod_autoscaler_condition.v2beta1.HorizontalPodAutoscalerCondition(
                        last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '0', 
                        reason = '0', 
                        status = '0', 
                        type = '0', )
                    ], 
                current_metrics = [
                    kubernetes.client.models.v2beta1/metric_status.v2beta1.MetricStatus(
                        container_resource = kubernetes.client.models.v2beta1/container_resource_metric_status.v2beta1.ContainerResourceMetricStatus(
                            container = '0', 
                            current_average_utilization = 56, 
                            current_average_value = '0', 
                            name = '0', ), 
                        external = kubernetes.client.models.v2beta1/external_metric_status.v2beta1.ExternalMetricStatus(
                            current_average_value = '0', 
                            current_value = '0', 
                            metric_name = '0', 
                            metric_selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
                                match_expressions = [
                                    kubernetes.client.models.v1/label_selector_requirement.v1.LabelSelectorRequirement(
                                        key = '0', 
                                        operator = '0', 
                                        values = [
                                            '0'
                                            ], )
                                    ], 
                                match_labels = {
                                    'key' : '0'
                                    }, ), ), 
                        object = kubernetes.client.models.v2beta1/object_metric_status.v2beta1.ObjectMetricStatus(
                            average_value = '0', 
                            current_value = '0', 
                            metric_name = '0', 
                            selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(), 
                            target = kubernetes.client.models.v2beta1/cross_version_object_reference.v2beta1.CrossVersionObjectReference(
                                api_version = '0', 
                                kind = '0', 
                                name = '0', ), ), 
                        pods = kubernetes.client.models.v2beta1/pods_metric_status.v2beta1.PodsMetricStatus(
                            current_average_value = '0', 
                            metric_name = '0', ), 
                        resource = kubernetes.client.models.v2beta1/resource_metric_status.v2beta1.ResourceMetricStatus(
                            current_average_utilization = 56, 
                            current_average_value = '0', 
                            name = '0', ), 
                        type = '0', )
                    ], 
                current_replicas = 56, 
                desired_replicas = 56, 
                last_scale_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                observed_generation = 56
            )
        else :
            return V2beta1HorizontalPodAutoscalerStatus(
                conditions = [
                    kubernetes.client.models.v2beta1/horizontal_pod_autoscaler_condition.v2beta1.HorizontalPodAutoscalerCondition(
                        last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '0', 
                        reason = '0', 
                        status = '0', 
                        type = '0', )
                    ],
                current_replicas = 56,
                desired_replicas = 56,
        )

    def testV2beta1HorizontalPodAutoscalerStatus(self):
        """Test V2beta1HorizontalPodAutoscalerStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
