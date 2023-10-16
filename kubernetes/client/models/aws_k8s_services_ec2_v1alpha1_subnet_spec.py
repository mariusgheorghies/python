# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.25.12
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class AwsK8sServicesEc2V1alpha1SubnetSpec(object):
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
        'assign_i_pv6_address_on_creation': 'bool',
        'availability_zone': 'str',
        'availability_zone_id': 'str',
        'cidr_block': 'str',
        'customer_owned_i_pv4_pool': 'str',
        'enable_dns64': 'bool',
        'enable_resource_name_dnsaaaa_record': 'bool',
        'enable_resource_name_dnsa_record': 'bool',
        'hostname_type': 'str',
        'ipv6_cidr_block': 'str',
        'ipv6_native': 'bool',
        'map_public_ip_on_launch': 'bool',
        'outpost_arn': 'str',
        'route_table_refs': 'list[AwsK8sServicesEc2V1alpha1DHCPOptionsSpecVpcRefs]',
        'route_tables': 'list[str]',
        'tags': 'list[AwsK8sServicesEc2V1alpha1DHCPOptionsSpecTags]',
        'vpc_id': 'str',
        'vpc_ref': 'AwsK8sServicesEc2V1alpha1DHCPOptionsSpecVpcRefs'
    }

    attribute_map = {
        'assign_i_pv6_address_on_creation': 'assignIPv6AddressOnCreation',
        'availability_zone': 'availabilityZone',
        'availability_zone_id': 'availabilityZoneID',
        'cidr_block': 'cidrBlock',
        'customer_owned_i_pv4_pool': 'customerOwnedIPv4Pool',
        'enable_dns64': 'enableDNS64',
        'enable_resource_name_dnsaaaa_record': 'enableResourceNameDNSAAAARecord',
        'enable_resource_name_dnsa_record': 'enableResourceNameDNSARecord',
        'hostname_type': 'hostnameType',
        'ipv6_cidr_block': 'ipv6CIDRBlock',
        'ipv6_native': 'ipv6Native',
        'map_public_ip_on_launch': 'mapPublicIPOnLaunch',
        'outpost_arn': 'outpostARN',
        'route_table_refs': 'routeTableRefs',
        'route_tables': 'routeTables',
        'tags': 'tags',
        'vpc_id': 'vpcID',
        'vpc_ref': 'vpcRef'
    }

    def __init__(self, assign_i_pv6_address_on_creation=None, availability_zone=None, availability_zone_id=None, cidr_block=None, customer_owned_i_pv4_pool=None, enable_dns64=None, enable_resource_name_dnsaaaa_record=None, enable_resource_name_dnsa_record=None, hostname_type=None, ipv6_cidr_block=None, ipv6_native=None, map_public_ip_on_launch=None, outpost_arn=None, route_table_refs=None, route_tables=None, tags=None, vpc_id=None, vpc_ref=None, local_vars_configuration=None):  # noqa: E501
        """AwsK8sServicesEc2V1alpha1SubnetSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._assign_i_pv6_address_on_creation = None
        self._availability_zone = None
        self._availability_zone_id = None
        self._cidr_block = None
        self._customer_owned_i_pv4_pool = None
        self._enable_dns64 = None
        self._enable_resource_name_dnsaaaa_record = None
        self._enable_resource_name_dnsa_record = None
        self._hostname_type = None
        self._ipv6_cidr_block = None
        self._ipv6_native = None
        self._map_public_ip_on_launch = None
        self._outpost_arn = None
        self._route_table_refs = None
        self._route_tables = None
        self._tags = None
        self._vpc_id = None
        self._vpc_ref = None
        self.discriminator = None

        if assign_i_pv6_address_on_creation is not None:
            self.assign_i_pv6_address_on_creation = assign_i_pv6_address_on_creation
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if availability_zone_id is not None:
            self.availability_zone_id = availability_zone_id
        if cidr_block is not None:
            self.cidr_block = cidr_block
        if customer_owned_i_pv4_pool is not None:
            self.customer_owned_i_pv4_pool = customer_owned_i_pv4_pool
        if enable_dns64 is not None:
            self.enable_dns64 = enable_dns64
        if enable_resource_name_dnsaaaa_record is not None:
            self.enable_resource_name_dnsaaaa_record = enable_resource_name_dnsaaaa_record
        if enable_resource_name_dnsa_record is not None:
            self.enable_resource_name_dnsa_record = enable_resource_name_dnsa_record
        if hostname_type is not None:
            self.hostname_type = hostname_type
        if ipv6_cidr_block is not None:
            self.ipv6_cidr_block = ipv6_cidr_block
        if ipv6_native is not None:
            self.ipv6_native = ipv6_native
        if map_public_ip_on_launch is not None:
            self.map_public_ip_on_launch = map_public_ip_on_launch
        if outpost_arn is not None:
            self.outpost_arn = outpost_arn
        if route_table_refs is not None:
            self.route_table_refs = route_table_refs
        if route_tables is not None:
            self.route_tables = route_tables
        if tags is not None:
            self.tags = tags
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if vpc_ref is not None:
            self.vpc_ref = vpc_ref

    @property
    def assign_i_pv6_address_on_creation(self):
        """Gets the assign_i_pv6_address_on_creation of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501


        :return: The assign_i_pv6_address_on_creation of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :rtype: bool
        """
        return self._assign_i_pv6_address_on_creation

    @assign_i_pv6_address_on_creation.setter
    def assign_i_pv6_address_on_creation(self, assign_i_pv6_address_on_creation):
        """Sets the assign_i_pv6_address_on_creation of this AwsK8sServicesEc2V1alpha1SubnetSpec.


        :param assign_i_pv6_address_on_creation: The assign_i_pv6_address_on_creation of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :type: bool
        """

        self._assign_i_pv6_address_on_creation = assign_i_pv6_address_on_creation

    @property
    def availability_zone(self):
        """Gets the availability_zone of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501

        The Availability Zone or Local Zone for the subnet.   Default: Amazon Web Services selects one for you. If you create more than one subnet in your VPC, we do not necessarily select a different zone for each subnet.   To create a subnet in a Local Zone, set this value to the Local Zone ID, for example us-west-2-lax-1a. For information about the Regions that support Local Zones, see Available Regions (https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in the Amazon Elastic Compute Cloud User Guide.   To create a subnet in an Outpost, set this value to the Availability Zone for the Outpost and specify the Outpost ARN.  # noqa: E501

        :return: The availability_zone of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this AwsK8sServicesEc2V1alpha1SubnetSpec.

        The Availability Zone or Local Zone for the subnet.   Default: Amazon Web Services selects one for you. If you create more than one subnet in your VPC, we do not necessarily select a different zone for each subnet.   To create a subnet in a Local Zone, set this value to the Local Zone ID, for example us-west-2-lax-1a. For information about the Regions that support Local Zones, see Available Regions (https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in the Amazon Elastic Compute Cloud User Guide.   To create a subnet in an Outpost, set this value to the Availability Zone for the Outpost and specify the Outpost ARN.  # noqa: E501

        :param availability_zone: The availability_zone of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :type: str
        """

        self._availability_zone = availability_zone

    @property
    def availability_zone_id(self):
        """Gets the availability_zone_id of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501

        The AZ ID or the Local Zone ID of the subnet.  # noqa: E501

        :return: The availability_zone_id of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :rtype: str
        """
        return self._availability_zone_id

    @availability_zone_id.setter
    def availability_zone_id(self, availability_zone_id):
        """Sets the availability_zone_id of this AwsK8sServicesEc2V1alpha1SubnetSpec.

        The AZ ID or the Local Zone ID of the subnet.  # noqa: E501

        :param availability_zone_id: The availability_zone_id of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :type: str
        """

        self._availability_zone_id = availability_zone_id

    @property
    def cidr_block(self):
        """Gets the cidr_block of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501

        The IPv4 network range for the subnet, in CIDR notation. For example, 10.0.0.0/24. We modify the specified CIDR block to its canonical form; for example, if you specify 100.68.0.18/18, we modify it to 100.68.0.0/18.   This parameter is not supported for an IPv6 only subnet.  # noqa: E501

        :return: The cidr_block of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :rtype: str
        """
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, cidr_block):
        """Sets the cidr_block of this AwsK8sServicesEc2V1alpha1SubnetSpec.

        The IPv4 network range for the subnet, in CIDR notation. For example, 10.0.0.0/24. We modify the specified CIDR block to its canonical form; for example, if you specify 100.68.0.18/18, we modify it to 100.68.0.0/18.   This parameter is not supported for an IPv6 only subnet.  # noqa: E501

        :param cidr_block: The cidr_block of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :type: str
        """

        self._cidr_block = cidr_block

    @property
    def customer_owned_i_pv4_pool(self):
        """Gets the customer_owned_i_pv4_pool of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501


        :return: The customer_owned_i_pv4_pool of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :rtype: str
        """
        return self._customer_owned_i_pv4_pool

    @customer_owned_i_pv4_pool.setter
    def customer_owned_i_pv4_pool(self, customer_owned_i_pv4_pool):
        """Sets the customer_owned_i_pv4_pool of this AwsK8sServicesEc2V1alpha1SubnetSpec.


        :param customer_owned_i_pv4_pool: The customer_owned_i_pv4_pool of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :type: str
        """

        self._customer_owned_i_pv4_pool = customer_owned_i_pv4_pool

    @property
    def enable_dns64(self):
        """Gets the enable_dns64 of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501


        :return: The enable_dns64 of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :rtype: bool
        """
        return self._enable_dns64

    @enable_dns64.setter
    def enable_dns64(self, enable_dns64):
        """Sets the enable_dns64 of this AwsK8sServicesEc2V1alpha1SubnetSpec.


        :param enable_dns64: The enable_dns64 of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :type: bool
        """

        self._enable_dns64 = enable_dns64

    @property
    def enable_resource_name_dnsaaaa_record(self):
        """Gets the enable_resource_name_dnsaaaa_record of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501


        :return: The enable_resource_name_dnsaaaa_record of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :rtype: bool
        """
        return self._enable_resource_name_dnsaaaa_record

    @enable_resource_name_dnsaaaa_record.setter
    def enable_resource_name_dnsaaaa_record(self, enable_resource_name_dnsaaaa_record):
        """Sets the enable_resource_name_dnsaaaa_record of this AwsK8sServicesEc2V1alpha1SubnetSpec.


        :param enable_resource_name_dnsaaaa_record: The enable_resource_name_dnsaaaa_record of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :type: bool
        """

        self._enable_resource_name_dnsaaaa_record = enable_resource_name_dnsaaaa_record

    @property
    def enable_resource_name_dnsa_record(self):
        """Gets the enable_resource_name_dnsa_record of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501


        :return: The enable_resource_name_dnsa_record of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :rtype: bool
        """
        return self._enable_resource_name_dnsa_record

    @enable_resource_name_dnsa_record.setter
    def enable_resource_name_dnsa_record(self, enable_resource_name_dnsa_record):
        """Sets the enable_resource_name_dnsa_record of this AwsK8sServicesEc2V1alpha1SubnetSpec.


        :param enable_resource_name_dnsa_record: The enable_resource_name_dnsa_record of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :type: bool
        """

        self._enable_resource_name_dnsa_record = enable_resource_name_dnsa_record

    @property
    def hostname_type(self):
        """Gets the hostname_type of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501


        :return: The hostname_type of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :rtype: str
        """
        return self._hostname_type

    @hostname_type.setter
    def hostname_type(self, hostname_type):
        """Sets the hostname_type of this AwsK8sServicesEc2V1alpha1SubnetSpec.


        :param hostname_type: The hostname_type of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :type: str
        """

        self._hostname_type = hostname_type

    @property
    def ipv6_cidr_block(self):
        """Gets the ipv6_cidr_block of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501

        The IPv6 network range for the subnet, in CIDR notation. The subnet size must use a /64 prefix length.   This parameter is required for an IPv6 only subnet.  # noqa: E501

        :return: The ipv6_cidr_block of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :rtype: str
        """
        return self._ipv6_cidr_block

    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, ipv6_cidr_block):
        """Sets the ipv6_cidr_block of this AwsK8sServicesEc2V1alpha1SubnetSpec.

        The IPv6 network range for the subnet, in CIDR notation. The subnet size must use a /64 prefix length.   This parameter is required for an IPv6 only subnet.  # noqa: E501

        :param ipv6_cidr_block: The ipv6_cidr_block of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :type: str
        """

        self._ipv6_cidr_block = ipv6_cidr_block

    @property
    def ipv6_native(self):
        """Gets the ipv6_native of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501

        Indicates whether to create an IPv6 only subnet.  # noqa: E501

        :return: The ipv6_native of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :rtype: bool
        """
        return self._ipv6_native

    @ipv6_native.setter
    def ipv6_native(self, ipv6_native):
        """Sets the ipv6_native of this AwsK8sServicesEc2V1alpha1SubnetSpec.

        Indicates whether to create an IPv6 only subnet.  # noqa: E501

        :param ipv6_native: The ipv6_native of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :type: bool
        """

        self._ipv6_native = ipv6_native

    @property
    def map_public_ip_on_launch(self):
        """Gets the map_public_ip_on_launch of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501


        :return: The map_public_ip_on_launch of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :rtype: bool
        """
        return self._map_public_ip_on_launch

    @map_public_ip_on_launch.setter
    def map_public_ip_on_launch(self, map_public_ip_on_launch):
        """Sets the map_public_ip_on_launch of this AwsK8sServicesEc2V1alpha1SubnetSpec.


        :param map_public_ip_on_launch: The map_public_ip_on_launch of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :type: bool
        """

        self._map_public_ip_on_launch = map_public_ip_on_launch

    @property
    def outpost_arn(self):
        """Gets the outpost_arn of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501

        The Amazon Resource Name (ARN) of the Outpost. If you specify an Outpost ARN, you must also specify the Availability Zone of the Outpost subnet.  # noqa: E501

        :return: The outpost_arn of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :rtype: str
        """
        return self._outpost_arn

    @outpost_arn.setter
    def outpost_arn(self, outpost_arn):
        """Sets the outpost_arn of this AwsK8sServicesEc2V1alpha1SubnetSpec.

        The Amazon Resource Name (ARN) of the Outpost. If you specify an Outpost ARN, you must also specify the Availability Zone of the Outpost subnet.  # noqa: E501

        :param outpost_arn: The outpost_arn of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :type: str
        """

        self._outpost_arn = outpost_arn

    @property
    def route_table_refs(self):
        """Gets the route_table_refs of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501


        :return: The route_table_refs of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :rtype: list[AwsK8sServicesEc2V1alpha1DHCPOptionsSpecVpcRefs]
        """
        return self._route_table_refs

    @route_table_refs.setter
    def route_table_refs(self, route_table_refs):
        """Sets the route_table_refs of this AwsK8sServicesEc2V1alpha1SubnetSpec.


        :param route_table_refs: The route_table_refs of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :type: list[AwsK8sServicesEc2V1alpha1DHCPOptionsSpecVpcRefs]
        """

        self._route_table_refs = route_table_refs

    @property
    def route_tables(self):
        """Gets the route_tables of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501


        :return: The route_tables of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._route_tables

    @route_tables.setter
    def route_tables(self, route_tables):
        """Sets the route_tables of this AwsK8sServicesEc2V1alpha1SubnetSpec.


        :param route_tables: The route_tables of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :type: list[str]
        """

        self._route_tables = route_tables

    @property
    def tags(self):
        """Gets the tags of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501

        The tags. The value parameter is required, but if you don't want the tag to have a value, specify the parameter with no value, and we set the value to an empty string.  # noqa: E501

        :return: The tags of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :rtype: list[AwsK8sServicesEc2V1alpha1DHCPOptionsSpecTags]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AwsK8sServicesEc2V1alpha1SubnetSpec.

        The tags. The value parameter is required, but if you don't want the tag to have a value, specify the parameter with no value, and we set the value to an empty string.  # noqa: E501

        :param tags: The tags of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :type: list[AwsK8sServicesEc2V1alpha1DHCPOptionsSpecTags]
        """

        self._tags = tags

    @property
    def vpc_id(self):
        """Gets the vpc_id of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501

        The ID of the VPC.  # noqa: E501

        :return: The vpc_id of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this AwsK8sServicesEc2V1alpha1SubnetSpec.

        The ID of the VPC.  # noqa: E501

        :param vpc_id: The vpc_id of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :type: str
        """

        self._vpc_id = vpc_id

    @property
    def vpc_ref(self):
        """Gets the vpc_ref of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501


        :return: The vpc_ref of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :rtype: AwsK8sServicesEc2V1alpha1DHCPOptionsSpecVpcRefs
        """
        return self._vpc_ref

    @vpc_ref.setter
    def vpc_ref(self, vpc_ref):
        """Sets the vpc_ref of this AwsK8sServicesEc2V1alpha1SubnetSpec.


        :param vpc_ref: The vpc_ref of this AwsK8sServicesEc2V1alpha1SubnetSpec.  # noqa: E501
        :type: AwsK8sServicesEc2V1alpha1DHCPOptionsSpecVpcRefs
        """

        self._vpc_ref = vpc_ref

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
        if not isinstance(other, AwsK8sServicesEc2V1alpha1SubnetSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AwsK8sServicesEc2V1alpha1SubnetSpec):
            return True

        return self.to_dict() != other.to_dict()