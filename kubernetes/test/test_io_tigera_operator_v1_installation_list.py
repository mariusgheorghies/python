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
from kubernetes.client.models.io_tigera_operator_v1_installation_list import IoTigeraOperatorV1InstallationList  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoTigeraOperatorV1InstallationList(unittest.TestCase):
    """IoTigeraOperatorV1InstallationList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoTigeraOperatorV1InstallationList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_tigera_operator_v1_installation_list.IoTigeraOperatorV1InstallationList()  # noqa: E501
        if include_optional :
            return IoTigeraOperatorV1InstallationList(
                api_version = '0', 
                items = [
                    kubernetes.client.models.io/tigera/operator/v1/installation.io.tigera.operator.v1.Installation(
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
                        spec = kubernetes.client.models.io_tigera_operator_v1_installation_spec.io_tigera_operator_v1_Installation_spec(
                            calico_network = kubernetes.client.models.io_tigera_operator_v1_installation_spec_calico_network.io_tigera_operator_v1_Installation_spec_calicoNetwork(
                                bgp = 'Enabled', 
                                container_ip_forwarding = 'Enabled', 
                                host_ports = 'Enabled', 
                                ip_pools = [
                                    kubernetes.client.models.io_tigera_operator_v1_installation_spec_calico_network_ip_pools.io_tigera_operator_v1_Installation_spec_calicoNetwork_ipPools(
                                        block_size = 56, 
                                        cidr = '0', 
                                        encapsulation = 'IPIPCrossSubnet', 
                                        nat_outgoing = 'Enabled', 
                                        node_selector = '0', )
                                    ], 
                                linux_dataplane = 'Iptables', 
                                mtu = 56, 
                                multi_interface_mode = 'None', 
                                node_address_autodetection_v4 = kubernetes.client.models.io_tigera_operator_v1_installation_spec_calico_network_node_address_autodetection_v4.io_tigera_operator_v1_Installation_spec_calicoNetwork_nodeAddressAutodetectionV4(
                                    can_reach = '0', 
                                    cidrs = [
                                        '0'
                                        ], 
                                    first_found = True, 
                                    interface = '0', 
                                    skip_interface = '0', ), 
                                node_address_autodetection_v6 = kubernetes.client.models.io_tigera_operator_v1_installation_spec_calico_network_node_address_autodetection_v6.io_tigera_operator_v1_Installation_spec_calicoNetwork_nodeAddressAutodetectionV6(
                                    can_reach = '0', 
                                    first_found = True, 
                                    interface = '0', 
                                    skip_interface = '0', ), ), 
                            certificate_management = kubernetes.client.models.io_tigera_operator_v1_installation_spec_certificate_management.io_tigera_operator_v1_Installation_spec_certificateManagement(
                                ca_cert = 'YQ==', 
                                key_algorithm = '', 
                                signature_algorithm = '', 
                                signer_name = '0', ), 
                            cni = kubernetes.client.models.io_tigera_operator_v1_installation_spec_cni.io_tigera_operator_v1_Installation_spec_cni(
                                ipam = kubernetes.client.models.io_tigera_operator_v1_installation_spec_cni_ipam.io_tigera_operator_v1_Installation_spec_cni_ipam(
                                    type = 'Calico', ), 
                                type = 'Calico', ), 
                            component_resources = [
                                kubernetes.client.models.io_tigera_operator_v1_installation_spec_component_resources.io_tigera_operator_v1_Installation_spec_componentResources(
                                    component_name = 'Node', 
                                    resource_requirements = kubernetes.client.models.io_tigera_operator_v1_installation_spec_resource_requirements.io_tigera_operator_v1_Installation_spec_resourceRequirements(
                                        limits = {
                                            'key' : None
                                            }, 
                                        requests = {
                                            'key' : None
                                            }, ), )
                                ], 
                            control_plane_node_selector = {
                                'key' : '0'
                                }, 
                            control_plane_tolerations = [
                                kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_tolerations.com_coreos_monitoring_v1_Alertmanager_spec_tolerations(
                                    effect = '0', 
                                    key = '0', 
                                    operator = '0', 
                                    toleration_seconds = 56, 
                                    value = '0', )
                                ], 
                            flex_volume_path = '0', 
                            image_path = '0', 
                            image_prefix = '0', 
                            image_pull_secrets = [
                                kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_image_pull_secrets.com_coreos_monitoring_v1_Alertmanager_spec_imagePullSecrets(
                                    name = '0', )
                                ], 
                            kubernetes_provider = '', 
                            node_metrics_port = 56, 
                            node_update_strategy = kubernetes.client.models.io_tigera_operator_v1_installation_spec_node_update_strategy.io_tigera_operator_v1_Installation_spec_nodeUpdateStrategy(
                                rolling_update = kubernetes.client.models.io_tigera_operator_v1_installation_spec_node_update_strategy_rolling_update.io_tigera_operator_v1_Installation_spec_nodeUpdateStrategy_rollingUpdate(
                                    max_unavailable = kubernetes.client.models.max_unavailable.maxUnavailable(), ), 
                                type = '0', ), 
                            registry = '0', 
                            typha_affinity = kubernetes.client.models.io_tigera_operator_v1_installation_spec_typha_affinity.io_tigera_operator_v1_Installation_spec_typhaAffinity(
                                node_affinity = kubernetes.client.models.io_tigera_operator_v1_installation_spec_typha_affinity_node_affinity.io_tigera_operator_v1_Installation_spec_typhaAffinity_nodeAffinity(
                                    preferred_during_scheduling_ignored_during_execution = [
                                        kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_node_affinity_preferred_during_scheduling_ignored_during_execution.com_coreos_monitoring_v1_Alertmanager_spec_affinity_nodeAffinity_preferredDuringSchedulingIgnoredDuringExecution(
                                            preference = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_node_affinity_preference.com_coreos_monitoring_v1_Alertmanager_spec_affinity_nodeAffinity_preference(
                                                match_expressions = [
                                                    kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_node_affinity_preference_match_expressions.com_coreos_monitoring_v1_Alertmanager_spec_affinity_nodeAffinity_preference_matchExpressions(
                                                        key = '0', 
                                                        operator = '0', 
                                                        values = [
                                                            '0'
                                                            ], )
                                                    ], 
                                                match_fields = [
                                                    kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_node_affinity_preference_match_expressions.com_coreos_monitoring_v1_Alertmanager_spec_affinity_nodeAffinity_preference_matchExpressions(
                                                        key = '0', 
                                                        operator = '0', )
                                                    ], ), 
                                            weight = 56, )
                                        ], 
                                    required_during_scheduling_ignored_during_execution = kubernetes.client.models.io_tigera_operator_v1_installation_spec_typha_affinity_node_affinity_required_during_scheduling_ignored_during_execution.io_tigera_operator_v1_Installation_spec_typhaAffinity_nodeAffinity_requiredDuringSchedulingIgnoredDuringExecution(
                                        node_selector_terms = [
                                            kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_node_affinity_required_during_scheduling_ignored_during_execution_node_selector_terms.com_coreos_monitoring_v1_Alertmanager_spec_affinity_nodeAffinity_requiredDuringSchedulingIgnoredDuringExecution_nodeSelectorTerms()
                                            ], ), ), ), 
                            typha_metrics_port = 56, 
                            variant = 'Calico', ), 
                        status = kubernetes.client.models.io_tigera_operator_v1_installation_status.io_tigera_operator_v1_Installation_status(
                            computed = kubernetes.client.models.io_tigera_operator_v1_installation_status_computed.io_tigera_operator_v1_Installation_status_computed(
                                flex_volume_path = '0', 
                                image_path = '0', 
                                image_prefix = '0', 
                                kubernetes_provider = '', 
                                node_metrics_port = 56, 
                                registry = '0', 
                                typha_metrics_port = 56, 
                                variant = 'Calico', ), 
                            image_set = '0', 
                            mtu = 56, 
                            variant = 'Calico', ), )
                    ], 
                kind = '0', 
                metadata = kubernetes.client.models.v1/list_meta.v1.ListMeta(
                    continue = '0', 
                    remaining_item_count = 56, 
                    resource_version = '0', 
                    self_link = '0', )
            )
        else :
            return IoTigeraOperatorV1InstallationList(
                items = [
                    kubernetes.client.models.io/tigera/operator/v1/installation.io.tigera.operator.v1.Installation(
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
                        spec = kubernetes.client.models.io_tigera_operator_v1_installation_spec.io_tigera_operator_v1_Installation_spec(
                            calico_network = kubernetes.client.models.io_tigera_operator_v1_installation_spec_calico_network.io_tigera_operator_v1_Installation_spec_calicoNetwork(
                                bgp = 'Enabled', 
                                container_ip_forwarding = 'Enabled', 
                                host_ports = 'Enabled', 
                                ip_pools = [
                                    kubernetes.client.models.io_tigera_operator_v1_installation_spec_calico_network_ip_pools.io_tigera_operator_v1_Installation_spec_calicoNetwork_ipPools(
                                        block_size = 56, 
                                        cidr = '0', 
                                        encapsulation = 'IPIPCrossSubnet', 
                                        nat_outgoing = 'Enabled', 
                                        node_selector = '0', )
                                    ], 
                                linux_dataplane = 'Iptables', 
                                mtu = 56, 
                                multi_interface_mode = 'None', 
                                node_address_autodetection_v4 = kubernetes.client.models.io_tigera_operator_v1_installation_spec_calico_network_node_address_autodetection_v4.io_tigera_operator_v1_Installation_spec_calicoNetwork_nodeAddressAutodetectionV4(
                                    can_reach = '0', 
                                    cidrs = [
                                        '0'
                                        ], 
                                    first_found = True, 
                                    interface = '0', 
                                    skip_interface = '0', ), 
                                node_address_autodetection_v6 = kubernetes.client.models.io_tigera_operator_v1_installation_spec_calico_network_node_address_autodetection_v6.io_tigera_operator_v1_Installation_spec_calicoNetwork_nodeAddressAutodetectionV6(
                                    can_reach = '0', 
                                    first_found = True, 
                                    interface = '0', 
                                    skip_interface = '0', ), ), 
                            certificate_management = kubernetes.client.models.io_tigera_operator_v1_installation_spec_certificate_management.io_tigera_operator_v1_Installation_spec_certificateManagement(
                                ca_cert = 'YQ==', 
                                key_algorithm = '', 
                                signature_algorithm = '', 
                                signer_name = '0', ), 
                            cni = kubernetes.client.models.io_tigera_operator_v1_installation_spec_cni.io_tigera_operator_v1_Installation_spec_cni(
                                ipam = kubernetes.client.models.io_tigera_operator_v1_installation_spec_cni_ipam.io_tigera_operator_v1_Installation_spec_cni_ipam(
                                    type = 'Calico', ), 
                                type = 'Calico', ), 
                            component_resources = [
                                kubernetes.client.models.io_tigera_operator_v1_installation_spec_component_resources.io_tigera_operator_v1_Installation_spec_componentResources(
                                    component_name = 'Node', 
                                    resource_requirements = kubernetes.client.models.io_tigera_operator_v1_installation_spec_resource_requirements.io_tigera_operator_v1_Installation_spec_resourceRequirements(
                                        limits = {
                                            'key' : None
                                            }, 
                                        requests = {
                                            'key' : None
                                            }, ), )
                                ], 
                            control_plane_node_selector = {
                                'key' : '0'
                                }, 
                            control_plane_tolerations = [
                                kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_tolerations.com_coreos_monitoring_v1_Alertmanager_spec_tolerations(
                                    effect = '0', 
                                    key = '0', 
                                    operator = '0', 
                                    toleration_seconds = 56, 
                                    value = '0', )
                                ], 
                            flex_volume_path = '0', 
                            image_path = '0', 
                            image_prefix = '0', 
                            image_pull_secrets = [
                                kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_image_pull_secrets.com_coreos_monitoring_v1_Alertmanager_spec_imagePullSecrets(
                                    name = '0', )
                                ], 
                            kubernetes_provider = '', 
                            node_metrics_port = 56, 
                            node_update_strategy = kubernetes.client.models.io_tigera_operator_v1_installation_spec_node_update_strategy.io_tigera_operator_v1_Installation_spec_nodeUpdateStrategy(
                                rolling_update = kubernetes.client.models.io_tigera_operator_v1_installation_spec_node_update_strategy_rolling_update.io_tigera_operator_v1_Installation_spec_nodeUpdateStrategy_rollingUpdate(
                                    max_unavailable = kubernetes.client.models.max_unavailable.maxUnavailable(), ), 
                                type = '0', ), 
                            registry = '0', 
                            typha_affinity = kubernetes.client.models.io_tigera_operator_v1_installation_spec_typha_affinity.io_tigera_operator_v1_Installation_spec_typhaAffinity(
                                node_affinity = kubernetes.client.models.io_tigera_operator_v1_installation_spec_typha_affinity_node_affinity.io_tigera_operator_v1_Installation_spec_typhaAffinity_nodeAffinity(
                                    preferred_during_scheduling_ignored_during_execution = [
                                        kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_node_affinity_preferred_during_scheduling_ignored_during_execution.com_coreos_monitoring_v1_Alertmanager_spec_affinity_nodeAffinity_preferredDuringSchedulingIgnoredDuringExecution(
                                            preference = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_node_affinity_preference.com_coreos_monitoring_v1_Alertmanager_spec_affinity_nodeAffinity_preference(
                                                match_expressions = [
                                                    kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_node_affinity_preference_match_expressions.com_coreos_monitoring_v1_Alertmanager_spec_affinity_nodeAffinity_preference_matchExpressions(
                                                        key = '0', 
                                                        operator = '0', 
                                                        values = [
                                                            '0'
                                                            ], )
                                                    ], 
                                                match_fields = [
                                                    kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_node_affinity_preference_match_expressions.com_coreos_monitoring_v1_Alertmanager_spec_affinity_nodeAffinity_preference_matchExpressions(
                                                        key = '0', 
                                                        operator = '0', )
                                                    ], ), 
                                            weight = 56, )
                                        ], 
                                    required_during_scheduling_ignored_during_execution = kubernetes.client.models.io_tigera_operator_v1_installation_spec_typha_affinity_node_affinity_required_during_scheduling_ignored_during_execution.io_tigera_operator_v1_Installation_spec_typhaAffinity_nodeAffinity_requiredDuringSchedulingIgnoredDuringExecution(
                                        node_selector_terms = [
                                            kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_node_affinity_required_during_scheduling_ignored_during_execution_node_selector_terms.com_coreos_monitoring_v1_Alertmanager_spec_affinity_nodeAffinity_requiredDuringSchedulingIgnoredDuringExecution_nodeSelectorTerms()
                                            ], ), ), ), 
                            typha_metrics_port = 56, 
                            variant = 'Calico', ), 
                        status = kubernetes.client.models.io_tigera_operator_v1_installation_status.io_tigera_operator_v1_Installation_status(
                            computed = kubernetes.client.models.io_tigera_operator_v1_installation_status_computed.io_tigera_operator_v1_Installation_status_computed(
                                flex_volume_path = '0', 
                                image_path = '0', 
                                image_prefix = '0', 
                                kubernetes_provider = '', 
                                node_metrics_port = 56, 
                                registry = '0', 
                                typha_metrics_port = 56, 
                                variant = 'Calico', ), 
                            image_set = '0', 
                            mtu = 56, 
                            variant = 'Calico', ), )
                    ],
        )

    def testIoTigeraOperatorV1InstallationList(self):
        """Test IoTigeraOperatorV1InstallationList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()