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
from kubernetes.client.models.io_argoproj_v1alpha1_application_operation_sync_sources import IoArgoprojV1alpha1ApplicationOperationSyncSources  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoArgoprojV1alpha1ApplicationOperationSyncSources(unittest.TestCase):
    """IoArgoprojV1alpha1ApplicationOperationSyncSources unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoArgoprojV1alpha1ApplicationOperationSyncSources
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_argoproj_v1alpha1_application_operation_sync_sources.IoArgoprojV1alpha1ApplicationOperationSyncSources()  # noqa: E501
        if include_optional :
            return IoArgoprojV1alpha1ApplicationOperationSyncSources(
                chart = '0', 
                directory = kubernetes.client.models.io_argoproj_v1alpha1_application_operation_sync_source_directory.io_argoproj_v1alpha1_Application_operation_sync_source_directory(
                    exclude = '0', 
                    include = '0', 
                    jsonnet = kubernetes.client.models.io_argoproj_v1alpha1_application_operation_sync_source_directory_jsonnet.io_argoproj_v1alpha1_Application_operation_sync_source_directory_jsonnet(
                        ext_vars = [
                            kubernetes.client.models.io_argoproj_v1alpha1_application_operation_sync_source_directory_jsonnet_ext_vars.io_argoproj_v1alpha1_Application_operation_sync_source_directory_jsonnet_extVars(
                                code = True, 
                                name = '0', 
                                value = '0', )
                            ], 
                        libs = [
                            '0'
                            ], 
                        tlas = [
                            kubernetes.client.models.io_argoproj_v1alpha1_application_operation_sync_source_directory_jsonnet_ext_vars.io_argoproj_v1alpha1_Application_operation_sync_source_directory_jsonnet_extVars(
                                code = True, 
                                name = '0', 
                                value = '0', )
                            ], ), 
                    recurse = True, ), 
                helm = kubernetes.client.models.io_argoproj_v1alpha1_application_operation_sync_source_helm.io_argoproj_v1alpha1_Application_operation_sync_source_helm(
                    file_parameters = [
                        kubernetes.client.models.io_argoproj_v1alpha1_application_operation_sync_source_helm_file_parameters.io_argoproj_v1alpha1_Application_operation_sync_source_helm_fileParameters(
                            name = '0', 
                            path = '0', )
                        ], 
                    ignore_missing_value_files = True, 
                    parameters = [
                        kubernetes.client.models.io_argoproj_v1alpha1_application_operation_sync_source_helm_parameters.io_argoproj_v1alpha1_Application_operation_sync_source_helm_parameters(
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
                kustomize = kubernetes.client.models.io_argoproj_v1alpha1_application_operation_sync_source_kustomize.io_argoproj_v1alpha1_Application_operation_sync_source_kustomize(
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
                        kubernetes.client.models.io_argoproj_v1alpha1_application_operation_sync_source_kustomize_replicas.io_argoproj_v1alpha1_Application_operation_sync_source_kustomize_replicas(
                            count = kubernetes.client.models.count.count(), 
                            name = '0', )
                        ], 
                    version = '0', ), 
                path = '0', 
                plugin = kubernetes.client.models.io_argoproj_v1alpha1_application_operation_sync_source_plugin.io_argoproj_v1alpha1_Application_operation_sync_source_plugin(
                    env = [
                        kubernetes.client.models.io_argoproj_v1alpha1_application_operation_sync_source_plugin_env.io_argoproj_v1alpha1_Application_operation_sync_source_plugin_env(
                            name = '0', 
                            value = '0', )
                        ], 
                    name = '0', 
                    parameters = [
                        kubernetes.client.models.io_argoproj_v1alpha1_application_operation_sync_source_plugin_parameters.io_argoproj_v1alpha1_Application_operation_sync_source_plugin_parameters(
                            array = [
                                '0'
                                ], 
                            map = {
                                'key' : '0'
                                }, 
                            name = '0', 
                            string = '0', )
                        ], ), 
                ref = '0', 
                repo_url = '0', 
                target_revision = '0'
            )
        else :
            return IoArgoprojV1alpha1ApplicationOperationSyncSources(
                repo_url = '0',
        )

    def testIoArgoprojV1alpha1ApplicationOperationSyncSources(self):
        """Test IoArgoprojV1alpha1ApplicationOperationSyncSources"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
