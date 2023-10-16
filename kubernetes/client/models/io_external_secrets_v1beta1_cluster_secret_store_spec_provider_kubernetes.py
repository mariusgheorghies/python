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


class IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetes(object):
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
        'auth': 'IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetesAuth',
        'remote_namespace': 'str',
        'server': 'IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetesServer'
    }

    attribute_map = {
        'auth': 'auth',
        'remote_namespace': 'remoteNamespace',
        'server': 'server'
    }

    def __init__(self, auth=None, remote_namespace=None, server=None, local_vars_configuration=None):  # noqa: E501
        """IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetes - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._auth = None
        self._remote_namespace = None
        self._server = None
        self.discriminator = None

        self.auth = auth
        if remote_namespace is not None:
            self.remote_namespace = remote_namespace
        if server is not None:
            self.server = server

    @property
    def auth(self):
        """Gets the auth of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetes.  # noqa: E501


        :return: The auth of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetes.  # noqa: E501
        :rtype: IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetesAuth
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        """Sets the auth of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetes.


        :param auth: The auth of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetes.  # noqa: E501
        :type: IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetesAuth
        """
        if self.local_vars_configuration.client_side_validation and auth is None:  # noqa: E501
            raise ValueError("Invalid value for `auth`, must not be `None`")  # noqa: E501

        self._auth = auth

    @property
    def remote_namespace(self):
        """Gets the remote_namespace of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetes.  # noqa: E501

        Remote namespace to fetch the secrets from  # noqa: E501

        :return: The remote_namespace of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetes.  # noqa: E501
        :rtype: str
        """
        return self._remote_namespace

    @remote_namespace.setter
    def remote_namespace(self, remote_namespace):
        """Sets the remote_namespace of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetes.

        Remote namespace to fetch the secrets from  # noqa: E501

        :param remote_namespace: The remote_namespace of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetes.  # noqa: E501
        :type: str
        """

        self._remote_namespace = remote_namespace

    @property
    def server(self):
        """Gets the server of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetes.  # noqa: E501


        :return: The server of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetes.  # noqa: E501
        :rtype: IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetesServer
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetes.


        :param server: The server of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetes.  # noqa: E501
        :type: IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetesServer
        """

        self._server = server

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
        if not isinstance(other, IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetes):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetes):
            return True

        return self.to_dict() != other.to_dict()
