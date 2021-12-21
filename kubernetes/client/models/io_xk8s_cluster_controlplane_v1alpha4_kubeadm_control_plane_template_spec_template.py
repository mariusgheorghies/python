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


class IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneTemplateSpecTemplate(object):
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
        'spec': 'IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpec'
    }

    attribute_map = {
        'spec': 'spec'
    }

    def __init__(self, spec=None, local_vars_configuration=None):  # noqa: E501
        """IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneTemplateSpecTemplate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._spec = None
        self.discriminator = None

        self.spec = spec

    @property
    def spec(self):
        """Gets the spec of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneTemplateSpecTemplate.  # noqa: E501


        :return: The spec of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneTemplateSpecTemplate.  # noqa: E501
        :rtype: IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpec
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneTemplateSpecTemplate.


        :param spec: The spec of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneTemplateSpecTemplate.  # noqa: E501
        :type: IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpec
        """
        if self.local_vars_configuration.client_side_validation and spec is None:  # noqa: E501
            raise ValueError("Invalid value for `spec`, must not be `None`")  # noqa: E501

        self._spec = spec

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
        if not isinstance(other, IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneTemplateSpecTemplate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneTemplateSpecTemplate):
            return True

        return self.to_dict() != other.to_dict()
