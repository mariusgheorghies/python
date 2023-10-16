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


class AwsK8sServicesEc2V1alpha1SecurityGroupSpecIpRanges(object):
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
        'cidr_ip': 'str',
        'description': 'str'
    }

    attribute_map = {
        'cidr_ip': 'cidrIP',
        'description': 'description'
    }

    def __init__(self, cidr_ip=None, description=None, local_vars_configuration=None):  # noqa: E501
        """AwsK8sServicesEc2V1alpha1SecurityGroupSpecIpRanges - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cidr_ip = None
        self._description = None
        self.discriminator = None

        if cidr_ip is not None:
            self.cidr_ip = cidr_ip
        if description is not None:
            self.description = description

    @property
    def cidr_ip(self):
        """Gets the cidr_ip of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecIpRanges.  # noqa: E501


        :return: The cidr_ip of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecIpRanges.  # noqa: E501
        :rtype: str
        """
        return self._cidr_ip

    @cidr_ip.setter
    def cidr_ip(self, cidr_ip):
        """Sets the cidr_ip of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecIpRanges.


        :param cidr_ip: The cidr_ip of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecIpRanges.  # noqa: E501
        :type: str
        """

        self._cidr_ip = cidr_ip

    @property
    def description(self):
        """Gets the description of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecIpRanges.  # noqa: E501


        :return: The description of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecIpRanges.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecIpRanges.


        :param description: The description of this AwsK8sServicesEc2V1alpha1SecurityGroupSpecIpRanges.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if not isinstance(other, AwsK8sServicesEc2V1alpha1SecurityGroupSpecIpRanges):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AwsK8sServicesEc2V1alpha1SecurityGroupSpecIpRanges):
            return True

        return self.to_dict() != other.to_dict()