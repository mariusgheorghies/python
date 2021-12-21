# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.20.7
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'addresses': 'list[IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionAddresses]',
        'availability_zone': 'str',
        'ebs_optimized': 'bool',
        'ena_support': 'bool',
        'iam_profile': 'str',
        'id': 'str',
        'image_id': 'str',
        'instance_state': 'str',
        'network_interfaces': 'list[str]',
        'non_root_volumes': 'list[IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastionNonRootVolumes]',
        'private_ip': 'str',
        'public_ip': 'str',
        'root_volume': 'IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastionRootVolume',
        'security_group_ids': 'list[str]',
        'spot_market_options': 'IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionSpotMarketOptions',
        'ssh_key_name': 'str',
        'subnet_id': 'str',
        'tags': 'dict(str, str)',
        'tenancy': 'str',
        'type': 'str',
        'user_data': 'str',
        'volume_i_ds': 'list[str]'
    }

    attribute_map = {
        'addresses': 'addresses',
        'availability_zone': 'availabilityZone',
        'ebs_optimized': 'ebsOptimized',
        'ena_support': 'enaSupport',
        'iam_profile': 'iamProfile',
        'id': 'id',
        'image_id': 'imageId',
        'instance_state': 'instanceState',
        'network_interfaces': 'networkInterfaces',
        'non_root_volumes': 'nonRootVolumes',
        'private_ip': 'privateIp',
        'public_ip': 'publicIp',
        'root_volume': 'rootVolume',
        'security_group_ids': 'securityGroupIds',
        'spot_market_options': 'spotMarketOptions',
        'ssh_key_name': 'sshKeyName',
        'subnet_id': 'subnetId',
        'tags': 'tags',
        'tenancy': 'tenancy',
        'type': 'type',
        'user_data': 'userData',
        'volume_i_ds': 'volumeIDs'
    }

    def __init__(self, addresses=None, availability_zone=None, ebs_optimized=None, ena_support=None, iam_profile=None, id=None, image_id=None, instance_state=None, network_interfaces=None, non_root_volumes=None, private_ip=None, public_ip=None, root_volume=None, security_group_ids=None, spot_market_options=None, ssh_key_name=None, subnet_id=None, tags=None, tenancy=None, type=None, user_data=None, volume_i_ds=None, local_vars_configuration=None):  # noqa: E501
        """IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._addresses = None
        self._availability_zone = None
        self._ebs_optimized = None
        self._ena_support = None
        self._iam_profile = None
        self._id = None
        self._image_id = None
        self._instance_state = None
        self._network_interfaces = None
        self._non_root_volumes = None
        self._private_ip = None
        self._public_ip = None
        self._root_volume = None
        self._security_group_ids = None
        self._spot_market_options = None
        self._ssh_key_name = None
        self._subnet_id = None
        self._tags = None
        self._tenancy = None
        self._type = None
        self._user_data = None
        self._volume_i_ds = None
        self.discriminator = None

        if addresses is not None:
            self.addresses = addresses
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if ebs_optimized is not None:
            self.ebs_optimized = ebs_optimized
        if ena_support is not None:
            self.ena_support = ena_support
        if iam_profile is not None:
            self.iam_profile = iam_profile
        self.id = id
        if image_id is not None:
            self.image_id = image_id
        if instance_state is not None:
            self.instance_state = instance_state
        if network_interfaces is not None:
            self.network_interfaces = network_interfaces
        if non_root_volumes is not None:
            self.non_root_volumes = non_root_volumes
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if root_volume is not None:
            self.root_volume = root_volume
        if security_group_ids is not None:
            self.security_group_ids = security_group_ids
        if spot_market_options is not None:
            self.spot_market_options = spot_market_options
        if ssh_key_name is not None:
            self.ssh_key_name = ssh_key_name
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if tags is not None:
            self.tags = tags
        if tenancy is not None:
            self.tenancy = tenancy
        if type is not None:
            self.type = type
        if user_data is not None:
            self.user_data = user_data
        if volume_i_ds is not None:
            self.volume_i_ds = volume_i_ds

    @property
    def addresses(self):
        """Gets the addresses of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501

        Addresses contains the AWS instance associated addresses.  # noqa: E501

        :return: The addresses of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :rtype: list[IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionAddresses]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.

        Addresses contains the AWS instance associated addresses.  # noqa: E501

        :param addresses: The addresses of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :type: list[IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionAddresses]
        """

        self._addresses = addresses

    @property
    def availability_zone(self):
        """Gets the availability_zone of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501

        Availability zone of instance  # noqa: E501

        :return: The availability_zone of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.

        Availability zone of instance  # noqa: E501

        :param availability_zone: The availability_zone of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :type: str
        """

        self._availability_zone = availability_zone

    @property
    def ebs_optimized(self):
        """Gets the ebs_optimized of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501

        Indicates whether the instance is optimized for Amazon EBS I/O.  # noqa: E501

        :return: The ebs_optimized of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :rtype: bool
        """
        return self._ebs_optimized

    @ebs_optimized.setter
    def ebs_optimized(self, ebs_optimized):
        """Sets the ebs_optimized of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.

        Indicates whether the instance is optimized for Amazon EBS I/O.  # noqa: E501

        :param ebs_optimized: The ebs_optimized of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :type: bool
        """

        self._ebs_optimized = ebs_optimized

    @property
    def ena_support(self):
        """Gets the ena_support of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501

        Specifies whether enhanced networking with ENA is enabled.  # noqa: E501

        :return: The ena_support of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :rtype: bool
        """
        return self._ena_support

    @ena_support.setter
    def ena_support(self, ena_support):
        """Sets the ena_support of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.

        Specifies whether enhanced networking with ENA is enabled.  # noqa: E501

        :param ena_support: The ena_support of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :type: bool
        """

        self._ena_support = ena_support

    @property
    def iam_profile(self):
        """Gets the iam_profile of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501

        The name of the IAM instance profile associated with the instance, if applicable.  # noqa: E501

        :return: The iam_profile of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :rtype: str
        """
        return self._iam_profile

    @iam_profile.setter
    def iam_profile(self, iam_profile):
        """Sets the iam_profile of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.

        The name of the IAM instance profile associated with the instance, if applicable.  # noqa: E501

        :param iam_profile: The iam_profile of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :type: str
        """

        self._iam_profile = iam_profile

    @property
    def id(self):
        """Gets the id of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501


        :return: The id of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.


        :param id: The id of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def image_id(self):
        """Gets the image_id of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501

        The ID of the AMI used to launch the instance.  # noqa: E501

        :return: The image_id of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.

        The ID of the AMI used to launch the instance.  # noqa: E501

        :param image_id: The image_id of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :type: str
        """

        self._image_id = image_id

    @property
    def instance_state(self):
        """Gets the instance_state of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501

        The current state of the instance.  # noqa: E501

        :return: The instance_state of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :rtype: str
        """
        return self._instance_state

    @instance_state.setter
    def instance_state(self, instance_state):
        """Sets the instance_state of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.

        The current state of the instance.  # noqa: E501

        :param instance_state: The instance_state of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :type: str
        """

        self._instance_state = instance_state

    @property
    def network_interfaces(self):
        """Gets the network_interfaces of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501

        Specifies ENIs attached to instance  # noqa: E501

        :return: The network_interfaces of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :rtype: list[str]
        """
        return self._network_interfaces

    @network_interfaces.setter
    def network_interfaces(self, network_interfaces):
        """Sets the network_interfaces of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.

        Specifies ENIs attached to instance  # noqa: E501

        :param network_interfaces: The network_interfaces of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :type: list[str]
        """

        self._network_interfaces = network_interfaces

    @property
    def non_root_volumes(self):
        """Gets the non_root_volumes of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501

        Configuration options for the non root storage volumes.  # noqa: E501

        :return: The non_root_volumes of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :rtype: list[IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastionNonRootVolumes]
        """
        return self._non_root_volumes

    @non_root_volumes.setter
    def non_root_volumes(self, non_root_volumes):
        """Sets the non_root_volumes of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.

        Configuration options for the non root storage volumes.  # noqa: E501

        :param non_root_volumes: The non_root_volumes of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :type: list[IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastionNonRootVolumes]
        """

        self._non_root_volumes = non_root_volumes

    @property
    def private_ip(self):
        """Gets the private_ip of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501

        The private IPv4 address assigned to the instance.  # noqa: E501

        :return: The private_ip of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.

        The private IPv4 address assigned to the instance.  # noqa: E501

        :param private_ip: The private_ip of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :type: str
        """

        self._private_ip = private_ip

    @property
    def public_ip(self):
        """Gets the public_ip of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501

        The public IPv4 address assigned to the instance, if applicable.  # noqa: E501

        :return: The public_ip of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.

        The public IPv4 address assigned to the instance, if applicable.  # noqa: E501

        :param public_ip: The public_ip of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :type: str
        """

        self._public_ip = public_ip

    @property
    def root_volume(self):
        """Gets the root_volume of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501


        :return: The root_volume of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :rtype: IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastionRootVolume
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        """Sets the root_volume of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.


        :param root_volume: The root_volume of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :type: IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastionRootVolume
        """

        self._root_volume = root_volume

    @property
    def security_group_ids(self):
        """Gets the security_group_ids of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501

        SecurityGroupIDs are one or more security group IDs this instance belongs to.  # noqa: E501

        :return: The security_group_ids of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :rtype: list[str]
        """
        return self._security_group_ids

    @security_group_ids.setter
    def security_group_ids(self, security_group_ids):
        """Sets the security_group_ids of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.

        SecurityGroupIDs are one or more security group IDs this instance belongs to.  # noqa: E501

        :param security_group_ids: The security_group_ids of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :type: list[str]
        """

        self._security_group_ids = security_group_ids

    @property
    def spot_market_options(self):
        """Gets the spot_market_options of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501


        :return: The spot_market_options of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :rtype: IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionSpotMarketOptions
        """
        return self._spot_market_options

    @spot_market_options.setter
    def spot_market_options(self, spot_market_options):
        """Sets the spot_market_options of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.


        :param spot_market_options: The spot_market_options of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :type: IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionSpotMarketOptions
        """

        self._spot_market_options = spot_market_options

    @property
    def ssh_key_name(self):
        """Gets the ssh_key_name of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501

        The name of the SSH key pair.  # noqa: E501

        :return: The ssh_key_name of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :rtype: str
        """
        return self._ssh_key_name

    @ssh_key_name.setter
    def ssh_key_name(self, ssh_key_name):
        """Sets the ssh_key_name of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.

        The name of the SSH key pair.  # noqa: E501

        :param ssh_key_name: The ssh_key_name of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :type: str
        """

        self._ssh_key_name = ssh_key_name

    @property
    def subnet_id(self):
        """Gets the subnet_id of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501

        The ID of the subnet of the instance.  # noqa: E501

        :return: The subnet_id of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.

        The ID of the subnet of the instance.  # noqa: E501

        :param subnet_id: The subnet_id of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :type: str
        """

        self._subnet_id = subnet_id

    @property
    def tags(self):
        """Gets the tags of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501

        The tags associated with the instance.  # noqa: E501

        :return: The tags of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.

        The tags associated with the instance.  # noqa: E501

        :param tags: The tags of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :type: dict(str, str)
        """

        self._tags = tags

    @property
    def tenancy(self):
        """Gets the tenancy of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501

        Tenancy indicates if instance should run on shared or single-tenant hardware.  # noqa: E501

        :return: The tenancy of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :rtype: str
        """
        return self._tenancy

    @tenancy.setter
    def tenancy(self, tenancy):
        """Sets the tenancy of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.

        Tenancy indicates if instance should run on shared or single-tenant hardware.  # noqa: E501

        :param tenancy: The tenancy of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :type: str
        """

        self._tenancy = tenancy

    @property
    def type(self):
        """Gets the type of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501

        The instance type.  # noqa: E501

        :return: The type of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.

        The instance type.  # noqa: E501

        :param type: The type of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def user_data(self):
        """Gets the user_data of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501

        UserData is the raw data script passed to the instance which is run upon bootstrap. This field must not be base64 encoded and should only be used when running a new instance.  # noqa: E501

        :return: The user_data of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.

        UserData is the raw data script passed to the instance which is run upon bootstrap. This field must not be base64 encoded and should only be used when running a new instance.  # noqa: E501

        :param user_data: The user_data of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :type: str
        """

        self._user_data = user_data

    @property
    def volume_i_ds(self):
        """Gets the volume_i_ds of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501

        IDs of the instance's volumes  # noqa: E501

        :return: The volume_i_ds of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :rtype: list[str]
        """
        return self._volume_i_ds

    @volume_i_ds.setter
    def volume_i_ds(self, volume_i_ds):
        """Sets the volume_i_ds of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.

        IDs of the instance's volumes  # noqa: E501

        :param volume_i_ds: The volume_i_ds of this IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion.  # noqa: E501
        :type: list[str]
        """

        self._volume_i_ds = volume_i_ds

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastion):
            return True

        return self.to_dict() != other.to_dict()
