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


class AwsK8sServicesEc2V1alpha1VPCStatus(object):
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
        'ack_resource_metadata': 'AwsK8sServicesEc2V1alpha1DHCPOptionsStatusAckResourceMetadata',
        'cidr_block_association_set': 'list[AwsK8sServicesEc2V1alpha1VPCStatusCidrBlockAssociationSet]',
        'conditions': 'list[AwsK8sServicesEc2V1alpha1DHCPOptionsStatusConditions]',
        'dhcp_options_id': 'str',
        'ipv6_cidr_block_association_set': 'list[AwsK8sServicesEc2V1alpha1VPCStatusIpv6CIDRBlockAssociationSet]',
        'is_default': 'bool',
        'owner_id': 'str',
        'state': 'str',
        'vpc_id': 'str'
    }

    attribute_map = {
        'ack_resource_metadata': 'ackResourceMetadata',
        'cidr_block_association_set': 'cidrBlockAssociationSet',
        'conditions': 'conditions',
        'dhcp_options_id': 'dhcpOptionsID',
        'ipv6_cidr_block_association_set': 'ipv6CIDRBlockAssociationSet',
        'is_default': 'isDefault',
        'owner_id': 'ownerID',
        'state': 'state',
        'vpc_id': 'vpcID'
    }

    def __init__(self, ack_resource_metadata=None, cidr_block_association_set=None, conditions=None, dhcp_options_id=None, ipv6_cidr_block_association_set=None, is_default=None, owner_id=None, state=None, vpc_id=None, local_vars_configuration=None):  # noqa: E501
        """AwsK8sServicesEc2V1alpha1VPCStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ack_resource_metadata = None
        self._cidr_block_association_set = None
        self._conditions = None
        self._dhcp_options_id = None
        self._ipv6_cidr_block_association_set = None
        self._is_default = None
        self._owner_id = None
        self._state = None
        self._vpc_id = None
        self.discriminator = None

        if ack_resource_metadata is not None:
            self.ack_resource_metadata = ack_resource_metadata
        if cidr_block_association_set is not None:
            self.cidr_block_association_set = cidr_block_association_set
        if conditions is not None:
            self.conditions = conditions
        if dhcp_options_id is not None:
            self.dhcp_options_id = dhcp_options_id
        if ipv6_cidr_block_association_set is not None:
            self.ipv6_cidr_block_association_set = ipv6_cidr_block_association_set
        if is_default is not None:
            self.is_default = is_default
        if owner_id is not None:
            self.owner_id = owner_id
        if state is not None:
            self.state = state
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def ack_resource_metadata(self):
        """Gets the ack_resource_metadata of this AwsK8sServicesEc2V1alpha1VPCStatus.  # noqa: E501


        :return: The ack_resource_metadata of this AwsK8sServicesEc2V1alpha1VPCStatus.  # noqa: E501
        :rtype: AwsK8sServicesEc2V1alpha1DHCPOptionsStatusAckResourceMetadata
        """
        return self._ack_resource_metadata

    @ack_resource_metadata.setter
    def ack_resource_metadata(self, ack_resource_metadata):
        """Sets the ack_resource_metadata of this AwsK8sServicesEc2V1alpha1VPCStatus.


        :param ack_resource_metadata: The ack_resource_metadata of this AwsK8sServicesEc2V1alpha1VPCStatus.  # noqa: E501
        :type: AwsK8sServicesEc2V1alpha1DHCPOptionsStatusAckResourceMetadata
        """

        self._ack_resource_metadata = ack_resource_metadata

    @property
    def cidr_block_association_set(self):
        """Gets the cidr_block_association_set of this AwsK8sServicesEc2V1alpha1VPCStatus.  # noqa: E501

        Information about the IPv4 CIDR blocks associated with the VPC.  # noqa: E501

        :return: The cidr_block_association_set of this AwsK8sServicesEc2V1alpha1VPCStatus.  # noqa: E501
        :rtype: list[AwsK8sServicesEc2V1alpha1VPCStatusCidrBlockAssociationSet]
        """
        return self._cidr_block_association_set

    @cidr_block_association_set.setter
    def cidr_block_association_set(self, cidr_block_association_set):
        """Sets the cidr_block_association_set of this AwsK8sServicesEc2V1alpha1VPCStatus.

        Information about the IPv4 CIDR blocks associated with the VPC.  # noqa: E501

        :param cidr_block_association_set: The cidr_block_association_set of this AwsK8sServicesEc2V1alpha1VPCStatus.  # noqa: E501
        :type: list[AwsK8sServicesEc2V1alpha1VPCStatusCidrBlockAssociationSet]
        """

        self._cidr_block_association_set = cidr_block_association_set

    @property
    def conditions(self):
        """Gets the conditions of this AwsK8sServicesEc2V1alpha1VPCStatus.  # noqa: E501

        All CRS managed by ACK have a common `Status.Conditions` member that contains a collection of `ackv1alpha1.Condition` objects that describe the various terminal states of the CR and its backend AWS service API resource  # noqa: E501

        :return: The conditions of this AwsK8sServicesEc2V1alpha1VPCStatus.  # noqa: E501
        :rtype: list[AwsK8sServicesEc2V1alpha1DHCPOptionsStatusConditions]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this AwsK8sServicesEc2V1alpha1VPCStatus.

        All CRS managed by ACK have a common `Status.Conditions` member that contains a collection of `ackv1alpha1.Condition` objects that describe the various terminal states of the CR and its backend AWS service API resource  # noqa: E501

        :param conditions: The conditions of this AwsK8sServicesEc2V1alpha1VPCStatus.  # noqa: E501
        :type: list[AwsK8sServicesEc2V1alpha1DHCPOptionsStatusConditions]
        """

        self._conditions = conditions

    @property
    def dhcp_options_id(self):
        """Gets the dhcp_options_id of this AwsK8sServicesEc2V1alpha1VPCStatus.  # noqa: E501

        The ID of the set of DHCP options you've associated with the VPC.  # noqa: E501

        :return: The dhcp_options_id of this AwsK8sServicesEc2V1alpha1VPCStatus.  # noqa: E501
        :rtype: str
        """
        return self._dhcp_options_id

    @dhcp_options_id.setter
    def dhcp_options_id(self, dhcp_options_id):
        """Sets the dhcp_options_id of this AwsK8sServicesEc2V1alpha1VPCStatus.

        The ID of the set of DHCP options you've associated with the VPC.  # noqa: E501

        :param dhcp_options_id: The dhcp_options_id of this AwsK8sServicesEc2V1alpha1VPCStatus.  # noqa: E501
        :type: str
        """

        self._dhcp_options_id = dhcp_options_id

    @property
    def ipv6_cidr_block_association_set(self):
        """Gets the ipv6_cidr_block_association_set of this AwsK8sServicesEc2V1alpha1VPCStatus.  # noqa: E501

        Information about the IPv6 CIDR blocks associated with the VPC.  # noqa: E501

        :return: The ipv6_cidr_block_association_set of this AwsK8sServicesEc2V1alpha1VPCStatus.  # noqa: E501
        :rtype: list[AwsK8sServicesEc2V1alpha1VPCStatusIpv6CIDRBlockAssociationSet]
        """
        return self._ipv6_cidr_block_association_set

    @ipv6_cidr_block_association_set.setter
    def ipv6_cidr_block_association_set(self, ipv6_cidr_block_association_set):
        """Sets the ipv6_cidr_block_association_set of this AwsK8sServicesEc2V1alpha1VPCStatus.

        Information about the IPv6 CIDR blocks associated with the VPC.  # noqa: E501

        :param ipv6_cidr_block_association_set: The ipv6_cidr_block_association_set of this AwsK8sServicesEc2V1alpha1VPCStatus.  # noqa: E501
        :type: list[AwsK8sServicesEc2V1alpha1VPCStatusIpv6CIDRBlockAssociationSet]
        """

        self._ipv6_cidr_block_association_set = ipv6_cidr_block_association_set

    @property
    def is_default(self):
        """Gets the is_default of this AwsK8sServicesEc2V1alpha1VPCStatus.  # noqa: E501

        Indicates whether the VPC is the default VPC.  # noqa: E501

        :return: The is_default of this AwsK8sServicesEc2V1alpha1VPCStatus.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this AwsK8sServicesEc2V1alpha1VPCStatus.

        Indicates whether the VPC is the default VPC.  # noqa: E501

        :param is_default: The is_default of this AwsK8sServicesEc2V1alpha1VPCStatus.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def owner_id(self):
        """Gets the owner_id of this AwsK8sServicesEc2V1alpha1VPCStatus.  # noqa: E501

        The ID of the Amazon Web Services account that owns the VPC.  # noqa: E501

        :return: The owner_id of this AwsK8sServicesEc2V1alpha1VPCStatus.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this AwsK8sServicesEc2V1alpha1VPCStatus.

        The ID of the Amazon Web Services account that owns the VPC.  # noqa: E501

        :param owner_id: The owner_id of this AwsK8sServicesEc2V1alpha1VPCStatus.  # noqa: E501
        :type: str
        """

        self._owner_id = owner_id

    @property
    def state(self):
        """Gets the state of this AwsK8sServicesEc2V1alpha1VPCStatus.  # noqa: E501

        The current state of the VPC.  # noqa: E501

        :return: The state of this AwsK8sServicesEc2V1alpha1VPCStatus.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AwsK8sServicesEc2V1alpha1VPCStatus.

        The current state of the VPC.  # noqa: E501

        :param state: The state of this AwsK8sServicesEc2V1alpha1VPCStatus.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def vpc_id(self):
        """Gets the vpc_id of this AwsK8sServicesEc2V1alpha1VPCStatus.  # noqa: E501

        The ID of the VPC.  # noqa: E501

        :return: The vpc_id of this AwsK8sServicesEc2V1alpha1VPCStatus.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this AwsK8sServicesEc2V1alpha1VPCStatus.

        The ID of the VPC.  # noqa: E501

        :param vpc_id: The vpc_id of this AwsK8sServicesEc2V1alpha1VPCStatus.  # noqa: E501
        :type: str
        """

        self._vpc_id = vpc_id

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
        if not isinstance(other, AwsK8sServicesEc2V1alpha1VPCStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AwsK8sServicesEc2V1alpha1VPCStatus):
            return True

        return self.to_dict() != other.to_dict()