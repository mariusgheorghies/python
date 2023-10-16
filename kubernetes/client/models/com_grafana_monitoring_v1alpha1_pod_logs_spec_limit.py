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


class ComGrafanaMonitoringV1alpha1PodLogsSpecLimit(object):
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
        'burst': 'int',
        'drop': 'bool',
        'rate': 'int'
    }

    attribute_map = {
        'burst': 'burst',
        'drop': 'drop',
        'rate': 'rate'
    }

    def __init__(self, burst=None, drop=None, rate=None, local_vars_configuration=None):  # noqa: E501
        """ComGrafanaMonitoringV1alpha1PodLogsSpecLimit - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._burst = None
        self._drop = None
        self._rate = None
        self.discriminator = None

        if burst is not None:
            self.burst = burst
        if drop is not None:
            self.drop = drop
        if rate is not None:
            self.rate = rate

    @property
    def burst(self):
        """Gets the burst of this ComGrafanaMonitoringV1alpha1PodLogsSpecLimit.  # noqa: E501

        The cap in the quantity of burst lines that Promtail will push to Loki.  # noqa: E501

        :return: The burst of this ComGrafanaMonitoringV1alpha1PodLogsSpecLimit.  # noqa: E501
        :rtype: int
        """
        return self._burst

    @burst.setter
    def burst(self, burst):
        """Sets the burst of this ComGrafanaMonitoringV1alpha1PodLogsSpecLimit.

        The cap in the quantity of burst lines that Promtail will push to Loki.  # noqa: E501

        :param burst: The burst of this ComGrafanaMonitoringV1alpha1PodLogsSpecLimit.  # noqa: E501
        :type: int
        """

        self._burst = burst

    @property
    def drop(self):
        """Gets the drop of this ComGrafanaMonitoringV1alpha1PodLogsSpecLimit.  # noqa: E501

        When drop is true, log lines that exceed the current rate limit are discarded. When drop is false, log lines that exceed the current rate limit wait to enter the back pressure mode.   Defaults to false.  # noqa: E501

        :return: The drop of this ComGrafanaMonitoringV1alpha1PodLogsSpecLimit.  # noqa: E501
        :rtype: bool
        """
        return self._drop

    @drop.setter
    def drop(self, drop):
        """Sets the drop of this ComGrafanaMonitoringV1alpha1PodLogsSpecLimit.

        When drop is true, log lines that exceed the current rate limit are discarded. When drop is false, log lines that exceed the current rate limit wait to enter the back pressure mode.   Defaults to false.  # noqa: E501

        :param drop: The drop of this ComGrafanaMonitoringV1alpha1PodLogsSpecLimit.  # noqa: E501
        :type: bool
        """

        self._drop = drop

    @property
    def rate(self):
        """Gets the rate of this ComGrafanaMonitoringV1alpha1PodLogsSpecLimit.  # noqa: E501

        The rate limit in lines per second that Promtail will push to Loki.  # noqa: E501

        :return: The rate of this ComGrafanaMonitoringV1alpha1PodLogsSpecLimit.  # noqa: E501
        :rtype: int
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this ComGrafanaMonitoringV1alpha1PodLogsSpecLimit.

        The rate limit in lines per second that Promtail will push to Loki.  # noqa: E501

        :param rate: The rate of this ComGrafanaMonitoringV1alpha1PodLogsSpecLimit.  # noqa: E501
        :type: int
        """

        self._rate = rate

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
        if not isinstance(other, ComGrafanaMonitoringV1alpha1PodLogsSpecLimit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComGrafanaMonitoringV1alpha1PodLogsSpecLimit):
            return True

        return self.to_dict() != other.to_dict()