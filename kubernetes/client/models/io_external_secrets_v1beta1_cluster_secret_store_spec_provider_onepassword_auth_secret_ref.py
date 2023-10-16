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


class IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderOnepasswordAuthSecretRef(object):
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
        'connect_token_secret_ref': 'IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderOnepasswordAuthSecretRefConnectTokenSecretRef'
    }

    attribute_map = {
        'connect_token_secret_ref': 'connectTokenSecretRef'
    }

    def __init__(self, connect_token_secret_ref=None, local_vars_configuration=None):  # noqa: E501
        """IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderOnepasswordAuthSecretRef - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._connect_token_secret_ref = None
        self.discriminator = None

        self.connect_token_secret_ref = connect_token_secret_ref

    @property
    def connect_token_secret_ref(self):
        """Gets the connect_token_secret_ref of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderOnepasswordAuthSecretRef.  # noqa: E501


        :return: The connect_token_secret_ref of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderOnepasswordAuthSecretRef.  # noqa: E501
        :rtype: IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderOnepasswordAuthSecretRefConnectTokenSecretRef
        """
        return self._connect_token_secret_ref

    @connect_token_secret_ref.setter
    def connect_token_secret_ref(self, connect_token_secret_ref):
        """Sets the connect_token_secret_ref of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderOnepasswordAuthSecretRef.


        :param connect_token_secret_ref: The connect_token_secret_ref of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderOnepasswordAuthSecretRef.  # noqa: E501
        :type: IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderOnepasswordAuthSecretRefConnectTokenSecretRef
        """
        if self.local_vars_configuration.client_side_validation and connect_token_secret_ref is None:  # noqa: E501
            raise ValueError("Invalid value for `connect_token_secret_ref`, must not be `None`")  # noqa: E501

        self._connect_token_secret_ref = connect_token_secret_ref

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
        if not isinstance(other, IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderOnepasswordAuthSecretRef):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderOnepasswordAuthSecretRef):
            return True

        return self.to_dict() != other.to_dict()