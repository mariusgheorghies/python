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


class AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules(object):
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
        'from_port': 'int',
        'ip_protocol': 'str',
        'ip_ranges': 'list[AwsK8sServicesEc2V1alpha1SecurityGroupSpecIpRanges]',
        'ipv6_ranges': 'list[AwsK8sServicesEc2V1alpha1SecurityGroupSpecIpv6Ranges]',
        'prefix_list_i_ds': 'list[AwsK8sServicesEc2V1alpha1SecurityGroupSpecPrefixListIDs]',
        'to_port': 'int',
        'user_id_group_pairs': 'list[AwsK8sServicesEc2V1alpha1SecurityGroupSpecUserIDGroupPairs]'
    }

    attribute_map = {
        'from_port': 'fromPort',
        'ip_protocol': 'ipProtocol',
        'ip_ranges': 'ipRanges',
        'ipv6_ranges': 'ipv6Ranges',
        'prefix_list_i_ds': 'prefixListIDs',
        'to_port': 'toPort',
        'user_id_group_pairs': 'userIDGroupPairs'
    }

    def __init__(self, from_port=None, ip_protocol=None, ip_ranges=None, ipv6_ranges=None, prefix_list_i_ds=None, to_port=None, user_id_group_pairs=None, local_vars_configuration=None):  # noqa: E501
        """AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._from_port = None
        self._ip_protocol = None
        self._ip_ranges = None
        self._ipv6_ranges = None
        self._prefix_list_i_ds = None
        self._to_port = None
        self._user_id_group_pairs = None
        self.discriminator = None

        if from_port is not None:
            self.from_port = from_port
        if ip_protocol is not None:
            self.ip_protocol = ip_protocol
        if ip_ranges is not None:
            self.ip_ranges = ip_ranges
        if ipv6_ranges is not None:
            self.ipv6_ranges = ipv6_ranges
        if prefix_list_i_ds is not None:
            self.prefix_list_i_ds = prefix_list_i_ds
        if to_port is not None:
            self.to_port = to_port
        if user_id_group_pairs is not None:
            self.user_id_group_pairs = user_id_group_pairs

    @property
    def from_port(self):
        """Gets the from_port of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules.  # noqa: E501


        :return: The from_port of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules.  # noqa: E501
        :rtype: int
        """
        return self._from_port

    @from_port.setter
    def from_port(self, from_port):
        """Sets the from_port of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules.


        :param from_port: The from_port of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules.  # noqa: E501
        :type: int
        """

        self._from_port = from_port

    @property
    def ip_protocol(self):
        """Gets the ip_protocol of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules.  # noqa: E501


        :return: The ip_protocol of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules.  # noqa: E501
        :rtype: str
        """
        return self._ip_protocol

    @ip_protocol.setter
    def ip_protocol(self, ip_protocol):
        """Sets the ip_protocol of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules.


        :param ip_protocol: The ip_protocol of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules.  # noqa: E501
        :type: str
        """

        self._ip_protocol = ip_protocol

    @property
    def ip_ranges(self):
        """Gets the ip_ranges of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules.  # noqa: E501


        :return: The ip_ranges of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules.  # noqa: E501
        :rtype: list[AwsK8sServicesEc2V1alpha1SecurityGroupSpecIpRanges]
        """
        return self._ip_ranges

    @ip_ranges.setter
    def ip_ranges(self, ip_ranges):
        """Sets the ip_ranges of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules.


        :param ip_ranges: The ip_ranges of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules.  # noqa: E501
        :type: list[AwsK8sServicesEc2V1alpha1SecurityGroupSpecIpRanges]
        """

        self._ip_ranges = ip_ranges

    @property
    def ipv6_ranges(self):
        """Gets the ipv6_ranges of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules.  # noqa: E501


        :return: The ipv6_ranges of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules.  # noqa: E501
        :rtype: list[AwsK8sServicesEc2V1alpha1SecurityGroupSpecIpv6Ranges]
        """
        return self._ipv6_ranges

    @ipv6_ranges.setter
    def ipv6_ranges(self, ipv6_ranges):
        """Sets the ipv6_ranges of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules.


        :param ipv6_ranges: The ipv6_ranges of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules.  # noqa: E501
        :type: list[AwsK8sServicesEc2V1alpha1SecurityGroupSpecIpv6Ranges]
        """

        self._ipv6_ranges = ipv6_ranges

    @property
    def prefix_list_i_ds(self):
        """Gets the prefix_list_i_ds of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules.  # noqa: E501


        :return: The prefix_list_i_ds of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules.  # noqa: E501
        :rtype: list[AwsK8sServicesEc2V1alpha1SecurityGroupSpecPrefixListIDs]
        """
        return self._prefix_list_i_ds

    @prefix_list_i_ds.setter
    def prefix_list_i_ds(self, prefix_list_i_ds):
        """Sets the prefix_list_i_ds of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules.


        :param prefix_list_i_ds: The prefix_list_i_ds of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules.  # noqa: E501
        :type: list[AwsK8sServicesEc2V1alpha1SecurityGroupSpecPrefixListIDs]
        """

        self._prefix_list_i_ds = prefix_list_i_ds

    @property
    def to_port(self):
        """Gets the to_port of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules.  # noqa: E501


        :return: The to_port of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules.  # noqa: E501
        :rtype: int
        """
        return self._to_port

    @to_port.setter
    def to_port(self, to_port):
        """Sets the to_port of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules.


        :param to_port: The to_port of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules.  # noqa: E501
        :type: int
        """

        self._to_port = to_port

    @property
    def user_id_group_pairs(self):
        """Gets the user_id_group_pairs of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules.  # noqa: E501


        :return: The user_id_group_pairs of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules.  # noqa: E501
        :rtype: list[AwsK8sServicesEc2V1alpha1SecurityGroupSpecUserIDGroupPairs]
        """
        return self._user_id_group_pairs

    @user_id_group_pairs.setter
    def user_id_group_pairs(self, user_id_group_pairs):
        """Sets the user_id_group_pairs of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules.


        :param user_id_group_pairs: The user_id_group_pairs of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules.  # noqa: E501
        :type: list[AwsK8sServicesEc2V1alpha1SecurityGroupSpecUserIDGroupPairs]
        """

        self._user_id_group_pairs = user_id_group_pairs

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
        if not isinstance(other, AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules):
            return True

        return self.to_dict() != other.to_dict()