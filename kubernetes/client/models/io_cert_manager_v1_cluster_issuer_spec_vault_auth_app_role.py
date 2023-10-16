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


class IoCertManagerV1ClusterIssuerSpecVaultAuthAppRole(object):
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
        'path': 'str',
        'role_id': 'str',
        'secret_ref': 'IoCertManagerV1ClusterIssuerSpecVaultAuthAppRoleSecretRef'
    }

    attribute_map = {
        'path': 'path',
        'role_id': 'roleId',
        'secret_ref': 'secretRef'
    }

    def __init__(self, path=None, role_id=None, secret_ref=None, local_vars_configuration=None):  # noqa: E501
        """IoCertManagerV1ClusterIssuerSpecVaultAuthAppRole - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._path = None
        self._role_id = None
        self._secret_ref = None
        self.discriminator = None

        self.path = path
        self.role_id = role_id
        self.secret_ref = secret_ref

    @property
    def path(self):
        """Gets the path of this IoCertManagerV1ClusterIssuerSpecVaultAuthAppRole.  # noqa: E501

        Path where the App Role authentication backend is mounted in Vault, e.g: \"approle\"  # noqa: E501

        :return: The path of this IoCertManagerV1ClusterIssuerSpecVaultAuthAppRole.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this IoCertManagerV1ClusterIssuerSpecVaultAuthAppRole.

        Path where the App Role authentication backend is mounted in Vault, e.g: \"approle\"  # noqa: E501

        :param path: The path of this IoCertManagerV1ClusterIssuerSpecVaultAuthAppRole.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and path is None:  # noqa: E501
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def role_id(self):
        """Gets the role_id of this IoCertManagerV1ClusterIssuerSpecVaultAuthAppRole.  # noqa: E501

        RoleID configured in the App Role authentication backend when setting up the authentication backend in Vault.  # noqa: E501

        :return: The role_id of this IoCertManagerV1ClusterIssuerSpecVaultAuthAppRole.  # noqa: E501
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this IoCertManagerV1ClusterIssuerSpecVaultAuthAppRole.

        RoleID configured in the App Role authentication backend when setting up the authentication backend in Vault.  # noqa: E501

        :param role_id: The role_id of this IoCertManagerV1ClusterIssuerSpecVaultAuthAppRole.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and role_id is None:  # noqa: E501
            raise ValueError("Invalid value for `role_id`, must not be `None`")  # noqa: E501

        self._role_id = role_id

    @property
    def secret_ref(self):
        """Gets the secret_ref of this IoCertManagerV1ClusterIssuerSpecVaultAuthAppRole.  # noqa: E501


        :return: The secret_ref of this IoCertManagerV1ClusterIssuerSpecVaultAuthAppRole.  # noqa: E501
        :rtype: IoCertManagerV1ClusterIssuerSpecVaultAuthAppRoleSecretRef
        """
        return self._secret_ref

    @secret_ref.setter
    def secret_ref(self, secret_ref):
        """Sets the secret_ref of this IoCertManagerV1ClusterIssuerSpecVaultAuthAppRole.


        :param secret_ref: The secret_ref of this IoCertManagerV1ClusterIssuerSpecVaultAuthAppRole.  # noqa: E501
        :type: IoCertManagerV1ClusterIssuerSpecVaultAuthAppRoleSecretRef
        """
        if self.local_vars_configuration.client_side_validation and secret_ref is None:  # noqa: E501
            raise ValueError("Invalid value for `secret_ref`, must not be `None`")  # noqa: E501

        self._secret_ref = secret_ref

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
        if not isinstance(other, IoCertManagerV1ClusterIssuerSpecVaultAuthAppRole):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoCertManagerV1ClusterIssuerSpecVaultAuthAppRole):
            return True

        return self.to_dict() != other.to_dict()