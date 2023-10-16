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


class IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook(object):
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
        'body': 'str',
        'ca_bundle': 'str',
        'ca_provider': 'IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhookCaProvider',
        'headers': 'dict(str, str)',
        'method': 'str',
        'result': 'IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhookResult',
        'secrets': 'list[IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhookSecrets]',
        'timeout': 'str',
        'url': 'str'
    }

    attribute_map = {
        'body': 'body',
        'ca_bundle': 'caBundle',
        'ca_provider': 'caProvider',
        'headers': 'headers',
        'method': 'method',
        'result': 'result',
        'secrets': 'secrets',
        'timeout': 'timeout',
        'url': 'url'
    }

    def __init__(self, body=None, ca_bundle=None, ca_provider=None, headers=None, method=None, result=None, secrets=None, timeout=None, url=None, local_vars_configuration=None):  # noqa: E501
        """IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._body = None
        self._ca_bundle = None
        self._ca_provider = None
        self._headers = None
        self._method = None
        self._result = None
        self._secrets = None
        self._timeout = None
        self._url = None
        self.discriminator = None

        if body is not None:
            self.body = body
        if ca_bundle is not None:
            self.ca_bundle = ca_bundle
        if ca_provider is not None:
            self.ca_provider = ca_provider
        if headers is not None:
            self.headers = headers
        if method is not None:
            self.method = method
        self.result = result
        if secrets is not None:
            self.secrets = secrets
        if timeout is not None:
            self.timeout = timeout
        self.url = url

    @property
    def body(self):
        """Gets the body of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.  # noqa: E501

        Body  # noqa: E501

        :return: The body of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.

        Body  # noqa: E501

        :param body: The body of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def ca_bundle(self):
        """Gets the ca_bundle of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.  # noqa: E501

        PEM encoded CA bundle used to validate webhook server certificate. Only used if the Server URL is using HTTPS protocol. This parameter is ignored for plain HTTP protocol connection. If not set the system root certificates are used to validate the TLS connection.  # noqa: E501

        :return: The ca_bundle of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.  # noqa: E501
        :rtype: str
        """
        return self._ca_bundle

    @ca_bundle.setter
    def ca_bundle(self, ca_bundle):
        """Sets the ca_bundle of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.

        PEM encoded CA bundle used to validate webhook server certificate. Only used if the Server URL is using HTTPS protocol. This parameter is ignored for plain HTTP protocol connection. If not set the system root certificates are used to validate the TLS connection.  # noqa: E501

        :param ca_bundle: The ca_bundle of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                ca_bundle is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', ca_bundle)):  # noqa: E501
            raise ValueError(r"Invalid value for `ca_bundle`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._ca_bundle = ca_bundle

    @property
    def ca_provider(self):
        """Gets the ca_provider of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.  # noqa: E501


        :return: The ca_provider of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.  # noqa: E501
        :rtype: IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhookCaProvider
        """
        return self._ca_provider

    @ca_provider.setter
    def ca_provider(self, ca_provider):
        """Sets the ca_provider of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.


        :param ca_provider: The ca_provider of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.  # noqa: E501
        :type: IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhookCaProvider
        """

        self._ca_provider = ca_provider

    @property
    def headers(self):
        """Gets the headers of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.  # noqa: E501

        Headers  # noqa: E501

        :return: The headers of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.

        Headers  # noqa: E501

        :param headers: The headers of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.  # noqa: E501
        :type: dict(str, str)
        """

        self._headers = headers

    @property
    def method(self):
        """Gets the method of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.  # noqa: E501

        Webhook Method  # noqa: E501

        :return: The method of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.

        Webhook Method  # noqa: E501

        :param method: The method of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.  # noqa: E501
        :type: str
        """

        self._method = method

    @property
    def result(self):
        """Gets the result of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.  # noqa: E501


        :return: The result of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.  # noqa: E501
        :rtype: IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhookResult
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.


        :param result: The result of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.  # noqa: E501
        :type: IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhookResult
        """
        if self.local_vars_configuration.client_side_validation and result is None:  # noqa: E501
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        self._result = result

    @property
    def secrets(self):
        """Gets the secrets of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.  # noqa: E501

        Secrets to fill in templates These secrets will be passed to the templating function as key value pairs under the given name  # noqa: E501

        :return: The secrets of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.  # noqa: E501
        :rtype: list[IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhookSecrets]
        """
        return self._secrets

    @secrets.setter
    def secrets(self, secrets):
        """Sets the secrets of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.

        Secrets to fill in templates These secrets will be passed to the templating function as key value pairs under the given name  # noqa: E501

        :param secrets: The secrets of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.  # noqa: E501
        :type: list[IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhookSecrets]
        """

        self._secrets = secrets

    @property
    def timeout(self):
        """Gets the timeout of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.  # noqa: E501

        Timeout  # noqa: E501

        :return: The timeout of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.  # noqa: E501
        :rtype: str
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.

        Timeout  # noqa: E501

        :param timeout: The timeout of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.  # noqa: E501
        :type: str
        """

        self._timeout = timeout

    @property
    def url(self):
        """Gets the url of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.  # noqa: E501

        Webhook url to call  # noqa: E501

        :return: The url of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.

        Webhook url to call  # noqa: E501

        :param url: The url of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

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
        if not isinstance(other, IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook):
            return True

        return self.to_dict() != other.to_dict()