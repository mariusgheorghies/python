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


class IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAwsAuthSecretRef(object):
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
        'access_key_id_secret_ref': 'IoExternalSecretsGeneratorsV1alpha1ECRAuthorizationTokenSpecAuthSecretRefAccessKeyIDSecretRef',
        'secret_access_key_secret_ref': 'IoExternalSecretsGeneratorsV1alpha1ECRAuthorizationTokenSpecAuthSecretRefSecretAccessKeySecretRef'
    }

    attribute_map = {
        'access_key_id_secret_ref': 'accessKeyIDSecretRef',
        'secret_access_key_secret_ref': 'secretAccessKeySecretRef'
    }

    def __init__(self, access_key_id_secret_ref=None, secret_access_key_secret_ref=None, local_vars_configuration=None):  # noqa: E501
        """IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAwsAuthSecretRef - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_key_id_secret_ref = None
        self._secret_access_key_secret_ref = None
        self.discriminator = None

        if access_key_id_secret_ref is not None:
            self.access_key_id_secret_ref = access_key_id_secret_ref
        if secret_access_key_secret_ref is not None:
            self.secret_access_key_secret_ref = secret_access_key_secret_ref

    @property
    def access_key_id_secret_ref(self):
        """Gets the access_key_id_secret_ref of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAwsAuthSecretRef.  # noqa: E501


        :return: The access_key_id_secret_ref of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAwsAuthSecretRef.  # noqa: E501
        :rtype: IoExternalSecretsGeneratorsV1alpha1ECRAuthorizationTokenSpecAuthSecretRefAccessKeyIDSecretRef
        """
        return self._access_key_id_secret_ref

    @access_key_id_secret_ref.setter
    def access_key_id_secret_ref(self, access_key_id_secret_ref):
        """Sets the access_key_id_secret_ref of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAwsAuthSecretRef.


        :param access_key_id_secret_ref: The access_key_id_secret_ref of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAwsAuthSecretRef.  # noqa: E501
        :type: IoExternalSecretsGeneratorsV1alpha1ECRAuthorizationTokenSpecAuthSecretRefAccessKeyIDSecretRef
        """

        self._access_key_id_secret_ref = access_key_id_secret_ref

    @property
    def secret_access_key_secret_ref(self):
        """Gets the secret_access_key_secret_ref of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAwsAuthSecretRef.  # noqa: E501


        :return: The secret_access_key_secret_ref of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAwsAuthSecretRef.  # noqa: E501
        :rtype: IoExternalSecretsGeneratorsV1alpha1ECRAuthorizationTokenSpecAuthSecretRefSecretAccessKeySecretRef
        """
        return self._secret_access_key_secret_ref

    @secret_access_key_secret_ref.setter
    def secret_access_key_secret_ref(self, secret_access_key_secret_ref):
        """Sets the secret_access_key_secret_ref of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAwsAuthSecretRef.


        :param secret_access_key_secret_ref: The secret_access_key_secret_ref of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAwsAuthSecretRef.  # noqa: E501
        :type: IoExternalSecretsGeneratorsV1alpha1ECRAuthorizationTokenSpecAuthSecretRefSecretAccessKeySecretRef
        """

        self._secret_access_key_secret_ref = secret_access_key_secret_ref

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
        if not isinstance(other, IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAwsAuthSecretRef):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAwsAuthSecretRef):
            return True

        return self.to_dict() != other.to_dict()
