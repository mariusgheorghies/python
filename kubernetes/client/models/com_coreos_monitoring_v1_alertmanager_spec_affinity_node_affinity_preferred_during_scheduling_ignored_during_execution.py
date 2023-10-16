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


class ComCoreosMonitoringV1AlertmanagerSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecution(object):
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
        'preference': 'ComCoreosMonitoringV1AlertmanagerSpecAffinityNodeAffinityPreference',
        'weight': 'int'
    }

    attribute_map = {
        'preference': 'preference',
        'weight': 'weight'
    }

    def __init__(self, preference=None, weight=None, local_vars_configuration=None):  # noqa: E501
        """ComCoreosMonitoringV1AlertmanagerSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecution - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._preference = None
        self._weight = None
        self.discriminator = None

        self.preference = preference
        self.weight = weight

    @property
    def preference(self):
        """Gets the preference of this ComCoreosMonitoringV1AlertmanagerSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecution.  # noqa: E501


        :return: The preference of this ComCoreosMonitoringV1AlertmanagerSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecution.  # noqa: E501
        :rtype: ComCoreosMonitoringV1AlertmanagerSpecAffinityNodeAffinityPreference
        """
        return self._preference

    @preference.setter
    def preference(self, preference):
        """Sets the preference of this ComCoreosMonitoringV1AlertmanagerSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecution.


        :param preference: The preference of this ComCoreosMonitoringV1AlertmanagerSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecution.  # noqa: E501
        :type: ComCoreosMonitoringV1AlertmanagerSpecAffinityNodeAffinityPreference
        """
        if self.local_vars_configuration.client_side_validation and preference is None:  # noqa: E501
            raise ValueError("Invalid value for `preference`, must not be `None`")  # noqa: E501

        self._preference = preference

    @property
    def weight(self):
        """Gets the weight of this ComCoreosMonitoringV1AlertmanagerSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecution.  # noqa: E501

        Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100.  # noqa: E501

        :return: The weight of this ComCoreosMonitoringV1AlertmanagerSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecution.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this ComCoreosMonitoringV1AlertmanagerSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecution.

        Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100.  # noqa: E501

        :param weight: The weight of this ComCoreosMonitoringV1AlertmanagerSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecution.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and weight is None:  # noqa: E501
            raise ValueError("Invalid value for `weight`, must not be `None`")  # noqa: E501

        self._weight = weight

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
        if not isinstance(other, ComCoreosMonitoringV1AlertmanagerSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecution):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComCoreosMonitoringV1AlertmanagerSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecution):
            return True

        return self.to_dict() != other.to_dict()