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


class IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecIamAuthenticatorConfigMapUsers(object):
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
        'groups': 'list[str]',
        'userarn': 'str',
        'username': 'str'
    }

    attribute_map = {
        'groups': 'groups',
        'userarn': 'userarn',
        'username': 'username'
    }

    def __init__(self, groups=None, userarn=None, username=None, local_vars_configuration=None):  # noqa: E501
        """IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecIamAuthenticatorConfigMapUsers - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._groups = None
        self._userarn = None
        self._username = None
        self.discriminator = None

        self.groups = groups
        self.userarn = userarn
        self.username = username

    @property
    def groups(self):
        """Gets the groups of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecIamAuthenticatorConfigMapUsers.  # noqa: E501

        Groups is a list of kubernetes RBAC groups  # noqa: E501

        :return: The groups of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecIamAuthenticatorConfigMapUsers.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecIamAuthenticatorConfigMapUsers.

        Groups is a list of kubernetes RBAC groups  # noqa: E501

        :param groups: The groups of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecIamAuthenticatorConfigMapUsers.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and groups is None:  # noqa: E501
            raise ValueError("Invalid value for `groups`, must not be `None`")  # noqa: E501

        self._groups = groups

    @property
    def userarn(self):
        """Gets the userarn of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecIamAuthenticatorConfigMapUsers.  # noqa: E501

        UserARN is the AWS ARN for the user to map  # noqa: E501

        :return: The userarn of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecIamAuthenticatorConfigMapUsers.  # noqa: E501
        :rtype: str
        """
        return self._userarn

    @userarn.setter
    def userarn(self, userarn):
        """Sets the userarn of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecIamAuthenticatorConfigMapUsers.

        UserARN is the AWS ARN for the user to map  # noqa: E501

        :param userarn: The userarn of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecIamAuthenticatorConfigMapUsers.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and userarn is None:  # noqa: E501
            raise ValueError("Invalid value for `userarn`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                userarn is not None and len(userarn) < 31):
            raise ValueError("Invalid value for `userarn`, length must be greater than or equal to `31`")  # noqa: E501

        self._userarn = userarn

    @property
    def username(self):
        """Gets the username of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecIamAuthenticatorConfigMapUsers.  # noqa: E501

        UserName is a kubernetes RBAC user subject  # noqa: E501

        :return: The username of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecIamAuthenticatorConfigMapUsers.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecIamAuthenticatorConfigMapUsers.

        UserName is a kubernetes RBAC user subject  # noqa: E501

        :param username: The username of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecIamAuthenticatorConfigMapUsers.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and username is None:  # noqa: E501
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

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
        if not isinstance(other, IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecIamAuthenticatorConfigMapUsers):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecIamAuthenticatorConfigMapUsers):
            return True

        return self.to_dict() != other.to_dict()
