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


class ComGrafanaMonitoringV1alpha1PodLogsSpecRegex(object):
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
        'expression': 'str',
        'source': 'str'
    }

    attribute_map = {
        'expression': 'expression',
        'source': 'source'
    }

    def __init__(self, expression=None, source=None, local_vars_configuration=None):  # noqa: E501
        """ComGrafanaMonitoringV1alpha1PodLogsSpecRegex - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._expression = None
        self._source = None
        self.discriminator = None

        self.expression = expression
        if source is not None:
            self.source = source

    @property
    def expression(self):
        """Gets the expression of this ComGrafanaMonitoringV1alpha1PodLogsSpecRegex.  # noqa: E501

        RE2 regular expression. Each capture group MUST be named. Required.  # noqa: E501

        :return: The expression of this ComGrafanaMonitoringV1alpha1PodLogsSpecRegex.  # noqa: E501
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this ComGrafanaMonitoringV1alpha1PodLogsSpecRegex.

        RE2 regular expression. Each capture group MUST be named. Required.  # noqa: E501

        :param expression: The expression of this ComGrafanaMonitoringV1alpha1PodLogsSpecRegex.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and expression is None:  # noqa: E501
            raise ValueError("Invalid value for `expression`, must not be `None`")  # noqa: E501

        self._expression = expression

    @property
    def source(self):
        """Gets the source of this ComGrafanaMonitoringV1alpha1PodLogsSpecRegex.  # noqa: E501

        Name from extracted data to parse. If empty, defaults to using the log message.  # noqa: E501

        :return: The source of this ComGrafanaMonitoringV1alpha1PodLogsSpecRegex.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ComGrafanaMonitoringV1alpha1PodLogsSpecRegex.

        Name from extracted data to parse. If empty, defaults to using the log message.  # noqa: E501

        :param source: The source of this ComGrafanaMonitoringV1alpha1PodLogsSpecRegex.  # noqa: E501
        :type: str
        """

        self._source = source

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
        if not isinstance(other, ComGrafanaMonitoringV1alpha1PodLogsSpecRegex):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComGrafanaMonitoringV1alpha1PodLogsSpecRegex):
            return True

        return self.to_dict() != other.to_dict()
