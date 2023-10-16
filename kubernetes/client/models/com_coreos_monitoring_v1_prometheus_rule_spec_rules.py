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


class ComCoreosMonitoringV1PrometheusRuleSpecRules(object):
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
        'alert': 'str',
        'annotations': 'dict(str, str)',
        'expr': 'object',
        '_for': 'str',
        'labels': 'dict(str, str)',
        'record': 'str'
    }

    attribute_map = {
        'alert': 'alert',
        'annotations': 'annotations',
        'expr': 'expr',
        '_for': 'for',
        'labels': 'labels',
        'record': 'record'
    }

    def __init__(self, alert=None, annotations=None, expr=None, _for=None, labels=None, record=None, local_vars_configuration=None):  # noqa: E501
        """ComCoreosMonitoringV1PrometheusRuleSpecRules - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._alert = None
        self._annotations = None
        self._expr = None
        self.__for = None
        self._labels = None
        self._record = None
        self.discriminator = None

        if alert is not None:
            self.alert = alert
        if annotations is not None:
            self.annotations = annotations
        self.expr = expr
        if _for is not None:
            self._for = _for
        if labels is not None:
            self.labels = labels
        if record is not None:
            self.record = record

    @property
    def alert(self):
        """Gets the alert of this ComCoreosMonitoringV1PrometheusRuleSpecRules.  # noqa: E501


        :return: The alert of this ComCoreosMonitoringV1PrometheusRuleSpecRules.  # noqa: E501
        :rtype: str
        """
        return self._alert

    @alert.setter
    def alert(self, alert):
        """Sets the alert of this ComCoreosMonitoringV1PrometheusRuleSpecRules.


        :param alert: The alert of this ComCoreosMonitoringV1PrometheusRuleSpecRules.  # noqa: E501
        :type: str
        """

        self._alert = alert

    @property
    def annotations(self):
        """Gets the annotations of this ComCoreosMonitoringV1PrometheusRuleSpecRules.  # noqa: E501


        :return: The annotations of this ComCoreosMonitoringV1PrometheusRuleSpecRules.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this ComCoreosMonitoringV1PrometheusRuleSpecRules.


        :param annotations: The annotations of this ComCoreosMonitoringV1PrometheusRuleSpecRules.  # noqa: E501
        :type: dict(str, str)
        """

        self._annotations = annotations

    @property
    def expr(self):
        """Gets the expr of this ComCoreosMonitoringV1PrometheusRuleSpecRules.  # noqa: E501


        :return: The expr of this ComCoreosMonitoringV1PrometheusRuleSpecRules.  # noqa: E501
        :rtype: object
        """
        return self._expr

    @expr.setter
    def expr(self, expr):
        """Sets the expr of this ComCoreosMonitoringV1PrometheusRuleSpecRules.


        :param expr: The expr of this ComCoreosMonitoringV1PrometheusRuleSpecRules.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and expr is None:  # noqa: E501
            raise ValueError("Invalid value for `expr`, must not be `None`")  # noqa: E501

        self._expr = expr

    @property
    def _for(self):
        """Gets the _for of this ComCoreosMonitoringV1PrometheusRuleSpecRules.  # noqa: E501


        :return: The _for of this ComCoreosMonitoringV1PrometheusRuleSpecRules.  # noqa: E501
        :rtype: str
        """
        return self.__for

    @_for.setter
    def _for(self, _for):
        """Sets the _for of this ComCoreosMonitoringV1PrometheusRuleSpecRules.


        :param _for: The _for of this ComCoreosMonitoringV1PrometheusRuleSpecRules.  # noqa: E501
        :type: str
        """

        self.__for = _for

    @property
    def labels(self):
        """Gets the labels of this ComCoreosMonitoringV1PrometheusRuleSpecRules.  # noqa: E501


        :return: The labels of this ComCoreosMonitoringV1PrometheusRuleSpecRules.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this ComCoreosMonitoringV1PrometheusRuleSpecRules.


        :param labels: The labels of this ComCoreosMonitoringV1PrometheusRuleSpecRules.  # noqa: E501
        :type: dict(str, str)
        """

        self._labels = labels

    @property
    def record(self):
        """Gets the record of this ComCoreosMonitoringV1PrometheusRuleSpecRules.  # noqa: E501


        :return: The record of this ComCoreosMonitoringV1PrometheusRuleSpecRules.  # noqa: E501
        :rtype: str
        """
        return self._record

    @record.setter
    def record(self, record):
        """Sets the record of this ComCoreosMonitoringV1PrometheusRuleSpecRules.


        :param record: The record of this ComCoreosMonitoringV1PrometheusRuleSpecRules.  # noqa: E501
        :type: str
        """

        self._record = record

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
        if not isinstance(other, ComCoreosMonitoringV1PrometheusRuleSpecRules):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComCoreosMonitoringV1PrometheusRuleSpecRules):
            return True

        return self.to_dict() != other.to_dict()
