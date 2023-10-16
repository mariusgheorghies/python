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
from kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_git import IoArgoprojV1alpha1ApplicationSetSpecGit  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoArgoprojV1alpha1ApplicationSetSpecGit(unittest.TestCase):
    """IoArgoprojV1alpha1ApplicationSetSpecGit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoArgoprojV1alpha1ApplicationSetSpecGit
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_git.IoArgoprojV1alpha1ApplicationSetSpecGit()  # noqa: E501
        if include_optional :
            return IoArgoprojV1alpha1ApplicationSetSpecGit(
                directories = [
                    kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_git_directories.io_argoproj_v1alpha1_ApplicationSet_spec_git_directories(
                        exclude = True, 
                        path = '0', )
                    ], 
                files = [
                    kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_git_files.io_argoproj_v1alpha1_ApplicationSet_spec_git_files(
                        path = '0', )
                    ], 
                path_param_prefix = '0', 
                repo_url = '0', 
                requeue_after_seconds = 56, 
                revision = '0', 
                template = kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_cluster_decision_resource_template.io_argoproj_v1alpha1_ApplicationSet_spec_clusterDecisionResource_template(
                    metadata = kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_cluster_decision_resource_template_metadata.io_argoproj_v1alpha1_ApplicationSet_spec_clusterDecisionResource_template_metadata(
                        annotations = {
                            'key' : '0'
                            }, 
                        finalizers = [
                            '0'
                            ], 
                        labels = {
                            'key' : '0'
                            }, 
                        name = '0', 
                        namespace = '0', ), 
                    spec = kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_cluster_decision_resource_template_spec.io_argoproj_v1alpha1_ApplicationSet_spec_clusterDecisionResource_template_spec(
                        destination = kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_cluster_decision_resource_template_spec_destination.io_argoproj_v1alpha1_ApplicationSet_spec_clusterDecisionResource_template_spec_destination(
                            name = '0', 
                            namespace = '0', 
                            server = '0', ), 
                        ignore_differences = [
                            kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_cluster_decision_resource_template_spec_ignore_differences.io_argoproj_v1alpha1_ApplicationSet_spec_clusterDecisionResource_template_spec_ignoreDifferences(
                                group = '0', 
                                jq_path_expressions = [
                                    '0'
                                    ], 
                                json_pointers = [
                                    '0'
                                    ], 
                                kind = '0', 
                                managed_fields_managers = [
                                    '0'
                                    ], 
                                name = '0', 
                                namespace = '0', )
                            ], 
                        info = [
                            kubernetes.client.models.io_argoproj_v1alpha1_application_operation_info.io_argoproj_v1alpha1_Application_operation_info(
                                name = '0', 
                                value = '0', )
                            ], 
                        project = '0', 
                        revision_history_limit = 56, 
                        source = kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_cluster_decision_resource_template_spec_source.io_argoproj_v1alpha1_ApplicationSet_spec_clusterDecisionResource_template_spec_source(
                            chart = '0', 
                            directory = kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_cluster_decision_resource_template_spec_source_directory.io_argoproj_v1alpha1_ApplicationSet_spec_clusterDecisionResource_template_spec_source_directory(
                                exclude = '0', 
                                include = '0', 
                                jsonnet = kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_cluster_decision_resource_template_spec_source_directory_jsonnet.io_argoproj_v1alpha1_ApplicationSet_spec_clusterDecisionResource_template_spec_source_directory_jsonnet(
                                    ext_vars = [
                                        kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_cluster_decision_resource_template_spec_source_directory_jsonnet_ext_vars.io_argoproj_v1alpha1_ApplicationSet_spec_clusterDecisionResource_template_spec_source_directory_jsonnet_extVars(
                                            code = True, 
                                            name = '0', 
                                            value = '0', )
                                        ], 
                                    libs = [
                                        '0'
                                        ], 
                                    tlas = [
                                        kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_cluster_decision_resource_template_spec_source_directory_jsonnet_ext_vars.io_argoproj_v1alpha1_ApplicationSet_spec_clusterDecisionResource_template_spec_source_directory_jsonnet_extVars(
                                            code = True, 
                                            name = '0', 
                                            value = '0', )
                                        ], ), 
                                recurse = True, ), 
                            helm = kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_cluster_decision_resource_template_spec_source_helm.io_argoproj_v1alpha1_ApplicationSet_spec_clusterDecisionResource_template_spec_source_helm(
                                file_parameters = [
                                    kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_cluster_decision_resource_template_spec_source_helm_file_parameters.io_argoproj_v1alpha1_ApplicationSet_spec_clusterDecisionResource_template_spec_source_helm_fileParameters(
                                        name = '0', 
                                        path = '0', )
                                    ], 
                                ignore_missing_value_files = True, 
                                parameters = [
                                    kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_cluster_decision_resource_template_spec_source_helm_parameters.io_argoproj_v1alpha1_ApplicationSet_spec_clusterDecisionResource_template_spec_source_helm_parameters(
                                        force_string = True, 
                                        name = '0', 
                                        value = '0', )
                                    ], 
                                pass_credentials = True, 
                                release_name = '0', 
                                skip_crds = True, 
                                value_files = [
                                    '0'
                                    ], 
                                values = '0', 
                                version = '0', ), 
                            kustomize = kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_cluster_decision_resource_template_spec_source_kustomize.io_argoproj_v1alpha1_ApplicationSet_spec_clusterDecisionResource_template_spec_source_kustomize(
                                common_annotations = {
                                    'key' : '0'
                                    }, 
                                common_annotations_envsubst = True, 
                                common_labels = {
                                    'key' : '0'
                                    }, 
                                force_common_annotations = True, 
                                force_common_labels = True, 
                                images = [
                                    '0'
                                    ], 
                                name_prefix = '0', 
                                name_suffix = '0', 
                                namespace = '0', 
                                replicas = [
                                    kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_cluster_decision_resource_template_spec_source_kustomize_replicas.io_argoproj_v1alpha1_ApplicationSet_spec_clusterDecisionResource_template_spec_source_kustomize_replicas(
                                        count = kubernetes.client.models.count.count(), 
                                        name = '0', )
                                    ], 
                                version = '0', ), 
                            path = '0', 
                            plugin = kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_cluster_decision_resource_template_spec_source_plugin.io_argoproj_v1alpha1_ApplicationSet_spec_clusterDecisionResource_template_spec_source_plugin(
                                env = [
                                    kubernetes.client.models.io_argoproj_v1alpha1_application_operation_info.io_argoproj_v1alpha1_Application_operation_info(
                                        name = '0', 
                                        value = '0', )
                                    ], 
                                name = '0', ), 
                            ref = '0', 
                            repo_url = '0', 
                            target_revision = '0', ), 
                        sources = [
                            kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_cluster_decision_resource_template_spec_source.io_argoproj_v1alpha1_ApplicationSet_spec_clusterDecisionResource_template_spec_source(
                                chart = '0', 
                                path = '0', 
                                ref = '0', 
                                repo_url = '0', 
                                target_revision = '0', )
                            ], 
                        sync_policy = kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_cluster_decision_resource_template_spec_sync_policy.io_argoproj_v1alpha1_ApplicationSet_spec_clusterDecisionResource_template_spec_syncPolicy(
                            automated = kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_cluster_decision_resource_template_spec_sync_policy_automated.io_argoproj_v1alpha1_ApplicationSet_spec_clusterDecisionResource_template_spec_syncPolicy_automated(
                                allow_empty = True, 
                                prune = True, 
                                self_heal = True, ), 
                            managed_namespace_metadata = kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_cluster_decision_resource_template_spec_sync_policy_managed_namespace_metadata.io_argoproj_v1alpha1_ApplicationSet_spec_clusterDecisionResource_template_spec_syncPolicy_managedNamespaceMetadata(), 
                            retry = kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_cluster_decision_resource_template_spec_sync_policy_retry.io_argoproj_v1alpha1_ApplicationSet_spec_clusterDecisionResource_template_spec_syncPolicy_retry(
                                backoff = kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_cluster_decision_resource_template_spec_sync_policy_retry_backoff.io_argoproj_v1alpha1_ApplicationSet_spec_clusterDecisionResource_template_spec_syncPolicy_retry_backoff(
                                    duration = '0', 
                                    factor = 56, 
                                    max_duration = '0', ), 
                                limit = 56, ), 
                            sync_options = [
                                '0'
                                ], ), ), )
            )
        else :
            return IoArgoprojV1alpha1ApplicationSetSpecGit(
                repo_url = '0',
                revision = '0',
        )

    def testIoArgoprojV1alpha1ApplicationSetSpecGit(self):
        """Test IoArgoprojV1alpha1ApplicationSetSpecGit"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
