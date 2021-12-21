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


class IoXK8sClusterV1beta1ClusterStatus(object):
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
        'conditions': 'list[IoXK8sClusterAddonsV1beta1ClusterResourceSetStatusConditions]',
        'control_plane_ready': 'bool',
        'failure_domains': 'dict(str, IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusFailureDomains)',
        'failure_message': 'str',
        'failure_reason': 'str',
        'infrastructure_ready': 'bool',
        'observed_generation': 'int',
        'phase': 'str'
    }

    attribute_map = {
        'conditions': 'conditions',
        'control_plane_ready': 'controlPlaneReady',
        'failure_domains': 'failureDomains',
        'failure_message': 'failureMessage',
        'failure_reason': 'failureReason',
        'infrastructure_ready': 'infrastructureReady',
        'observed_generation': 'observedGeneration',
        'phase': 'phase'
    }

    def __init__(self, conditions=None, control_plane_ready=None, failure_domains=None, failure_message=None, failure_reason=None, infrastructure_ready=None, observed_generation=None, phase=None, local_vars_configuration=None):  # noqa: E501
        """IoXK8sClusterV1beta1ClusterStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._conditions = None
        self._control_plane_ready = None
        self._failure_domains = None
        self._failure_message = None
        self._failure_reason = None
        self._infrastructure_ready = None
        self._observed_generation = None
        self._phase = None
        self.discriminator = None

        if conditions is not None:
            self.conditions = conditions
        if control_plane_ready is not None:
            self.control_plane_ready = control_plane_ready
        if failure_domains is not None:
            self.failure_domains = failure_domains
        if failure_message is not None:
            self.failure_message = failure_message
        if failure_reason is not None:
            self.failure_reason = failure_reason
        if infrastructure_ready is not None:
            self.infrastructure_ready = infrastructure_ready
        if observed_generation is not None:
            self.observed_generation = observed_generation
        if phase is not None:
            self.phase = phase

    @property
    def conditions(self):
        """Gets the conditions of this IoXK8sClusterV1beta1ClusterStatus.  # noqa: E501

        Conditions defines current service state of the cluster.  # noqa: E501

        :return: The conditions of this IoXK8sClusterV1beta1ClusterStatus.  # noqa: E501
        :rtype: list[IoXK8sClusterAddonsV1beta1ClusterResourceSetStatusConditions]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this IoXK8sClusterV1beta1ClusterStatus.

        Conditions defines current service state of the cluster.  # noqa: E501

        :param conditions: The conditions of this IoXK8sClusterV1beta1ClusterStatus.  # noqa: E501
        :type: list[IoXK8sClusterAddonsV1beta1ClusterResourceSetStatusConditions]
        """

        self._conditions = conditions

    @property
    def control_plane_ready(self):
        """Gets the control_plane_ready of this IoXK8sClusterV1beta1ClusterStatus.  # noqa: E501

        ControlPlaneReady defines if the control plane is ready.  # noqa: E501

        :return: The control_plane_ready of this IoXK8sClusterV1beta1ClusterStatus.  # noqa: E501
        :rtype: bool
        """
        return self._control_plane_ready

    @control_plane_ready.setter
    def control_plane_ready(self, control_plane_ready):
        """Sets the control_plane_ready of this IoXK8sClusterV1beta1ClusterStatus.

        ControlPlaneReady defines if the control plane is ready.  # noqa: E501

        :param control_plane_ready: The control_plane_ready of this IoXK8sClusterV1beta1ClusterStatus.  # noqa: E501
        :type: bool
        """

        self._control_plane_ready = control_plane_ready

    @property
    def failure_domains(self):
        """Gets the failure_domains of this IoXK8sClusterV1beta1ClusterStatus.  # noqa: E501

        FailureDomains is a slice of failure domain objects synced from the infrastructure provider.  # noqa: E501

        :return: The failure_domains of this IoXK8sClusterV1beta1ClusterStatus.  # noqa: E501
        :rtype: dict(str, IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusFailureDomains)
        """
        return self._failure_domains

    @failure_domains.setter
    def failure_domains(self, failure_domains):
        """Sets the failure_domains of this IoXK8sClusterV1beta1ClusterStatus.

        FailureDomains is a slice of failure domain objects synced from the infrastructure provider.  # noqa: E501

        :param failure_domains: The failure_domains of this IoXK8sClusterV1beta1ClusterStatus.  # noqa: E501
        :type: dict(str, IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusFailureDomains)
        """

        self._failure_domains = failure_domains

    @property
    def failure_message(self):
        """Gets the failure_message of this IoXK8sClusterV1beta1ClusterStatus.  # noqa: E501

        FailureMessage indicates that there is a fatal problem reconciling the state, and will be set to a descriptive error message.  # noqa: E501

        :return: The failure_message of this IoXK8sClusterV1beta1ClusterStatus.  # noqa: E501
        :rtype: str
        """
        return self._failure_message

    @failure_message.setter
    def failure_message(self, failure_message):
        """Sets the failure_message of this IoXK8sClusterV1beta1ClusterStatus.

        FailureMessage indicates that there is a fatal problem reconciling the state, and will be set to a descriptive error message.  # noqa: E501

        :param failure_message: The failure_message of this IoXK8sClusterV1beta1ClusterStatus.  # noqa: E501
        :type: str
        """

        self._failure_message = failure_message

    @property
    def failure_reason(self):
        """Gets the failure_reason of this IoXK8sClusterV1beta1ClusterStatus.  # noqa: E501

        FailureReason indicates that there is a fatal problem reconciling the state, and will be set to a token value suitable for programmatic interpretation.  # noqa: E501

        :return: The failure_reason of this IoXK8sClusterV1beta1ClusterStatus.  # noqa: E501
        :rtype: str
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """Sets the failure_reason of this IoXK8sClusterV1beta1ClusterStatus.

        FailureReason indicates that there is a fatal problem reconciling the state, and will be set to a token value suitable for programmatic interpretation.  # noqa: E501

        :param failure_reason: The failure_reason of this IoXK8sClusterV1beta1ClusterStatus.  # noqa: E501
        :type: str
        """

        self._failure_reason = failure_reason

    @property
    def infrastructure_ready(self):
        """Gets the infrastructure_ready of this IoXK8sClusterV1beta1ClusterStatus.  # noqa: E501

        InfrastructureReady is the state of the infrastructure provider.  # noqa: E501

        :return: The infrastructure_ready of this IoXK8sClusterV1beta1ClusterStatus.  # noqa: E501
        :rtype: bool
        """
        return self._infrastructure_ready

    @infrastructure_ready.setter
    def infrastructure_ready(self, infrastructure_ready):
        """Sets the infrastructure_ready of this IoXK8sClusterV1beta1ClusterStatus.

        InfrastructureReady is the state of the infrastructure provider.  # noqa: E501

        :param infrastructure_ready: The infrastructure_ready of this IoXK8sClusterV1beta1ClusterStatus.  # noqa: E501
        :type: bool
        """

        self._infrastructure_ready = infrastructure_ready

    @property
    def observed_generation(self):
        """Gets the observed_generation of this IoXK8sClusterV1beta1ClusterStatus.  # noqa: E501

        ObservedGeneration is the latest generation observed by the controller.  # noqa: E501

        :return: The observed_generation of this IoXK8sClusterV1beta1ClusterStatus.  # noqa: E501
        :rtype: int
        """
        return self._observed_generation

    @observed_generation.setter
    def observed_generation(self, observed_generation):
        """Sets the observed_generation of this IoXK8sClusterV1beta1ClusterStatus.

        ObservedGeneration is the latest generation observed by the controller.  # noqa: E501

        :param observed_generation: The observed_generation of this IoXK8sClusterV1beta1ClusterStatus.  # noqa: E501
        :type: int
        """

        self._observed_generation = observed_generation

    @property
    def phase(self):
        """Gets the phase of this IoXK8sClusterV1beta1ClusterStatus.  # noqa: E501

        Phase represents the current phase of cluster actuation. E.g. Pending, Running, Terminating, Failed etc.  # noqa: E501

        :return: The phase of this IoXK8sClusterV1beta1ClusterStatus.  # noqa: E501
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this IoXK8sClusterV1beta1ClusterStatus.

        Phase represents the current phase of cluster actuation. E.g. Pending, Running, Terminating, Failed etc.  # noqa: E501

        :param phase: The phase of this IoXK8sClusterV1beta1ClusterStatus.  # noqa: E501
        :type: str
        """

        self._phase = phase

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
        if not isinstance(other, IoXK8sClusterV1beta1ClusterStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoXK8sClusterV1beta1ClusterStatus):
            return True

        return self.to_dict() != other.to_dict()
