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


class OrgProjectcalicoCrdV1KubeControllersConfigurationStatus(object):
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
        'environment_vars': 'dict(str, str)',
        'running_config': 'OrgProjectcalicoCrdV1KubeControllersConfigurationStatusRunningConfig'
    }

    attribute_map = {
        'environment_vars': 'environmentVars',
        'running_config': 'runningConfig'
    }

    def __init__(self, environment_vars=None, running_config=None, local_vars_configuration=None):  # noqa: E501
        """OrgProjectcalicoCrdV1KubeControllersConfigurationStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._environment_vars = None
        self._running_config = None
        self.discriminator = None

        if environment_vars is not None:
            self.environment_vars = environment_vars
        if running_config is not None:
            self.running_config = running_config

    @property
    def environment_vars(self):
        """Gets the environment_vars of this OrgProjectcalicoCrdV1KubeControllersConfigurationStatus.  # noqa: E501

        EnvironmentVars contains the environment variables on the kube-controllers that influenced the RunningConfig.  # noqa: E501

        :return: The environment_vars of this OrgProjectcalicoCrdV1KubeControllersConfigurationStatus.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._environment_vars

    @environment_vars.setter
    def environment_vars(self, environment_vars):
        """Sets the environment_vars of this OrgProjectcalicoCrdV1KubeControllersConfigurationStatus.

        EnvironmentVars contains the environment variables on the kube-controllers that influenced the RunningConfig.  # noqa: E501

        :param environment_vars: The environment_vars of this OrgProjectcalicoCrdV1KubeControllersConfigurationStatus.  # noqa: E501
        :type: dict(str, str)
        """

        self._environment_vars = environment_vars

    @property
    def running_config(self):
        """Gets the running_config of this OrgProjectcalicoCrdV1KubeControllersConfigurationStatus.  # noqa: E501


        :return: The running_config of this OrgProjectcalicoCrdV1KubeControllersConfigurationStatus.  # noqa: E501
        :rtype: OrgProjectcalicoCrdV1KubeControllersConfigurationStatusRunningConfig
        """
        return self._running_config

    @running_config.setter
    def running_config(self, running_config):
        """Sets the running_config of this OrgProjectcalicoCrdV1KubeControllersConfigurationStatus.


        :param running_config: The running_config of this OrgProjectcalicoCrdV1KubeControllersConfigurationStatus.  # noqa: E501
        :type: OrgProjectcalicoCrdV1KubeControllersConfigurationStatusRunningConfig
        """

        self._running_config = running_config

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
        if not isinstance(other, OrgProjectcalicoCrdV1KubeControllersConfigurationStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrgProjectcalicoCrdV1KubeControllersConfigurationStatus):
            return True

        return self.to_dict() != other.to_dict()