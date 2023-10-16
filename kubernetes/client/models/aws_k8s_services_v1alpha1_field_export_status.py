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


class AwsK8sServicesV1alpha1FieldExportStatus(object):
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
        'conditions': 'list[AwsK8sServicesEc2V1alpha1DHCPOptionsStatusConditions]'
    }

    attribute_map = {
        'conditions': 'conditions'
    }

    def __init__(self, conditions=None, local_vars_configuration=None):  # noqa: E501
        """AwsK8sServicesV1alpha1FieldExportStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._conditions = None
        self.discriminator = None

        self.conditions = conditions

    @property
    def conditions(self):
        """Gets the conditions of this AwsK8sServicesV1alpha1FieldExportStatus.  # noqa: E501

        A collection of `ackv1alpha1.Condition` objects that describe the various recoverable states of the field CR  # noqa: E501

        :return: The conditions of this AwsK8sServicesV1alpha1FieldExportStatus.  # noqa: E501
        :rtype: list[AwsK8sServicesEc2V1alpha1DHCPOptionsStatusConditions]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this AwsK8sServicesV1alpha1FieldExportStatus.

        A collection of `ackv1alpha1.Condition` objects that describe the various recoverable states of the field CR  # noqa: E501

        :param conditions: The conditions of this AwsK8sServicesV1alpha1FieldExportStatus.  # noqa: E501
        :type: list[AwsK8sServicesEc2V1alpha1DHCPOptionsStatusConditions]
        """
        if self.local_vars_configuration.client_side_validation and conditions is None:  # noqa: E501
            raise ValueError("Invalid value for `conditions`, must not be `None`")  # noqa: E501

        self._conditions = conditions

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
        if not isinstance(other, AwsK8sServicesV1alpha1FieldExportStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AwsK8sServicesV1alpha1FieldExportStatus):
            return True

        return self.to_dict() != other.to_dict()
