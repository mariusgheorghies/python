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
from kubernetes.client.models.aws_k8s_networking_v1alpha1_policy_endpoint import AwsK8sNetworkingV1alpha1PolicyEndpoint  # noqa: E501
from kubernetes.client.rest import ApiException

class TestAwsK8sNetworkingV1alpha1PolicyEndpoint(unittest.TestCase):
    """AwsK8sNetworkingV1alpha1PolicyEndpoint unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AwsK8sNetworkingV1alpha1PolicyEndpoint
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.aws_k8s_networking_v1alpha1_policy_endpoint.AwsK8sNetworkingV1alpha1PolicyEndpoint()  # noqa: E501
        if include_optional :
            return AwsK8sNetworkingV1alpha1PolicyEndpoint(
                api_version = '0', 
                kind = '0', 
                metadata = kubernetes.client.models.v1/object_meta.v1.ObjectMeta(
                    annotations = {
                        'key' : '0'
                        }, 
                    creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    deletion_grace_period_seconds = 56, 
                    deletion_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    finalizers = [
                        '0'
                        ], 
                    generate_name = '0', 
                    generation = 56, 
                    labels = {
                        'key' : '0'
                        }, 
                    managed_fields = [
                        kubernetes.client.models.v1/managed_fields_entry.v1.ManagedFieldsEntry(
                            api_version = '0', 
                            fields_type = '0', 
                            fields_v1 = kubernetes.client.models.fields_v1.fieldsV1(), 
                            manager = '0', 
                            operation = '0', 
                            subresource = '0', 
                            time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    name = '0', 
                    namespace = '0', 
                    owner_references = [
                        kubernetes.client.models.v1/owner_reference.v1.OwnerReference(
                            api_version = '0', 
                            block_owner_deletion = True, 
                            controller = True, 
                            kind = '0', 
                            name = '0', 
                            uid = '0', )
                        ], 
                    resource_version = '0', 
                    self_link = '0', 
                    uid = '0', ), 
                spec = kubernetes.client.models.aws_k8s_networking_v1alpha1_policy_endpoint_spec.aws_k8s_networking_v1alpha1_PolicyEndpoint_spec(
                    egress = [
                        kubernetes.client.models.aws_k8s_networking_v1alpha1_policy_endpoint_spec_egress.aws_k8s_networking_v1alpha1_PolicyEndpoint_spec_egress(
                            cidr = '0', 
                            except = [
                                '0'
                                ], 
                            ports = [
                                kubernetes.client.models.aws_k8s_networking_v1alpha1_policy_endpoint_spec_ports.aws_k8s_networking_v1alpha1_PolicyEndpoint_spec_ports(
                                    end_port = 56, 
                                    port = 56, 
                                    protocol = '0', )
                                ], )
                        ], 
                    ingress = [
                        kubernetes.client.models.aws_k8s_networking_v1alpha1_policy_endpoint_spec_egress.aws_k8s_networking_v1alpha1_PolicyEndpoint_spec_egress(
                            cidr = '0', )
                        ], 
                    pod_isolation = [
                        '0'
                        ], 
                    pod_selector = kubernetes.client.models.aws_k8s_networking_v1alpha1_policy_endpoint_spec_pod_selector.aws_k8s_networking_v1alpha1_PolicyEndpoint_spec_podSelector(
                        match_expressions = [
                            kubernetes.client.models.aws_k8s_networking_v1alpha1_policy_endpoint_spec_pod_selector_match_expressions.aws_k8s_networking_v1alpha1_PolicyEndpoint_spec_podSelector_matchExpressions(
                                key = '0', 
                                operator = '0', 
                                values = [
                                    '0'
                                    ], )
                            ], 
                        match_labels = {
                            'key' : '0'
                            }, ), 
                    pod_selector_endpoints = [
                        kubernetes.client.models.aws_k8s_networking_v1alpha1_policy_endpoint_spec_pod_selector_endpoints.aws_k8s_networking_v1alpha1_PolicyEndpoint_spec_podSelectorEndpoints(
                            host_ip = '0', 
                            name = '0', 
                            namespace = '0', 
                            pod_ip = '0', )
                        ], 
                    policy_ref = kubernetes.client.models.aws_k8s_networking_v1alpha1_policy_endpoint_spec_policy_ref.aws_k8s_networking_v1alpha1_PolicyEndpoint_spec_policyRef(
                        name = '0', 
                        namespace = '0', ), ), 
                status = None
            )
        else :
            return AwsK8sNetworkingV1alpha1PolicyEndpoint(
        )

    def testAwsK8sNetworkingV1alpha1PolicyEndpoint(self):
        """Test AwsK8sNetworkingV1alpha1PolicyEndpoint"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
