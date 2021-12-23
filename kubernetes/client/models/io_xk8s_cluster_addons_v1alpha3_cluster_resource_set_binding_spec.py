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


class IoXK8sClusterAddonsV1alpha3ClusterResourceSetBindingSpec(object):
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
        'bindings': 'list[IoXK8sClusterAddonsV1alpha3ClusterResourceSetBindingSpecBindings]'
    }

    attribute_map = {
        'bindings': 'bindings'
    }

    def __init__(self, bindings=None, local_vars_configuration=None):  # noqa: E501
        """IoXK8sClusterAddonsV1alpha3ClusterResourceSetBindingSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._bindings = None
        self.discriminator = None

        if bindings is not None:
            self.bindings = bindings

    @property
    def bindings(self):
        """Gets the bindings of this IoXK8sClusterAddonsV1alpha3ClusterResourceSetBindingSpec.  # noqa: E501

        Bindings is a list of ClusterResourceSets and their resources.  # noqa: E501

        :return: The bindings of this IoXK8sClusterAddonsV1alpha3ClusterResourceSetBindingSpec.  # noqa: E501
        :rtype: list[IoXK8sClusterAddonsV1alpha3ClusterResourceSetBindingSpecBindings]
        """
        return self._bindings

    @bindings.setter
    def bindings(self, bindings):
        """Sets the bindings of this IoXK8sClusterAddonsV1alpha3ClusterResourceSetBindingSpec.

        Bindings is a list of ClusterResourceSets and their resources.  # noqa: E501

        :param bindings: The bindings of this IoXK8sClusterAddonsV1alpha3ClusterResourceSetBindingSpec.  # noqa: E501
        :type: list[IoXK8sClusterAddonsV1alpha3ClusterResourceSetBindingSpecBindings]
        """

        self._bindings = bindings

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
        if not isinstance(other, IoXK8sClusterAddonsV1alpha3ClusterResourceSetBindingSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoXK8sClusterAddonsV1alpha3ClusterResourceSetBindingSpec):
            return True

        return self.to_dict() != other.to_dict()
