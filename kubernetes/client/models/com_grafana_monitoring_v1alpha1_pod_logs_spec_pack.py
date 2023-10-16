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


class ComGrafanaMonitoringV1alpha1PodLogsSpecPack(object):
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
        'ingest_timestamp': 'bool',
        'labels': 'list[str]'
    }

    attribute_map = {
        'ingest_timestamp': 'ingestTimestamp',
        'labels': 'labels'
    }

    def __init__(self, ingest_timestamp=None, labels=None, local_vars_configuration=None):  # noqa: E501
        """ComGrafanaMonitoringV1alpha1PodLogsSpecPack - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ingest_timestamp = None
        self._labels = None
        self.discriminator = None

        if ingest_timestamp is not None:
            self.ingest_timestamp = ingest_timestamp
        self.labels = labels

    @property
    def ingest_timestamp(self):
        """Gets the ingest_timestamp of this ComGrafanaMonitoringV1alpha1PodLogsSpecPack.  # noqa: E501

        If the resulting log line should use any existing timestamp or use time.Now() when the line was created. Set to true when combining several log streams from different containers to avoid out of order errors.  # noqa: E501

        :return: The ingest_timestamp of this ComGrafanaMonitoringV1alpha1PodLogsSpecPack.  # noqa: E501
        :rtype: bool
        """
        return self._ingest_timestamp

    @ingest_timestamp.setter
    def ingest_timestamp(self, ingest_timestamp):
        """Sets the ingest_timestamp of this ComGrafanaMonitoringV1alpha1PodLogsSpecPack.

        If the resulting log line should use any existing timestamp or use time.Now() when the line was created. Set to true when combining several log streams from different containers to avoid out of order errors.  # noqa: E501

        :param ingest_timestamp: The ingest_timestamp of this ComGrafanaMonitoringV1alpha1PodLogsSpecPack.  # noqa: E501
        :type: bool
        """

        self._ingest_timestamp = ingest_timestamp

    @property
    def labels(self):
        """Gets the labels of this ComGrafanaMonitoringV1alpha1PodLogsSpecPack.  # noqa: E501

        Name from extracted data or line labels. Required. Labels provided here are automatically removed from output labels.  # noqa: E501

        :return: The labels of this ComGrafanaMonitoringV1alpha1PodLogsSpecPack.  # noqa: E501
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this ComGrafanaMonitoringV1alpha1PodLogsSpecPack.

        Name from extracted data or line labels. Required. Labels provided here are automatically removed from output labels.  # noqa: E501

        :param labels: The labels of this ComGrafanaMonitoringV1alpha1PodLogsSpecPack.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and labels is None:  # noqa: E501
            raise ValueError("Invalid value for `labels`, must not be `None`")  # noqa: E501

        self._labels = labels

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
        if not isinstance(other, ComGrafanaMonitoringV1alpha1PodLogsSpecPack):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComGrafanaMonitoringV1alpha1PodLogsSpecPack):
            return True

        return self.to_dict() != other.to_dict()