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


class ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe(object):
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
        '_exec': 'ComCoreosMonitoringV1AlertmanagerSpecLifecyclePostStartExec',
        'failure_threshold': 'int',
        'grpc': 'ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbeGrpc',
        'http_get': 'ComCoreosMonitoringV1AlertmanagerSpecLifecyclePostStartHttpGet',
        'initial_delay_seconds': 'int',
        'period_seconds': 'int',
        'success_threshold': 'int',
        'tcp_socket': 'ComCoreosMonitoringV1AlertmanagerSpecLivenessProbeTcpSocket',
        'termination_grace_period_seconds': 'int',
        'timeout_seconds': 'int'
    }

    attribute_map = {
        '_exec': 'exec',
        'failure_threshold': 'failureThreshold',
        'grpc': 'grpc',
        'http_get': 'httpGet',
        'initial_delay_seconds': 'initialDelaySeconds',
        'period_seconds': 'periodSeconds',
        'success_threshold': 'successThreshold',
        'tcp_socket': 'tcpSocket',
        'termination_grace_period_seconds': 'terminationGracePeriodSeconds',
        'timeout_seconds': 'timeoutSeconds'
    }

    def __init__(self, _exec=None, failure_threshold=None, grpc=None, http_get=None, initial_delay_seconds=None, period_seconds=None, success_threshold=None, tcp_socket=None, termination_grace_period_seconds=None, timeout_seconds=None, local_vars_configuration=None):  # noqa: E501
        """ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self.__exec = None
        self._failure_threshold = None
        self._grpc = None
        self._http_get = None
        self._initial_delay_seconds = None
        self._period_seconds = None
        self._success_threshold = None
        self._tcp_socket = None
        self._termination_grace_period_seconds = None
        self._timeout_seconds = None
        self.discriminator = None

        if _exec is not None:
            self._exec = _exec
        if failure_threshold is not None:
            self.failure_threshold = failure_threshold
        if grpc is not None:
            self.grpc = grpc
        if http_get is not None:
            self.http_get = http_get
        if initial_delay_seconds is not None:
            self.initial_delay_seconds = initial_delay_seconds
        if period_seconds is not None:
            self.period_seconds = period_seconds
        if success_threshold is not None:
            self.success_threshold = success_threshold
        if tcp_socket is not None:
            self.tcp_socket = tcp_socket
        if termination_grace_period_seconds is not None:
            self.termination_grace_period_seconds = termination_grace_period_seconds
        if timeout_seconds is not None:
            self.timeout_seconds = timeout_seconds

    @property
    def _exec(self):
        """Gets the _exec of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.  # noqa: E501


        :return: The _exec of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.  # noqa: E501
        :rtype: ComCoreosMonitoringV1AlertmanagerSpecLifecyclePostStartExec
        """
        return self.__exec

    @_exec.setter
    def _exec(self, _exec):
        """Sets the _exec of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.


        :param _exec: The _exec of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.  # noqa: E501
        :type: ComCoreosMonitoringV1AlertmanagerSpecLifecyclePostStartExec
        """

        self.__exec = _exec

    @property
    def failure_threshold(self):
        """Gets the failure_threshold of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.  # noqa: E501

        Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.  # noqa: E501

        :return: The failure_threshold of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.  # noqa: E501
        :rtype: int
        """
        return self._failure_threshold

    @failure_threshold.setter
    def failure_threshold(self, failure_threshold):
        """Sets the failure_threshold of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.

        Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.  # noqa: E501

        :param failure_threshold: The failure_threshold of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.  # noqa: E501
        :type: int
        """

        self._failure_threshold = failure_threshold

    @property
    def grpc(self):
        """Gets the grpc of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.  # noqa: E501


        :return: The grpc of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.  # noqa: E501
        :rtype: ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbeGrpc
        """
        return self._grpc

    @grpc.setter
    def grpc(self, grpc):
        """Sets the grpc of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.


        :param grpc: The grpc of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.  # noqa: E501
        :type: ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbeGrpc
        """

        self._grpc = grpc

    @property
    def http_get(self):
        """Gets the http_get of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.  # noqa: E501


        :return: The http_get of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.  # noqa: E501
        :rtype: ComCoreosMonitoringV1AlertmanagerSpecLifecyclePostStartHttpGet
        """
        return self._http_get

    @http_get.setter
    def http_get(self, http_get):
        """Sets the http_get of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.


        :param http_get: The http_get of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.  # noqa: E501
        :type: ComCoreosMonitoringV1AlertmanagerSpecLifecyclePostStartHttpGet
        """

        self._http_get = http_get

    @property
    def initial_delay_seconds(self):
        """Gets the initial_delay_seconds of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.  # noqa: E501

        Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes  # noqa: E501

        :return: The initial_delay_seconds of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.  # noqa: E501
        :rtype: int
        """
        return self._initial_delay_seconds

    @initial_delay_seconds.setter
    def initial_delay_seconds(self, initial_delay_seconds):
        """Sets the initial_delay_seconds of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.

        Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes  # noqa: E501

        :param initial_delay_seconds: The initial_delay_seconds of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.  # noqa: E501
        :type: int
        """

        self._initial_delay_seconds = initial_delay_seconds

    @property
    def period_seconds(self):
        """Gets the period_seconds of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.  # noqa: E501

        How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.  # noqa: E501

        :return: The period_seconds of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.  # noqa: E501
        :rtype: int
        """
        return self._period_seconds

    @period_seconds.setter
    def period_seconds(self, period_seconds):
        """Sets the period_seconds of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.

        How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.  # noqa: E501

        :param period_seconds: The period_seconds of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.  # noqa: E501
        :type: int
        """

        self._period_seconds = period_seconds

    @property
    def success_threshold(self):
        """Gets the success_threshold of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.  # noqa: E501

        Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.  # noqa: E501

        :return: The success_threshold of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.  # noqa: E501
        :rtype: int
        """
        return self._success_threshold

    @success_threshold.setter
    def success_threshold(self, success_threshold):
        """Sets the success_threshold of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.

        Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.  # noqa: E501

        :param success_threshold: The success_threshold of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.  # noqa: E501
        :type: int
        """

        self._success_threshold = success_threshold

    @property
    def tcp_socket(self):
        """Gets the tcp_socket of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.  # noqa: E501


        :return: The tcp_socket of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.  # noqa: E501
        :rtype: ComCoreosMonitoringV1AlertmanagerSpecLivenessProbeTcpSocket
        """
        return self._tcp_socket

    @tcp_socket.setter
    def tcp_socket(self, tcp_socket):
        """Sets the tcp_socket of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.


        :param tcp_socket: The tcp_socket of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.  # noqa: E501
        :type: ComCoreosMonitoringV1AlertmanagerSpecLivenessProbeTcpSocket
        """

        self._tcp_socket = tcp_socket

    @property
    def termination_grace_period_seconds(self):
        """Gets the termination_grace_period_seconds of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.  # noqa: E501

        Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod's terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset.  # noqa: E501

        :return: The termination_grace_period_seconds of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.  # noqa: E501
        :rtype: int
        """
        return self._termination_grace_period_seconds

    @termination_grace_period_seconds.setter
    def termination_grace_period_seconds(self, termination_grace_period_seconds):
        """Sets the termination_grace_period_seconds of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.

        Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod's terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset.  # noqa: E501

        :param termination_grace_period_seconds: The termination_grace_period_seconds of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.  # noqa: E501
        :type: int
        """

        self._termination_grace_period_seconds = termination_grace_period_seconds

    @property
    def timeout_seconds(self):
        """Gets the timeout_seconds of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.  # noqa: E501

        Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes  # noqa: E501

        :return: The timeout_seconds of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.  # noqa: E501
        :rtype: int
        """
        return self._timeout_seconds

    @timeout_seconds.setter
    def timeout_seconds(self, timeout_seconds):
        """Sets the timeout_seconds of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.

        Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes  # noqa: E501

        :param timeout_seconds: The timeout_seconds of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe.  # noqa: E501
        :type: int
        """

        self._timeout_seconds = timeout_seconds

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
        if not isinstance(other, ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLivenessProbe):
            return True

        return self.to_dict() != other.to_dict()
