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


class IoXK8sHncV1alpha2HNCConfigurationStatus(object):
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
        'conditions': 'list[IoXK8sHncV1alpha2HNCConfigurationStatusConditions]',
        'resources': 'list[IoXK8sHncV1alpha2HNCConfigurationStatusResources]'
    }

    attribute_map = {
        'conditions': 'conditions',
        'resources': 'resources'
    }

    def __init__(self, conditions=None, resources=None, local_vars_configuration=None):  # noqa: E501
        """IoXK8sHncV1alpha2HNCConfigurationStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._conditions = None
        self._resources = None
        self.discriminator = None

        if conditions is not None:
            self.conditions = conditions
        if resources is not None:
            self.resources = resources

    @property
    def conditions(self):
        """Gets the conditions of this IoXK8sHncV1alpha2HNCConfigurationStatus.  # noqa: E501

        Conditions describes the errors, if any. If there are any conditions with \"ActivitiesHalted\" reason, this means that HNC cannot function in the affected namespaces. The HierarchyConfiguration object in each of the affected namespaces will have more information. To learn more about conditions, see https://github.com/kubernetes-sigs/hierarchical-namespaces/blob/master/docs/user-guide/concepts.md#admin-conditions.  # noqa: E501

        :return: The conditions of this IoXK8sHncV1alpha2HNCConfigurationStatus.  # noqa: E501
        :rtype: list[IoXK8sHncV1alpha2HNCConfigurationStatusConditions]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this IoXK8sHncV1alpha2HNCConfigurationStatus.

        Conditions describes the errors, if any. If there are any conditions with \"ActivitiesHalted\" reason, this means that HNC cannot function in the affected namespaces. The HierarchyConfiguration object in each of the affected namespaces will have more information. To learn more about conditions, see https://github.com/kubernetes-sigs/hierarchical-namespaces/blob/master/docs/user-guide/concepts.md#admin-conditions.  # noqa: E501

        :param conditions: The conditions of this IoXK8sHncV1alpha2HNCConfigurationStatus.  # noqa: E501
        :type: list[IoXK8sHncV1alpha2HNCConfigurationStatusConditions]
        """

        self._conditions = conditions

    @property
    def resources(self):
        """Gets the resources of this IoXK8sHncV1alpha2HNCConfigurationStatus.  # noqa: E501

        Resources indicates the observed synchronization states of the resources.  # noqa: E501

        :return: The resources of this IoXK8sHncV1alpha2HNCConfigurationStatus.  # noqa: E501
        :rtype: list[IoXK8sHncV1alpha2HNCConfigurationStatusResources]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this IoXK8sHncV1alpha2HNCConfigurationStatus.

        Resources indicates the observed synchronization states of the resources.  # noqa: E501

        :param resources: The resources of this IoXK8sHncV1alpha2HNCConfigurationStatus.  # noqa: E501
        :type: list[IoXK8sHncV1alpha2HNCConfigurationStatusResources]
        """

        self._resources = resources

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
        if not isinstance(other, IoXK8sHncV1alpha2HNCConfigurationStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoXK8sHncV1alpha2HNCConfigurationStatus):
            return True

        return self.to_dict() != other.to_dict()
