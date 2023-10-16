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
from kubernetes.client.models.io_external_secrets_v1beta1_external_secret_spec import IoExternalSecretsV1beta1ExternalSecretSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoExternalSecretsV1beta1ExternalSecretSpec(unittest.TestCase):
    """IoExternalSecretsV1beta1ExternalSecretSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoExternalSecretsV1beta1ExternalSecretSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_external_secrets_v1beta1_external_secret_spec.IoExternalSecretsV1beta1ExternalSecretSpec()  # noqa: E501
        if include_optional :
            return IoExternalSecretsV1beta1ExternalSecretSpec(
                data = [
                    kubernetes.client.models.io_external_secrets_v1beta1_cluster_external_secret_spec_external_secret_spec_data.io_external_secrets_v1beta1_ClusterExternalSecret_spec_externalSecretSpec_data(
                        remote_ref = kubernetes.client.models.io_external_secrets_v1beta1_cluster_external_secret_spec_external_secret_spec_remote_ref.io_external_secrets_v1beta1_ClusterExternalSecret_spec_externalSecretSpec_remoteRef(
                            conversion_strategy = '0', 
                            decoding_strategy = '0', 
                            key = '0', 
                            metadata_policy = '0', 
                            property = '0', 
                            version = '0', ), 
                        secret_key = '0', 
                        source_ref = kubernetes.client.models.io_external_secrets_v1beta1_cluster_external_secret_spec_external_secret_spec_source_ref.io_external_secrets_v1beta1_ClusterExternalSecret_spec_externalSecretSpec_sourceRef(
                            generator_ref = kubernetes.client.models.io_external_secrets_v1beta1_cluster_external_secret_spec_external_secret_spec_source_ref_generator_ref.io_external_secrets_v1beta1_ClusterExternalSecret_spec_externalSecretSpec_sourceRef_generatorRef(
                                api_version = '0', 
                                kind = '0', 
                                name = '0', ), 
                            store_ref = kubernetes.client.models.io_external_secrets_v1alpha1_external_secret_spec_secret_store_ref.io_external_secrets_v1alpha1_ExternalSecret_spec_secretStoreRef(
                                kind = '0', 
                                name = '0', ), ), )
                    ], 
                data_from = [
                    kubernetes.client.models.io_external_secrets_v1beta1_cluster_external_secret_spec_external_secret_spec_data_from.io_external_secrets_v1beta1_ClusterExternalSecret_spec_externalSecretSpec_dataFrom(
                        extract = kubernetes.client.models.io_external_secrets_v1beta1_cluster_external_secret_spec_external_secret_spec_extract.io_external_secrets_v1beta1_ClusterExternalSecret_spec_externalSecretSpec_extract(
                            conversion_strategy = '0', 
                            decoding_strategy = '0', 
                            key = '0', 
                            metadata_policy = '0', 
                            property = '0', 
                            version = '0', ), 
                        find = kubernetes.client.models.io_external_secrets_v1beta1_cluster_external_secret_spec_external_secret_spec_find.io_external_secrets_v1beta1_ClusterExternalSecret_spec_externalSecretSpec_find(
                            conversion_strategy = '0', 
                            decoding_strategy = '0', 
                            name = kubernetes.client.models.io_external_secrets_v1beta1_cluster_external_secret_spec_external_secret_spec_find_name.io_external_secrets_v1beta1_ClusterExternalSecret_spec_externalSecretSpec_find_name(
                                regexp = '0', ), 
                            path = '0', 
                            tags = {
                                'key' : '0'
                                }, ), 
                        rewrite = [
                            kubernetes.client.models.io_external_secrets_v1beta1_cluster_external_secret_spec_external_secret_spec_rewrite.io_external_secrets_v1beta1_ClusterExternalSecret_spec_externalSecretSpec_rewrite(
                                regexp = kubernetes.client.models.io_external_secrets_v1beta1_cluster_external_secret_spec_external_secret_spec_regexp.io_external_secrets_v1beta1_ClusterExternalSecret_spec_externalSecretSpec_regexp(
                                    source = '0', 
                                    target = '0', ), )
                            ], 
                        source_ref = kubernetes.client.models.io_external_secrets_v1beta1_cluster_external_secret_spec_external_secret_spec_source_ref_1.io_external_secrets_v1beta1_ClusterExternalSecret_spec_externalSecretSpec_sourceRef_1(
                            generator_ref = kubernetes.client.models.io_external_secrets_v1beta1_cluster_external_secret_spec_external_secret_spec_source_ref_generator_ref.io_external_secrets_v1beta1_ClusterExternalSecret_spec_externalSecretSpec_sourceRef_generatorRef(
                                api_version = '0', 
                                kind = '0', 
                                name = '0', ), 
                            store_ref = kubernetes.client.models.io_external_secrets_v1alpha1_external_secret_spec_secret_store_ref.io_external_secrets_v1alpha1_ExternalSecret_spec_secretStoreRef(
                                kind = '0', 
                                name = '0', ), ), )
                    ], 
                refresh_interval = '0', 
                secret_store_ref = kubernetes.client.models.io_external_secrets_v1alpha1_external_secret_spec_secret_store_ref.io_external_secrets_v1alpha1_ExternalSecret_spec_secretStoreRef(
                    kind = '0', 
                    name = '0', ), 
                target = kubernetes.client.models.io_external_secrets_v1beta1_cluster_external_secret_spec_external_secret_spec_target.io_external_secrets_v1beta1_ClusterExternalSecret_spec_externalSecretSpec_target(
                    creation_policy = 'Owner', 
                    deletion_policy = 'Delete', 
                    immutable = True, 
                    name = '0', 
                    template = kubernetes.client.models.io_external_secrets_v1beta1_cluster_external_secret_spec_external_secret_spec_target_template.io_external_secrets_v1beta1_ClusterExternalSecret_spec_externalSecretSpec_target_template(
                        data = {
                            'key' : '0'
                            }, 
                        engine_version = '0', 
                        metadata = kubernetes.client.models.io_external_secrets_v1alpha1_external_secret_spec_target_template_metadata.io_external_secrets_v1alpha1_ExternalSecret_spec_target_template_metadata(
                            annotations = {
                                'key' : '0'
                                }, 
                            labels = {
                                'key' : '0'
                                }, ), 
                        template_from = [
                            kubernetes.client.models.io_external_secrets_v1beta1_cluster_external_secret_spec_external_secret_spec_target_template_template_from.io_external_secrets_v1beta1_ClusterExternalSecret_spec_externalSecretSpec_target_template_templateFrom(
                                config_map = kubernetes.client.models.io_external_secrets_v1beta1_cluster_external_secret_spec_external_secret_spec_target_template_config_map.io_external_secrets_v1beta1_ClusterExternalSecret_spec_externalSecretSpec_target_template_configMap(
                                    items = [
                                        kubernetes.client.models.io_external_secrets_v1beta1_cluster_external_secret_spec_external_secret_spec_target_template_config_map_items.io_external_secrets_v1beta1_ClusterExternalSecret_spec_externalSecretSpec_target_template_configMap_items(
                                            key = '0', 
                                            template_as = '0', )
                                        ], 
                                    name = '0', ), 
                                literal = '0', 
                                secret = kubernetes.client.models.io_external_secrets_v1beta1_cluster_external_secret_spec_external_secret_spec_target_template_config_map.io_external_secrets_v1beta1_ClusterExternalSecret_spec_externalSecretSpec_target_template_configMap(
                                    items = [
                                        kubernetes.client.models.io_external_secrets_v1beta1_cluster_external_secret_spec_external_secret_spec_target_template_config_map_items.io_external_secrets_v1beta1_ClusterExternalSecret_spec_externalSecretSpec_target_template_configMap_items(
                                            key = '0', 
                                            template_as = '0', )
                                        ], 
                                    name = '0', ), )
                            ], 
                        type = '0', ), )
            )
        else :
            return IoExternalSecretsV1beta1ExternalSecretSpec(
        )

    def testIoExternalSecretsV1beta1ExternalSecretSpec(self):
        """Test IoExternalSecretsV1beta1ExternalSecretSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
