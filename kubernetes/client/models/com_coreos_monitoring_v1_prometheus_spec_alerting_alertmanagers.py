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


class ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers(object):
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
        'api_version': 'str',
        'authorization': 'ComCoreosMonitoringV1PrometheusSpecAlertingAuthorization',
        'bearer_token_file': 'str',
        'name': 'str',
        'namespace': 'str',
        'path_prefix': 'str',
        'port': 'object',
        'scheme': 'str',
        'timeout': 'str',
        'tls_config': 'ComCoreosMonitoringV1PrometheusSpecAlertingTlsConfig'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'authorization': 'authorization',
        'bearer_token_file': 'bearerTokenFile',
        'name': 'name',
        'namespace': 'namespace',
        'path_prefix': 'pathPrefix',
        'port': 'port',
        'scheme': 'scheme',
        'timeout': 'timeout',
        'tls_config': 'tlsConfig'
    }

    def __init__(self, api_version=None, authorization=None, bearer_token_file=None, name=None, namespace=None, path_prefix=None, port=None, scheme=None, timeout=None, tls_config=None, local_vars_configuration=None):  # noqa: E501
        """ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._api_version = None
        self._authorization = None
        self._bearer_token_file = None
        self._name = None
        self._namespace = None
        self._path_prefix = None
        self._port = None
        self._scheme = None
        self._timeout = None
        self._tls_config = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if authorization is not None:
            self.authorization = authorization
        if bearer_token_file is not None:
            self.bearer_token_file = bearer_token_file
        self.name = name
        self.namespace = namespace
        if path_prefix is not None:
            self.path_prefix = path_prefix
        self.port = port
        if scheme is not None:
            self.scheme = scheme
        if timeout is not None:
            self.timeout = timeout
        if tls_config is not None:
            self.tls_config = tls_config

    @property
    def api_version(self):
        """Gets the api_version of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.  # noqa: E501

        Version of the Alertmanager API that Prometheus uses to send alerts. It can be \"v1\" or \"v2\".  # noqa: E501

        :return: The api_version of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.

        Version of the Alertmanager API that Prometheus uses to send alerts. It can be \"v1\" or \"v2\".  # noqa: E501

        :param api_version: The api_version of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def authorization(self):
        """Gets the authorization of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.  # noqa: E501


        :return: The authorization of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.  # noqa: E501
        :rtype: ComCoreosMonitoringV1PrometheusSpecAlertingAuthorization
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """Sets the authorization of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.


        :param authorization: The authorization of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.  # noqa: E501
        :type: ComCoreosMonitoringV1PrometheusSpecAlertingAuthorization
        """

        self._authorization = authorization

    @property
    def bearer_token_file(self):
        """Gets the bearer_token_file of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.  # noqa: E501

        BearerTokenFile to read from filesystem to use when authenticating to Alertmanager.  # noqa: E501

        :return: The bearer_token_file of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.  # noqa: E501
        :rtype: str
        """
        return self._bearer_token_file

    @bearer_token_file.setter
    def bearer_token_file(self, bearer_token_file):
        """Sets the bearer_token_file of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.

        BearerTokenFile to read from filesystem to use when authenticating to Alertmanager.  # noqa: E501

        :param bearer_token_file: The bearer_token_file of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.  # noqa: E501
        :type: str
        """

        self._bearer_token_file = bearer_token_file

    @property
    def name(self):
        """Gets the name of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.  # noqa: E501

        Name of Endpoints object in Namespace.  # noqa: E501

        :return: The name of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.

        Name of Endpoints object in Namespace.  # noqa: E501

        :param name: The name of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.  # noqa: E501

        Namespace of Endpoints object.  # noqa: E501

        :return: The namespace of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.

        Namespace of Endpoints object.  # noqa: E501

        :param namespace: The namespace of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and namespace is None:  # noqa: E501
            raise ValueError("Invalid value for `namespace`, must not be `None`")  # noqa: E501

        self._namespace = namespace

    @property
    def path_prefix(self):
        """Gets the path_prefix of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.  # noqa: E501

        Prefix for the HTTP path alerts are pushed to.  # noqa: E501

        :return: The path_prefix of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.  # noqa: E501
        :rtype: str
        """
        return self._path_prefix

    @path_prefix.setter
    def path_prefix(self, path_prefix):
        """Sets the path_prefix of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.

        Prefix for the HTTP path alerts are pushed to.  # noqa: E501

        :param path_prefix: The path_prefix of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.  # noqa: E501
        :type: str
        """

        self._path_prefix = path_prefix

    @property
    def port(self):
        """Gets the port of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.  # noqa: E501

        Port the Alertmanager API is exposed on.  # noqa: E501

        :return: The port of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.  # noqa: E501
        :rtype: object
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.

        Port the Alertmanager API is exposed on.  # noqa: E501

        :param port: The port of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and port is None:  # noqa: E501
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def scheme(self):
        """Gets the scheme of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.  # noqa: E501

        Scheme to use when firing alerts.  # noqa: E501

        :return: The scheme of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.  # noqa: E501
        :rtype: str
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        """Sets the scheme of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.

        Scheme to use when firing alerts.  # noqa: E501

        :param scheme: The scheme of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.  # noqa: E501
        :type: str
        """

        self._scheme = scheme

    @property
    def timeout(self):
        """Gets the timeout of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.  # noqa: E501

        Timeout is a per-target Alertmanager timeout when pushing alerts.  # noqa: E501

        :return: The timeout of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.  # noqa: E501
        :rtype: str
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.

        Timeout is a per-target Alertmanager timeout when pushing alerts.  # noqa: E501

        :param timeout: The timeout of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.  # noqa: E501
        :type: str
        """

        self._timeout = timeout

    @property
    def tls_config(self):
        """Gets the tls_config of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.  # noqa: E501


        :return: The tls_config of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.  # noqa: E501
        :rtype: ComCoreosMonitoringV1PrometheusSpecAlertingTlsConfig
        """
        return self._tls_config

    @tls_config.setter
    def tls_config(self, tls_config):
        """Sets the tls_config of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.


        :param tls_config: The tls_config of this ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers.  # noqa: E501
        :type: ComCoreosMonitoringV1PrometheusSpecAlertingTlsConfig
        """

        self._tls_config = tls_config

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
        if not isinstance(other, ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers):
            return True

        return self.to_dict() != other.to_dict()
