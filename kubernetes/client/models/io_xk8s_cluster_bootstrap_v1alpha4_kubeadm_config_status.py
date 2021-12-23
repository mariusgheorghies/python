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


class IoXK8sClusterBootstrapV1alpha4KubeadmConfigStatus(object):
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
        'conditions': 'list[IoXK8sClusterAddonsV1alpha3ClusterResourceSetStatusConditions]',
        'data_secret_name': 'str',
        'failure_message': 'str',
        'failure_reason': 'str',
        'observed_generation': 'int',
        'ready': 'bool'
    }

    attribute_map = {
        'conditions': 'conditions',
        'data_secret_name': 'dataSecretName',
        'failure_message': 'failureMessage',
        'failure_reason': 'failureReason',
        'observed_generation': 'observedGeneration',
        'ready': 'ready'
    }

    def __init__(self, conditions=None, data_secret_name=None, failure_message=None, failure_reason=None, observed_generation=None, ready=None, local_vars_configuration=None):  # noqa: E501
        """IoXK8sClusterBootstrapV1alpha4KubeadmConfigStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._conditions = None
        self._data_secret_name = None
        self._failure_message = None
        self._failure_reason = None
        self._observed_generation = None
        self._ready = None
        self.discriminator = None

        if conditions is not None:
            self.conditions = conditions
        if data_secret_name is not None:
            self.data_secret_name = data_secret_name
        if failure_message is not None:
            self.failure_message = failure_message
        if failure_reason is not None:
            self.failure_reason = failure_reason
        if observed_generation is not None:
            self.observed_generation = observed_generation
        if ready is not None:
            self.ready = ready

    @property
    def conditions(self):
        """Gets the conditions of this IoXK8sClusterBootstrapV1alpha4KubeadmConfigStatus.  # noqa: E501

        Conditions defines current service state of the KubeadmConfig.  # noqa: E501

        :return: The conditions of this IoXK8sClusterBootstrapV1alpha4KubeadmConfigStatus.  # noqa: E501
        :rtype: list[IoXK8sClusterAddonsV1alpha3ClusterResourceSetStatusConditions]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this IoXK8sClusterBootstrapV1alpha4KubeadmConfigStatus.

        Conditions defines current service state of the KubeadmConfig.  # noqa: E501

        :param conditions: The conditions of this IoXK8sClusterBootstrapV1alpha4KubeadmConfigStatus.  # noqa: E501
        :type: list[IoXK8sClusterAddonsV1alpha3ClusterResourceSetStatusConditions]
        """

        self._conditions = conditions

    @property
    def data_secret_name(self):
        """Gets the data_secret_name of this IoXK8sClusterBootstrapV1alpha4KubeadmConfigStatus.  # noqa: E501

        DataSecretName is the name of the secret that stores the bootstrap data script.  # noqa: E501

        :return: The data_secret_name of this IoXK8sClusterBootstrapV1alpha4KubeadmConfigStatus.  # noqa: E501
        :rtype: str
        """
        return self._data_secret_name

    @data_secret_name.setter
    def data_secret_name(self, data_secret_name):
        """Sets the data_secret_name of this IoXK8sClusterBootstrapV1alpha4KubeadmConfigStatus.

        DataSecretName is the name of the secret that stores the bootstrap data script.  # noqa: E501

        :param data_secret_name: The data_secret_name of this IoXK8sClusterBootstrapV1alpha4KubeadmConfigStatus.  # noqa: E501
        :type: str
        """

        self._data_secret_name = data_secret_name

    @property
    def failure_message(self):
        """Gets the failure_message of this IoXK8sClusterBootstrapV1alpha4KubeadmConfigStatus.  # noqa: E501

        FailureMessage will be set on non-retryable errors  # noqa: E501

        :return: The failure_message of this IoXK8sClusterBootstrapV1alpha4KubeadmConfigStatus.  # noqa: E501
        :rtype: str
        """
        return self._failure_message

    @failure_message.setter
    def failure_message(self, failure_message):
        """Sets the failure_message of this IoXK8sClusterBootstrapV1alpha4KubeadmConfigStatus.

        FailureMessage will be set on non-retryable errors  # noqa: E501

        :param failure_message: The failure_message of this IoXK8sClusterBootstrapV1alpha4KubeadmConfigStatus.  # noqa: E501
        :type: str
        """

        self._failure_message = failure_message

    @property
    def failure_reason(self):
        """Gets the failure_reason of this IoXK8sClusterBootstrapV1alpha4KubeadmConfigStatus.  # noqa: E501

        FailureReason will be set on non-retryable errors  # noqa: E501

        :return: The failure_reason of this IoXK8sClusterBootstrapV1alpha4KubeadmConfigStatus.  # noqa: E501
        :rtype: str
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """Sets the failure_reason of this IoXK8sClusterBootstrapV1alpha4KubeadmConfigStatus.

        FailureReason will be set on non-retryable errors  # noqa: E501

        :param failure_reason: The failure_reason of this IoXK8sClusterBootstrapV1alpha4KubeadmConfigStatus.  # noqa: E501
        :type: str
        """

        self._failure_reason = failure_reason

    @property
    def observed_generation(self):
        """Gets the observed_generation of this IoXK8sClusterBootstrapV1alpha4KubeadmConfigStatus.  # noqa: E501

        ObservedGeneration is the latest generation observed by the controller.  # noqa: E501

        :return: The observed_generation of this IoXK8sClusterBootstrapV1alpha4KubeadmConfigStatus.  # noqa: E501
        :rtype: int
        """
        return self._observed_generation

    @observed_generation.setter
    def observed_generation(self, observed_generation):
        """Sets the observed_generation of this IoXK8sClusterBootstrapV1alpha4KubeadmConfigStatus.

        ObservedGeneration is the latest generation observed by the controller.  # noqa: E501

        :param observed_generation: The observed_generation of this IoXK8sClusterBootstrapV1alpha4KubeadmConfigStatus.  # noqa: E501
        :type: int
        """

        self._observed_generation = observed_generation

    @property
    def ready(self):
        """Gets the ready of this IoXK8sClusterBootstrapV1alpha4KubeadmConfigStatus.  # noqa: E501

        Ready indicates the BootstrapData field is ready to be consumed  # noqa: E501

        :return: The ready of this IoXK8sClusterBootstrapV1alpha4KubeadmConfigStatus.  # noqa: E501
        :rtype: bool
        """
        return self._ready

    @ready.setter
    def ready(self, ready):
        """Sets the ready of this IoXK8sClusterBootstrapV1alpha4KubeadmConfigStatus.

        Ready indicates the BootstrapData field is ready to be consumed  # noqa: E501

        :param ready: The ready of this IoXK8sClusterBootstrapV1alpha4KubeadmConfigStatus.  # noqa: E501
        :type: bool
        """

        self._ready = ready

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
        if not isinstance(other, IoXK8sClusterBootstrapV1alpha4KubeadmConfigStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoXK8sClusterBootstrapV1alpha4KubeadmConfigStatus):
            return True

        return self.to_dict() != other.to_dict()
