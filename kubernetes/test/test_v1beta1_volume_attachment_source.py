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
from kubernetes.client.models.v1beta1_volume_attachment_source import V1beta1VolumeAttachmentSource  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1beta1VolumeAttachmentSource(unittest.TestCase):
    """V1beta1VolumeAttachmentSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1beta1VolumeAttachmentSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1beta1_volume_attachment_source.V1beta1VolumeAttachmentSource()  # noqa: E501
        if include_optional :
            return V1beta1VolumeAttachmentSource(
                inline_volume_spec = kubernetes.client.models.v1/persistent_volume_spec.v1.PersistentVolumeSpec(
                    access_modes = [
                        '0'
                        ], 
                    aws_elastic_block_store = kubernetes.client.models.v1/aws_elastic_block_store_volume_source.v1.AWSElasticBlockStoreVolumeSource(
                        fs_type = '0', 
                        partition = 56, 
                        read_only = True, 
                        volume_id = '0', ), 
                    azure_disk = kubernetes.client.models.v1/azure_disk_volume_source.v1.AzureDiskVolumeSource(
                        caching_mode = '0', 
                        disk_name = '0', 
                        disk_uri = '0', 
                        fs_type = '0', 
                        kind = '0', 
                        read_only = True, ), 
                    azure_file = kubernetes.client.models.v1/azure_file_persistent_volume_source.v1.AzureFilePersistentVolumeSource(
                        read_only = True, 
                        secret_name = '0', 
                        secret_namespace = '0', 
                        share_name = '0', ), 
                    capacity = {
                        'key' : '0'
                        }, 
                    cephfs = kubernetes.client.models.v1/ceph_fs_persistent_volume_source.v1.CephFSPersistentVolumeSource(
                        monitors = [
                            '0'
                            ], 
                        path = '0', 
                        read_only = True, 
                        secret_file = '0', 
                        secret_ref = kubernetes.client.models.v1/secret_reference.v1.SecretReference(
                            name = '0', 
                            namespace = '0', ), 
                        user = '0', ), 
                    cinder = kubernetes.client.models.v1/cinder_persistent_volume_source.v1.CinderPersistentVolumeSource(
                        fs_type = '0', 
                        read_only = True, 
                        volume_id = '0', ), 
                    claim_ref = kubernetes.client.models.v1/object_reference.v1.ObjectReference(
                        api_version = '0', 
                        field_path = '0', 
                        kind = '0', 
                        name = '0', 
                        namespace = '0', 
                        resource_version = '0', 
                        uid = '0', ), 
                    csi = kubernetes.client.models.v1/csi_persistent_volume_source.v1.CSIPersistentVolumeSource(
                        controller_expand_secret_ref = kubernetes.client.models.v1/secret_reference.v1.SecretReference(
                            name = '0', 
                            namespace = '0', ), 
                        controller_publish_secret_ref = kubernetes.client.models.v1/secret_reference.v1.SecretReference(
                            name = '0', 
                            namespace = '0', ), 
                        driver = '0', 
                        fs_type = '0', 
                        node_publish_secret_ref = kubernetes.client.models.v1/secret_reference.v1.SecretReference(
                            name = '0', 
                            namespace = '0', ), 
                        node_stage_secret_ref = kubernetes.client.models.v1/secret_reference.v1.SecretReference(
                            name = '0', 
                            namespace = '0', ), 
                        read_only = True, 
                        volume_attributes = {
                            'key' : '0'
                            }, 
                        volume_handle = '0', ), 
                    fc = kubernetes.client.models.v1/fc_volume_source.v1.FCVolumeSource(
                        fs_type = '0', 
                        lun = 56, 
                        read_only = True, 
                        target_ww_ns = [
                            '0'
                            ], 
                        wwids = [
                            '0'
                            ], ), 
                    flex_volume = kubernetes.client.models.v1/flex_persistent_volume_source.v1.FlexPersistentVolumeSource(
                        driver = '0', 
                        fs_type = '0', 
                        options = {
                            'key' : '0'
                            }, 
                        read_only = True, ), 
                    flocker = kubernetes.client.models.v1/flocker_volume_source.v1.FlockerVolumeSource(
                        dataset_name = '0', 
                        dataset_uuid = '0', ), 
                    gce_persistent_disk = kubernetes.client.models.v1/gce_persistent_disk_volume_source.v1.GCEPersistentDiskVolumeSource(
                        fs_type = '0', 
                        partition = 56, 
                        pd_name = '0', 
                        read_only = True, ), 
                    glusterfs = kubernetes.client.models.v1/glusterfs_persistent_volume_source.v1.GlusterfsPersistentVolumeSource(
                        endpoints = '0', 
                        endpoints_namespace = '0', 
                        path = '0', 
                        read_only = True, ), 
                    host_path = kubernetes.client.models.v1/host_path_volume_source.v1.HostPathVolumeSource(
                        path = '0', 
                        type = '0', ), 
                    iscsi = kubernetes.client.models.v1/iscsi_persistent_volume_source.v1.ISCSIPersistentVolumeSource(
                        chap_auth_discovery = True, 
                        chap_auth_session = True, 
                        fs_type = '0', 
                        initiator_name = '0', 
                        iqn = '0', 
                        iscsi_interface = '0', 
                        lun = 56, 
                        portals = [
                            '0'
                            ], 
                        read_only = True, 
                        target_portal = '0', ), 
                    local = kubernetes.client.models.v1/local_volume_source.v1.LocalVolumeSource(
                        fs_type = '0', 
                        path = '0', ), 
                    mount_options = [
                        '0'
                        ], 
                    nfs = kubernetes.client.models.v1/nfs_volume_source.v1.NFSVolumeSource(
                        path = '0', 
                        read_only = True, 
                        server = '0', ), 
                    node_affinity = kubernetes.client.models.v1/volume_node_affinity.v1.VolumeNodeAffinity(
                        required = kubernetes.client.models.v1/node_selector.v1.NodeSelector(
                            node_selector_terms = [
                                kubernetes.client.models.v1/node_selector_term.v1.NodeSelectorTerm(
                                    match_expressions = [
                                        kubernetes.client.models.v1/node_selector_requirement.v1.NodeSelectorRequirement(
                                            key = '0', 
                                            operator = '0', 
                                            values = [
                                                '0'
                                                ], )
                                        ], 
                                    match_fields = [
                                        kubernetes.client.models.v1/node_selector_requirement.v1.NodeSelectorRequirement(
                                            key = '0', 
                                            operator = '0', )
                                        ], )
                                ], ), ), 
                    persistent_volume_reclaim_policy = '0', 
                    photon_persistent_disk = kubernetes.client.models.v1/photon_persistent_disk_volume_source.v1.PhotonPersistentDiskVolumeSource(
                        fs_type = '0', 
                        pd_id = '0', ), 
                    portworx_volume = kubernetes.client.models.v1/portworx_volume_source.v1.PortworxVolumeSource(
                        fs_type = '0', 
                        read_only = True, 
                        volume_id = '0', ), 
                    quobyte = kubernetes.client.models.v1/quobyte_volume_source.v1.QuobyteVolumeSource(
                        group = '0', 
                        read_only = True, 
                        registry = '0', 
                        tenant = '0', 
                        user = '0', 
                        volume = '0', ), 
                    rbd = kubernetes.client.models.v1/rbd_persistent_volume_source.v1.RBDPersistentVolumeSource(
                        fs_type = '0', 
                        image = '0', 
                        keyring = '0', 
                        monitors = [
                            '0'
                            ], 
                        pool = '0', 
                        read_only = True, 
                        user = '0', ), 
                    scale_io = kubernetes.client.models.v1/scale_io_persistent_volume_source.v1.ScaleIOPersistentVolumeSource(
                        fs_type = '0', 
                        gateway = '0', 
                        protection_domain = '0', 
                        read_only = True, 
                        secret_ref = kubernetes.client.models.v1/secret_reference.v1.SecretReference(
                            name = '0', 
                            namespace = '0', ), 
                        ssl_enabled = True, 
                        storage_mode = '0', 
                        storage_pool = '0', 
                        system = '0', 
                        volume_name = '0', ), 
                    storage_class_name = '0', 
                    storageos = kubernetes.client.models.v1/storage_os_persistent_volume_source.v1.StorageOSPersistentVolumeSource(
                        fs_type = '0', 
                        read_only = True, 
                        volume_name = '0', 
                        volume_namespace = '0', ), 
                    volume_mode = '0', 
                    vsphere_volume = kubernetes.client.models.v1/vsphere_virtual_disk_volume_source.v1.VsphereVirtualDiskVolumeSource(
                        fs_type = '0', 
                        storage_policy_id = '0', 
                        storage_policy_name = '0', 
                        volume_path = '0', ), ), 
                persistent_volume_name = '0'
            )
        else :
            return V1beta1VolumeAttachmentSource(
        )

    def testV1beta1VolumeAttachmentSource(self):
        """Test V1beta1VolumeAttachmentSource"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
