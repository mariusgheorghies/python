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


class ComCoreosMonitoringV1alpha1AlertmanagerConfigSpec(object):
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
        'inhibit_rules': 'list[ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecInhibitRules]',
        'receivers': 'list[ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecReceivers]',
        'route': 'ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecRoute'
    }

    attribute_map = {
        'inhibit_rules': 'inhibitRules',
        'receivers': 'receivers',
        'route': 'route'
    }

    def __init__(self, inhibit_rules=None, receivers=None, route=None, local_vars_configuration=None):  # noqa: E501
        """ComCoreosMonitoringV1alpha1AlertmanagerConfigSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._inhibit_rules = None
        self._receivers = None
        self._route = None
        self.discriminator = None

        if inhibit_rules is not None:
            self.inhibit_rules = inhibit_rules
        if receivers is not None:
            self.receivers = receivers
        if route is not None:
            self.route = route

    @property
    def inhibit_rules(self):
        """Gets the inhibit_rules of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpec.  # noqa: E501

        List of inhibition rules. The rules will only apply to alerts matching the resource’s namespace.  # noqa: E501

        :return: The inhibit_rules of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpec.  # noqa: E501
        :rtype: list[ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecInhibitRules]
        """
        return self._inhibit_rules

    @inhibit_rules.setter
    def inhibit_rules(self, inhibit_rules):
        """Sets the inhibit_rules of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpec.

        List of inhibition rules. The rules will only apply to alerts matching the resource’s namespace.  # noqa: E501

        :param inhibit_rules: The inhibit_rules of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpec.  # noqa: E501
        :type: list[ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecInhibitRules]
        """

        self._inhibit_rules = inhibit_rules

    @property
    def receivers(self):
        """Gets the receivers of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpec.  # noqa: E501

        List of receivers.  # noqa: E501

        :return: The receivers of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpec.  # noqa: E501
        :rtype: list[ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecReceivers]
        """
        return self._receivers

    @receivers.setter
    def receivers(self, receivers):
        """Sets the receivers of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpec.

        List of receivers.  # noqa: E501

        :param receivers: The receivers of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpec.  # noqa: E501
        :type: list[ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecReceivers]
        """

        self._receivers = receivers

    @property
    def route(self):
        """Gets the route of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpec.  # noqa: E501


        :return: The route of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpec.  # noqa: E501
        :rtype: ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecRoute
        """
        return self._route

    @route.setter
    def route(self, route):
        """Sets the route of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpec.


        :param route: The route of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpec.  # noqa: E501
        :type: ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecRoute
        """

        self._route = route

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
        if not isinstance(other, ComCoreosMonitoringV1alpha1AlertmanagerConfigSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComCoreosMonitoringV1alpha1AlertmanagerConfigSpec):
            return True

        return self.to_dict() != other.to_dict()
