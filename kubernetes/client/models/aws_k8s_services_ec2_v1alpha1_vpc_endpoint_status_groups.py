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


class AwsK8sServicesEc2V1alpha1VPCEndpointStatusGroups(object):
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
        'group_id': 'str',
        'group_name': 'str'
    }

    attribute_map = {
        'group_id': 'groupID',
        'group_name': 'groupName'
    }

    def __init__(self, group_id=None, group_name=None, local_vars_configuration=None):  # noqa: E501
        """AwsK8sServicesEc2V1alpha1VPCEndpointStatusGroups - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._group_id = None
        self._group_name = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name

    @property
    def group_id(self):
        """Gets the group_id of this AwsK8sServicesEc2V1alpha1VPCEndpointStatusGroups.  # noqa: E501


        :return: The group_id of this AwsK8sServicesEc2V1alpha1VPCEndpointStatusGroups.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this AwsK8sServicesEc2V1alpha1VPCEndpointStatusGroups.


        :param group_id: The group_id of this AwsK8sServicesEc2V1alpha1VPCEndpointStatusGroups.  # noqa: E501
        :type: str
        """

        self._group_id = group_id

    @property
    def group_name(self):
        """Gets the group_name of this AwsK8sServicesEc2V1alpha1VPCEndpointStatusGroups.  # noqa: E501


        :return: The group_name of this AwsK8sServicesEc2V1alpha1VPCEndpointStatusGroups.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this AwsK8sServicesEc2V1alpha1VPCEndpointStatusGroups.


        :param group_name: The group_name of this AwsK8sServicesEc2V1alpha1VPCEndpointStatusGroups.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

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
        if not isinstance(other, AwsK8sServicesEc2V1alpha1VPCEndpointStatusGroups):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AwsK8sServicesEc2V1alpha1VPCEndpointStatusGroups):
            return True

        return self.to_dict() != other.to_dict()