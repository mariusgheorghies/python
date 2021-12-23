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


class IoXK8sClusterV1alpha4ClusterClassSpecWorkersTemplateMetadata(object):
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
        'annotations': 'dict(str, str)',
        'labels': 'dict(str, str)'
    }

    attribute_map = {
        'annotations': 'annotations',
        'labels': 'labels'
    }

    def __init__(self, annotations=None, labels=None, local_vars_configuration=None):  # noqa: E501
        """IoXK8sClusterV1alpha4ClusterClassSpecWorkersTemplateMetadata - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._annotations = None
        self._labels = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        if labels is not None:
            self.labels = labels

    @property
    def annotations(self):
        """Gets the annotations of this IoXK8sClusterV1alpha4ClusterClassSpecWorkersTemplateMetadata.  # noqa: E501

        Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: http://kubernetes.io/docs/user-guide/annotations  # noqa: E501

        :return: The annotations of this IoXK8sClusterV1alpha4ClusterClassSpecWorkersTemplateMetadata.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this IoXK8sClusterV1alpha4ClusterClassSpecWorkersTemplateMetadata.

        Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: http://kubernetes.io/docs/user-guide/annotations  # noqa: E501

        :param annotations: The annotations of this IoXK8sClusterV1alpha4ClusterClassSpecWorkersTemplateMetadata.  # noqa: E501
        :type: dict(str, str)
        """

        self._annotations = annotations

    @property
    def labels(self):
        """Gets the labels of this IoXK8sClusterV1alpha4ClusterClassSpecWorkersTemplateMetadata.  # noqa: E501

        Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels  # noqa: E501

        :return: The labels of this IoXK8sClusterV1alpha4ClusterClassSpecWorkersTemplateMetadata.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this IoXK8sClusterV1alpha4ClusterClassSpecWorkersTemplateMetadata.

        Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels  # noqa: E501

        :param labels: The labels of this IoXK8sClusterV1alpha4ClusterClassSpecWorkersTemplateMetadata.  # noqa: E501
        :type: dict(str, str)
        """

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
        if not isinstance(other, IoXK8sClusterV1alpha4ClusterClassSpecWorkersTemplateMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoXK8sClusterV1alpha4ClusterClassSpecWorkersTemplateMetadata):
            return True

        return self.to_dict() != other.to_dict()
