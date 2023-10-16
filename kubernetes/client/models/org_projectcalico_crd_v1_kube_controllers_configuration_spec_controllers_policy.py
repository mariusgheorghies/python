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


class OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllersPolicy(object):
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
        'reconciler_period': 'str'
    }

    attribute_map = {
        'reconciler_period': 'reconcilerPeriod'
    }

    def __init__(self, reconciler_period=None, local_vars_configuration=None):  # noqa: E501
        """OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllersPolicy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._reconciler_period = None
        self.discriminator = None

        if reconciler_period is not None:
            self.reconciler_period = reconciler_period

    @property
    def reconciler_period(self):
        """Gets the reconciler_period of this OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllersPolicy.  # noqa: E501

        ReconcilerPeriod is the period to perform reconciliation with the Calico datastore. [Default: 5m]  # noqa: E501

        :return: The reconciler_period of this OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllersPolicy.  # noqa: E501
        :rtype: str
        """
        return self._reconciler_period

    @reconciler_period.setter
    def reconciler_period(self, reconciler_period):
        """Sets the reconciler_period of this OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllersPolicy.

        ReconcilerPeriod is the period to perform reconciliation with the Calico datastore. [Default: 5m]  # noqa: E501

        :param reconciler_period: The reconciler_period of this OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllersPolicy.  # noqa: E501
        :type: str
        """

        self._reconciler_period = reconciler_period

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
        if not isinstance(other, OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllersPolicy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllersPolicy):
            return True

        return self.to_dict() != other.to_dict()
