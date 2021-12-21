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


class ComCoreosMonitoringV1PodMonitorSpecTlsConfigCa(object):
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
        'config_map': 'ComCoreosMonitoringV1PodMonitorSpecOauth2ClientIdConfigMap',
        'secret': 'ComCoreosMonitoringV1PodMonitorSpecOauth2ClientIdSecret'
    }

    attribute_map = {
        'config_map': 'configMap',
        'secret': 'secret'
    }

    def __init__(self, config_map=None, secret=None, local_vars_configuration=None):  # noqa: E501
        """ComCoreosMonitoringV1PodMonitorSpecTlsConfigCa - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._config_map = None
        self._secret = None
        self.discriminator = None

        if config_map is not None:
            self.config_map = config_map
        if secret is not None:
            self.secret = secret

    @property
    def config_map(self):
        """Gets the config_map of this ComCoreosMonitoringV1PodMonitorSpecTlsConfigCa.  # noqa: E501


        :return: The config_map of this ComCoreosMonitoringV1PodMonitorSpecTlsConfigCa.  # noqa: E501
        :rtype: ComCoreosMonitoringV1PodMonitorSpecOauth2ClientIdConfigMap
        """
        return self._config_map

    @config_map.setter
    def config_map(self, config_map):
        """Sets the config_map of this ComCoreosMonitoringV1PodMonitorSpecTlsConfigCa.


        :param config_map: The config_map of this ComCoreosMonitoringV1PodMonitorSpecTlsConfigCa.  # noqa: E501
        :type: ComCoreosMonitoringV1PodMonitorSpecOauth2ClientIdConfigMap
        """

        self._config_map = config_map

    @property
    def secret(self):
        """Gets the secret of this ComCoreosMonitoringV1PodMonitorSpecTlsConfigCa.  # noqa: E501


        :return: The secret of this ComCoreosMonitoringV1PodMonitorSpecTlsConfigCa.  # noqa: E501
        :rtype: ComCoreosMonitoringV1PodMonitorSpecOauth2ClientIdSecret
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this ComCoreosMonitoringV1PodMonitorSpecTlsConfigCa.


        :param secret: The secret of this ComCoreosMonitoringV1PodMonitorSpecTlsConfigCa.  # noqa: E501
        :type: ComCoreosMonitoringV1PodMonitorSpecOauth2ClientIdSecret
        """

        self._secret = secret

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
        if not isinstance(other, ComCoreosMonitoringV1PodMonitorSpecTlsConfigCa):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComCoreosMonitoringV1PodMonitorSpecTlsConfigCa):
            return True

        return self.to_dict() != other.to_dict()
