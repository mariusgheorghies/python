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


class ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings(object):
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
        'action': 'str',
        'modulus': 'int',
        'regex': 'str',
        'replacement': 'str',
        'separator': 'str',
        'source_labels': 'list[str]',
        'target_label': 'str'
    }

    attribute_map = {
        'action': 'action',
        'modulus': 'modulus',
        'regex': 'regex',
        'replacement': 'replacement',
        'separator': 'separator',
        'source_labels': 'sourceLabels',
        'target_label': 'targetLabel'
    }

    def __init__(self, action=None, modulus=None, regex=None, replacement=None, separator=None, source_labels=None, target_label=None, local_vars_configuration=None):  # noqa: E501
        """ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._action = None
        self._modulus = None
        self._regex = None
        self._replacement = None
        self._separator = None
        self._source_labels = None
        self._target_label = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if modulus is not None:
            self.modulus = modulus
        if regex is not None:
            self.regex = regex
        if replacement is not None:
            self.replacement = replacement
        if separator is not None:
            self.separator = separator
        if source_labels is not None:
            self.source_labels = source_labels
        if target_label is not None:
            self.target_label = target_label

    @property
    def action(self):
        """Gets the action of this ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.  # noqa: E501

        Action to perform based on regex matching. Default is 'replace'. uppercase and lowercase actions require Prometheus >= 2.36.  # noqa: E501

        :return: The action of this ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.

        Action to perform based on regex matching. Default is 'replace'. uppercase and lowercase actions require Prometheus >= 2.36.  # noqa: E501

        :param action: The action of this ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.  # noqa: E501
        :type: str
        """
        allowed_values = ["replace", "Replace", "keep", "Keep", "drop", "Drop", "hashmod", "HashMod", "labelmap", "LabelMap", "labeldrop", "LabelDrop", "labelkeep", "LabelKeep", "lowercase", "Lowercase", "uppercase", "Uppercase"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and action not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def modulus(self):
        """Gets the modulus of this ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.  # noqa: E501

        Modulus to take of the hash of the source label values.  # noqa: E501

        :return: The modulus of this ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.  # noqa: E501
        :rtype: int
        """
        return self._modulus

    @modulus.setter
    def modulus(self, modulus):
        """Sets the modulus of this ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.

        Modulus to take of the hash of the source label values.  # noqa: E501

        :param modulus: The modulus of this ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.  # noqa: E501
        :type: int
        """

        self._modulus = modulus

    @property
    def regex(self):
        """Gets the regex of this ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.  # noqa: E501

        Regular expression against which the extracted value is matched. Default is '(.*)'  # noqa: E501

        :return: The regex of this ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.  # noqa: E501
        :rtype: str
        """
        return self._regex

    @regex.setter
    def regex(self, regex):
        """Sets the regex of this ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.

        Regular expression against which the extracted value is matched. Default is '(.*)'  # noqa: E501

        :param regex: The regex of this ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.  # noqa: E501
        :type: str
        """

        self._regex = regex

    @property
    def replacement(self):
        """Gets the replacement of this ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.  # noqa: E501

        Replacement value against which a regex replace is performed if the regular expression matches. Regex capture groups are available. Default is '$1'  # noqa: E501

        :return: The replacement of this ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.  # noqa: E501
        :rtype: str
        """
        return self._replacement

    @replacement.setter
    def replacement(self, replacement):
        """Sets the replacement of this ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.

        Replacement value against which a regex replace is performed if the regular expression matches. Regex capture groups are available. Default is '$1'  # noqa: E501

        :param replacement: The replacement of this ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.  # noqa: E501
        :type: str
        """

        self._replacement = replacement

    @property
    def separator(self):
        """Gets the separator of this ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.  # noqa: E501

        Separator placed between concatenated source label values. default is ';'.  # noqa: E501

        :return: The separator of this ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.  # noqa: E501
        :rtype: str
        """
        return self._separator

    @separator.setter
    def separator(self, separator):
        """Sets the separator of this ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.

        Separator placed between concatenated source label values. default is ';'.  # noqa: E501

        :param separator: The separator of this ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.  # noqa: E501
        :type: str
        """

        self._separator = separator

    @property
    def source_labels(self):
        """Gets the source_labels of this ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.  # noqa: E501

        The source labels select values from existing labels. Their content is concatenated using the configured separator and matched against the configured regular expression for the replace, keep, and drop actions.  # noqa: E501

        :return: The source_labels of this ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.  # noqa: E501
        :rtype: list[str]
        """
        return self._source_labels

    @source_labels.setter
    def source_labels(self, source_labels):
        """Sets the source_labels of this ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.

        The source labels select values from existing labels. Their content is concatenated using the configured separator and matched against the configured regular expression for the replace, keep, and drop actions.  # noqa: E501

        :param source_labels: The source_labels of this ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.  # noqa: E501
        :type: list[str]
        """

        self._source_labels = source_labels

    @property
    def target_label(self):
        """Gets the target_label of this ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.  # noqa: E501

        Label to which the resulting value is written in a replace action. It is mandatory for replace actions. Regex capture groups are available.  # noqa: E501

        :return: The target_label of this ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.  # noqa: E501
        :rtype: str
        """
        return self._target_label

    @target_label.setter
    def target_label(self, target_label):
        """Sets the target_label of this ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.

        Label to which the resulting value is written in a replace action. It is mandatory for replace actions. Regex capture groups are available.  # noqa: E501

        :param target_label: The target_label of this ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.  # noqa: E501
        :type: str
        """

        self._target_label = target_label

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
        if not isinstance(other, ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings):
            return True

        return self.to_dict() != other.to_dict()