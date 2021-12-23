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


class ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig(object):
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
        'ca': 'ComCoreosMonitoringV1PodMonitorSpecTlsConfigCa',
        'ca_file': 'str',
        'cert': 'ComCoreosMonitoringV1PodMonitorSpecTlsConfigCert',
        'cert_file': 'str',
        'insecure_skip_verify': 'bool',
        'key_file': 'str',
        'key_secret': 'ComCoreosMonitoringV1PodMonitorSpecTlsConfigKeySecret',
        'server_name': 'str'
    }

    attribute_map = {
        'ca': 'ca',
        'ca_file': 'caFile',
        'cert': 'cert',
        'cert_file': 'certFile',
        'insecure_skip_verify': 'insecureSkipVerify',
        'key_file': 'keyFile',
        'key_secret': 'keySecret',
        'server_name': 'serverName'
    }

    def __init__(self, ca=None, ca_file=None, cert=None, cert_file=None, insecure_skip_verify=None, key_file=None, key_secret=None, server_name=None, local_vars_configuration=None):  # noqa: E501
        """ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ca = None
        self._ca_file = None
        self._cert = None
        self._cert_file = None
        self._insecure_skip_verify = None
        self._key_file = None
        self._key_secret = None
        self._server_name = None
        self.discriminator = None

        if ca is not None:
            self.ca = ca
        if ca_file is not None:
            self.ca_file = ca_file
        if cert is not None:
            self.cert = cert
        if cert_file is not None:
            self.cert_file = cert_file
        if insecure_skip_verify is not None:
            self.insecure_skip_verify = insecure_skip_verify
        if key_file is not None:
            self.key_file = key_file
        if key_secret is not None:
            self.key_secret = key_secret
        if server_name is not None:
            self.server_name = server_name

    @property
    def ca(self):
        """Gets the ca of this ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig.  # noqa: E501


        :return: The ca of this ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig.  # noqa: E501
        :rtype: ComCoreosMonitoringV1PodMonitorSpecTlsConfigCa
        """
        return self._ca

    @ca.setter
    def ca(self, ca):
        """Sets the ca of this ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig.


        :param ca: The ca of this ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig.  # noqa: E501
        :type: ComCoreosMonitoringV1PodMonitorSpecTlsConfigCa
        """

        self._ca = ca

    @property
    def ca_file(self):
        """Gets the ca_file of this ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig.  # noqa: E501

        Path to the CA cert in the Prometheus container to use for the targets.  # noqa: E501

        :return: The ca_file of this ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig.  # noqa: E501
        :rtype: str
        """
        return self._ca_file

    @ca_file.setter
    def ca_file(self, ca_file):
        """Sets the ca_file of this ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig.

        Path to the CA cert in the Prometheus container to use for the targets.  # noqa: E501

        :param ca_file: The ca_file of this ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig.  # noqa: E501
        :type: str
        """

        self._ca_file = ca_file

    @property
    def cert(self):
        """Gets the cert of this ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig.  # noqa: E501


        :return: The cert of this ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig.  # noqa: E501
        :rtype: ComCoreosMonitoringV1PodMonitorSpecTlsConfigCert
        """
        return self._cert

    @cert.setter
    def cert(self, cert):
        """Sets the cert of this ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig.


        :param cert: The cert of this ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig.  # noqa: E501
        :type: ComCoreosMonitoringV1PodMonitorSpecTlsConfigCert
        """

        self._cert = cert

    @property
    def cert_file(self):
        """Gets the cert_file of this ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig.  # noqa: E501

        Path to the client cert file in the Prometheus container for the targets.  # noqa: E501

        :return: The cert_file of this ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig.  # noqa: E501
        :rtype: str
        """
        return self._cert_file

    @cert_file.setter
    def cert_file(self, cert_file):
        """Sets the cert_file of this ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig.

        Path to the client cert file in the Prometheus container for the targets.  # noqa: E501

        :param cert_file: The cert_file of this ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig.  # noqa: E501
        :type: str
        """

        self._cert_file = cert_file

    @property
    def insecure_skip_verify(self):
        """Gets the insecure_skip_verify of this ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig.  # noqa: E501

        Disable target certificate validation.  # noqa: E501

        :return: The insecure_skip_verify of this ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig.  # noqa: E501
        :rtype: bool
        """
        return self._insecure_skip_verify

    @insecure_skip_verify.setter
    def insecure_skip_verify(self, insecure_skip_verify):
        """Sets the insecure_skip_verify of this ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig.

        Disable target certificate validation.  # noqa: E501

        :param insecure_skip_verify: The insecure_skip_verify of this ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig.  # noqa: E501
        :type: bool
        """

        self._insecure_skip_verify = insecure_skip_verify

    @property
    def key_file(self):
        """Gets the key_file of this ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig.  # noqa: E501

        Path to the client key file in the Prometheus container for the targets.  # noqa: E501

        :return: The key_file of this ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig.  # noqa: E501
        :rtype: str
        """
        return self._key_file

    @key_file.setter
    def key_file(self, key_file):
        """Sets the key_file of this ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig.

        Path to the client key file in the Prometheus container for the targets.  # noqa: E501

        :param key_file: The key_file of this ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig.  # noqa: E501
        :type: str
        """

        self._key_file = key_file

    @property
    def key_secret(self):
        """Gets the key_secret of this ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig.  # noqa: E501


        :return: The key_secret of this ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig.  # noqa: E501
        :rtype: ComCoreosMonitoringV1PodMonitorSpecTlsConfigKeySecret
        """
        return self._key_secret

    @key_secret.setter
    def key_secret(self, key_secret):
        """Sets the key_secret of this ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig.


        :param key_secret: The key_secret of this ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig.  # noqa: E501
        :type: ComCoreosMonitoringV1PodMonitorSpecTlsConfigKeySecret
        """

        self._key_secret = key_secret

    @property
    def server_name(self):
        """Gets the server_name of this ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig.  # noqa: E501

        Used to verify the hostname for the targets.  # noqa: E501

        :return: The server_name of this ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig.  # noqa: E501
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        """Sets the server_name of this ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig.

        Used to verify the hostname for the targets.  # noqa: E501

        :param server_name: The server_name of this ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig.  # noqa: E501
        :type: str
        """

        self._server_name = server_name

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
        if not isinstance(other, ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig):
            return True

        return self.to_dict() != other.to_dict()
