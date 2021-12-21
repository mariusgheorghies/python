# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.20.7
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.io_xk8s_cluster_controlplane_v1alpha4_kubeadm_control_plane_spec_kubeadm_config_spec import IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecKubeadmConfigSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecKubeadmConfigSpec(unittest.TestCase):
    """IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecKubeadmConfigSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecKubeadmConfigSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_xk8s_cluster_controlplane_v1alpha4_kubeadm_control_plane_spec_kubeadm_config_spec.IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecKubeadmConfigSpec()  # noqa: E501
        if include_optional :
            return IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecKubeadmConfigSpec(
                cluster_configuration = kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha4_kubeadm_config_spec_cluster_configuration.io_x_k8s_cluster_bootstrap_v1alpha4_KubeadmConfig_spec_clusterConfiguration(
                    api_server = kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha3_kubeadm_config_spec_cluster_configuration_api_server.io_x_k8s_cluster_bootstrap_v1alpha3_KubeadmConfig_spec_clusterConfiguration_apiServer(
                        cert_sa_ns = [
                            '0'
                            ], 
                        extra_args = {
                            'key' : '0'
                            }, 
                        extra_volumes = [
                            kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha3_kubeadm_config_spec_cluster_configuration_api_server_extra_volumes.io_x_k8s_cluster_bootstrap_v1alpha3_KubeadmConfig_spec_clusterConfiguration_apiServer_extraVolumes(
                                host_path = '0', 
                                mount_path = '0', 
                                name = '0', 
                                path_type = '0', 
                                read_only = True, )
                            ], 
                        timeout_for_control_plane = '0', ), 
                    api_version = '0', 
                    certificates_dir = '0', 
                    cluster_name = '0', 
                    control_plane_endpoint = '0', 
                    controller_manager = kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha3_kubeadm_config_spec_cluster_configuration_controller_manager.io_x_k8s_cluster_bootstrap_v1alpha3_KubeadmConfig_spec_clusterConfiguration_controllerManager(), 
                    dns = kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha4_kubeadm_config_spec_cluster_configuration_dns.io_x_k8s_cluster_bootstrap_v1alpha4_KubeadmConfig_spec_clusterConfiguration_dns(
                        image_repository = '0', 
                        image_tag = '0', ), 
                    etcd = kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha3_kubeadm_config_spec_cluster_configuration_etcd.io_x_k8s_cluster_bootstrap_v1alpha3_KubeadmConfig_spec_clusterConfiguration_etcd(
                        external = kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha3_kubeadm_config_spec_cluster_configuration_etcd_external.io_x_k8s_cluster_bootstrap_v1alpha3_KubeadmConfig_spec_clusterConfiguration_etcd_external(
                            ca_file = '0', 
                            cert_file = '0', 
                            endpoints = [
                                '0'
                                ], 
                            key_file = '0', ), 
                        local = kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha3_kubeadm_config_spec_cluster_configuration_etcd_local.io_x_k8s_cluster_bootstrap_v1alpha3_KubeadmConfig_spec_clusterConfiguration_etcd_local(
                            data_dir = '0', 
                            image_repository = '0', 
                            image_tag = '0', 
                            peer_cert_sa_ns = [
                                '0'
                                ], 
                            server_cert_sa_ns = [
                                '0'
                                ], ), ), 
                    feature_gates = {
                        'key' : True
                        }, 
                    image_repository = '0', 
                    kind = '0', 
                    kubernetes_version = '0', 
                    networking = kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha3_kubeadm_config_spec_cluster_configuration_networking.io_x_k8s_cluster_bootstrap_v1alpha3_KubeadmConfig_spec_clusterConfiguration_networking(
                        dns_domain = '0', 
                        pod_subnet = '0', 
                        service_subnet = '0', ), 
                    scheduler = kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha3_kubeadm_config_spec_cluster_configuration_scheduler.io_x_k8s_cluster_bootstrap_v1alpha3_KubeadmConfig_spec_clusterConfiguration_scheduler(), ), 
                disk_setup = kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha3_kubeadm_config_spec_disk_setup.io_x_k8s_cluster_bootstrap_v1alpha3_KubeadmConfig_spec_diskSetup(
                    filesystems = [
                        kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha3_kubeadm_config_spec_disk_setup_filesystems.io_x_k8s_cluster_bootstrap_v1alpha3_KubeadmConfig_spec_diskSetup_filesystems(
                            device = '0', 
                            extra_opts = [
                                '0'
                                ], 
                            filesystem = '0', 
                            label = '0', 
                            overwrite = True, 
                            partition = '0', 
                            replace_fs = '0', )
                        ], 
                    partitions = [
                        kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha3_kubeadm_config_spec_disk_setup_partitions.io_x_k8s_cluster_bootstrap_v1alpha3_KubeadmConfig_spec_diskSetup_partitions(
                            device = '0', 
                            layout = True, 
                            overwrite = True, 
                            table_type = '0', )
                        ], ), 
                files = [
                    kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha3_kubeadm_config_spec_files.io_x_k8s_cluster_bootstrap_v1alpha3_KubeadmConfig_spec_files(
                        content = '0', 
                        content_from = kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha3_kubeadm_config_spec_content_from.io_x_k8s_cluster_bootstrap_v1alpha3_KubeadmConfig_spec_contentFrom(
                            secret = kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha3_kubeadm_config_spec_content_from_secret.io_x_k8s_cluster_bootstrap_v1alpha3_KubeadmConfig_spec_contentFrom_secret(
                                key = '0', 
                                name = '0', ), ), 
                        encoding = 'base64', 
                        owner = '0', 
                        path = '0', 
                        permissions = '0', )
                    ], 
                format = 'cloud-config', 
                init_configuration = kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha4_kubeadm_config_spec_init_configuration.io_x_k8s_cluster_bootstrap_v1alpha4_KubeadmConfig_spec_initConfiguration(
                    api_version = '0', 
                    bootstrap_tokens = [
                        kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha3_kubeadm_config_spec_init_configuration_bootstrap_tokens.io_x_k8s_cluster_bootstrap_v1alpha3_KubeadmConfig_spec_initConfiguration_bootstrapTokens(
                            description = '0', 
                            expires = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            groups = [
                                '0'
                                ], 
                            token = '0', 
                            ttl = '0', 
                            usages = [
                                '0'
                                ], )
                        ], 
                    kind = '0', 
                    local_api_endpoint = kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha4_kubeadm_config_spec_init_configuration_local_api_endpoint.io_x_k8s_cluster_bootstrap_v1alpha4_KubeadmConfig_spec_initConfiguration_localAPIEndpoint(
                        advertise_address = '0', 
                        bind_port = 56, ), 
                    node_registration = kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha4_kubeadm_config_spec_init_configuration_node_registration.io_x_k8s_cluster_bootstrap_v1alpha4_KubeadmConfig_spec_initConfiguration_nodeRegistration(
                        cri_socket = '0', 
                        ignore_preflight_errors = [
                            '0'
                            ], 
                        kubelet_extra_args = {
                            'key' : '0'
                            }, 
                        name = '0', 
                        taints = [
                            kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha3_kubeadm_config_spec_init_configuration_node_registration_taints.io_x_k8s_cluster_bootstrap_v1alpha3_KubeadmConfig_spec_initConfiguration_nodeRegistration_taints(
                                effect = '0', 
                                key = '0', 
                                time_added = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                value = '0', )
                            ], ), ), 
                join_configuration = kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha4_kubeadm_config_spec_join_configuration.io_x_k8s_cluster_bootstrap_v1alpha4_KubeadmConfig_spec_joinConfiguration(
                    api_version = '0', 
                    ca_cert_path = '0', 
                    control_plane = kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha4_kubeadm_config_spec_join_configuration_control_plane.io_x_k8s_cluster_bootstrap_v1alpha4_KubeadmConfig_spec_joinConfiguration_controlPlane(
                        local_api_endpoint = kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha4_kubeadm_config_spec_join_configuration_control_plane_local_api_endpoint.io_x_k8s_cluster_bootstrap_v1alpha4_KubeadmConfig_spec_joinConfiguration_controlPlane_localAPIEndpoint(
                            advertise_address = '0', 
                            bind_port = 56, ), ), 
                    discovery = kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha4_kubeadm_config_spec_join_configuration_discovery.io_x_k8s_cluster_bootstrap_v1alpha4_KubeadmConfig_spec_joinConfiguration_discovery(
                        bootstrap_token = kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha4_kubeadm_config_spec_join_configuration_discovery_bootstrap_token.io_x_k8s_cluster_bootstrap_v1alpha4_KubeadmConfig_spec_joinConfiguration_discovery_bootstrapToken(
                            api_server_endpoint = '0', 
                            ca_cert_hashes = [
                                '0'
                                ], 
                            token = '0', 
                            unsafe_skip_ca_verification = True, ), 
                        file = kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha3_kubeadm_config_spec_join_configuration_discovery_file.io_x_k8s_cluster_bootstrap_v1alpha3_KubeadmConfig_spec_joinConfiguration_discovery_file(
                            kube_config_path = '0', ), 
                        timeout = '0', 
                        tls_bootstrap_token = '0', ), 
                    kind = '0', 
                    node_registration = kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha4_kubeadm_config_spec_init_configuration_node_registration.io_x_k8s_cluster_bootstrap_v1alpha4_KubeadmConfig_spec_initConfiguration_nodeRegistration(
                        cri_socket = '0', 
                        ignore_preflight_errors = [
                            '0'
                            ], 
                        kubelet_extra_args = {
                            'key' : '0'
                            }, 
                        name = '0', 
                        taints = [
                            kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha3_kubeadm_config_spec_init_configuration_node_registration_taints.io_x_k8s_cluster_bootstrap_v1alpha3_KubeadmConfig_spec_initConfiguration_nodeRegistration_taints(
                                effect = '0', 
                                key = '0', 
                                time_added = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                value = '0', )
                            ], ), ), 
                mounts = [
                    [
                        '0'
                        ]
                    ], 
                ntp = kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha3_kubeadm_config_spec_ntp.io_x_k8s_cluster_bootstrap_v1alpha3_KubeadmConfig_spec_ntp(
                    enabled = True, 
                    servers = [
                        '0'
                        ], ), 
                post_kubeadm_commands = [
                    '0'
                    ], 
                pre_kubeadm_commands = [
                    '0'
                    ], 
                use_experimental_retry_join = True, 
                users = [
                    kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha3_kubeadm_config_spec_users.io_x_k8s_cluster_bootstrap_v1alpha3_KubeadmConfig_spec_users(
                        gecos = '0', 
                        groups = '0', 
                        home_dir = '0', 
                        inactive = True, 
                        lock_password = True, 
                        name = '0', 
                        passwd = '0', 
                        primary_group = '0', 
                        shell = '0', 
                        ssh_authorized_keys = [
                            '0'
                            ], 
                        sudo = '0', )
                    ], 
                verbosity = 56
            )
        else :
            return IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecKubeadmConfigSpec(
        )

    def testIoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecKubeadmConfigSpec(self):
        """Test IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecKubeadmConfigSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
