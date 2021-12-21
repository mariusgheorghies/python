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


class IoXK8sClusterInfrastructureV1alpha3AWSFargateProfileSpecSelectors(object):
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
        'labels': 'dict(str, str)',
        'namespace': 'str'
    }

    attribute_map = {
        'labels': 'labels',
        'namespace': 'namespace'
    }

    def __init__(self, labels=None, namespace=None, local_vars_configuration=None):  # noqa: E501
        """IoXK8sClusterInfrastructureV1alpha3AWSFargateProfileSpecSelectors - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._labels = None
        self._namespace = None
        self.discriminator = None

        if labels is not None:
            self.labels = labels
        if namespace is not None:
            self.namespace = namespace

    @property
    def labels(self):
        """Gets the labels of this IoXK8sClusterInfrastructureV1alpha3AWSFargateProfileSpecSelectors.  # noqa: E501

        Labels specifies which pod labels this selector should match.  # noqa: E501

        :return: The labels of this IoXK8sClusterInfrastructureV1alpha3AWSFargateProfileSpecSelectors.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this IoXK8sClusterInfrastructureV1alpha3AWSFargateProfileSpecSelectors.

        Labels specifies which pod labels this selector should match.  # noqa: E501

        :param labels: The labels of this IoXK8sClusterInfrastructureV1alpha3AWSFargateProfileSpecSelectors.  # noqa: E501
        :type: dict(str, str)
        """

        self._labels = labels

    @property
    def namespace(self):
        """Gets the namespace of this IoXK8sClusterInfrastructureV1alpha3AWSFargateProfileSpecSelectors.  # noqa: E501

        Namespace specifies which namespace this selector should match.  # noqa: E501

        :return: The namespace of this IoXK8sClusterInfrastructureV1alpha3AWSFargateProfileSpecSelectors.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this IoXK8sClusterInfrastructureV1alpha3AWSFargateProfileSpecSelectors.

        Namespace specifies which namespace this selector should match.  # noqa: E501

        :param namespace: The namespace of this IoXK8sClusterInfrastructureV1alpha3AWSFargateProfileSpecSelectors.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

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
        if not isinstance(other, IoXK8sClusterInfrastructureV1alpha3AWSFargateProfileSpecSelectors):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoXK8sClusterInfrastructureV1alpha3AWSFargateProfileSpecSelectors):
            return True

        return self.to_dict() != other.to_dict()
