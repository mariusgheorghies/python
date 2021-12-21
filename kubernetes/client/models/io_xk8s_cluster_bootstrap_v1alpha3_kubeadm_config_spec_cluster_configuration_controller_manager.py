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


class IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationControllerManager(object):
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
        'extra_args': 'dict(str, str)',
        'extra_volumes': 'list[IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationApiServerExtraVolumes]'
    }

    attribute_map = {
        'extra_args': 'extraArgs',
        'extra_volumes': 'extraVolumes'
    }

    def __init__(self, extra_args=None, extra_volumes=None, local_vars_configuration=None):  # noqa: E501
        """IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationControllerManager - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._extra_args = None
        self._extra_volumes = None
        self.discriminator = None

        if extra_args is not None:
            self.extra_args = extra_args
        if extra_volumes is not None:
            self.extra_volumes = extra_volumes

    @property
    def extra_args(self):
        """Gets the extra_args of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationControllerManager.  # noqa: E501

        ExtraArgs is an extra set of flags to pass to the control plane component. TODO: This is temporary and ideally we would like to switch all components to use ComponentConfig + ConfigMaps.  # noqa: E501

        :return: The extra_args of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationControllerManager.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._extra_args

    @extra_args.setter
    def extra_args(self, extra_args):
        """Sets the extra_args of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationControllerManager.

        ExtraArgs is an extra set of flags to pass to the control plane component. TODO: This is temporary and ideally we would like to switch all components to use ComponentConfig + ConfigMaps.  # noqa: E501

        :param extra_args: The extra_args of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationControllerManager.  # noqa: E501
        :type: dict(str, str)
        """

        self._extra_args = extra_args

    @property
    def extra_volumes(self):
        """Gets the extra_volumes of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationControllerManager.  # noqa: E501

        ExtraVolumes is an extra set of host volumes, mounted to the control plane component.  # noqa: E501

        :return: The extra_volumes of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationControllerManager.  # noqa: E501
        :rtype: list[IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationApiServerExtraVolumes]
        """
        return self._extra_volumes

    @extra_volumes.setter
    def extra_volumes(self, extra_volumes):
        """Sets the extra_volumes of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationControllerManager.

        ExtraVolumes is an extra set of host volumes, mounted to the control plane component.  # noqa: E501

        :param extra_volumes: The extra_volumes of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationControllerManager.  # noqa: E501
        :type: list[IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationApiServerExtraVolumes]
        """

        self._extra_volumes = extra_volumes

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
        if not isinstance(other, IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationControllerManager):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationControllerManager):
            return True

        return self.to_dict() != other.to_dict()
