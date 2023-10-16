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


class IoArgoprojV1alpha1ApplicationSetSpecMatrixPullRequestBitbucketServerBasicAuth(object):
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
        'password_ref': 'IoArgoprojV1alpha1ApplicationSetSpecMatrixPullRequestBitbucketServerBasicAuthPasswordRef',
        'username': 'str'
    }

    attribute_map = {
        'password_ref': 'passwordRef',
        'username': 'username'
    }

    def __init__(self, password_ref=None, username=None, local_vars_configuration=None):  # noqa: E501
        """IoArgoprojV1alpha1ApplicationSetSpecMatrixPullRequestBitbucketServerBasicAuth - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._password_ref = None
        self._username = None
        self.discriminator = None

        self.password_ref = password_ref
        self.username = username

    @property
    def password_ref(self):
        """Gets the password_ref of this IoArgoprojV1alpha1ApplicationSetSpecMatrixPullRequestBitbucketServerBasicAuth.  # noqa: E501


        :return: The password_ref of this IoArgoprojV1alpha1ApplicationSetSpecMatrixPullRequestBitbucketServerBasicAuth.  # noqa: E501
        :rtype: IoArgoprojV1alpha1ApplicationSetSpecMatrixPullRequestBitbucketServerBasicAuthPasswordRef
        """
        return self._password_ref

    @password_ref.setter
    def password_ref(self, password_ref):
        """Sets the password_ref of this IoArgoprojV1alpha1ApplicationSetSpecMatrixPullRequestBitbucketServerBasicAuth.


        :param password_ref: The password_ref of this IoArgoprojV1alpha1ApplicationSetSpecMatrixPullRequestBitbucketServerBasicAuth.  # noqa: E501
        :type: IoArgoprojV1alpha1ApplicationSetSpecMatrixPullRequestBitbucketServerBasicAuthPasswordRef
        """
        if self.local_vars_configuration.client_side_validation and password_ref is None:  # noqa: E501
            raise ValueError("Invalid value for `password_ref`, must not be `None`")  # noqa: E501

        self._password_ref = password_ref

    @property
    def username(self):
        """Gets the username of this IoArgoprojV1alpha1ApplicationSetSpecMatrixPullRequestBitbucketServerBasicAuth.  # noqa: E501


        :return: The username of this IoArgoprojV1alpha1ApplicationSetSpecMatrixPullRequestBitbucketServerBasicAuth.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this IoArgoprojV1alpha1ApplicationSetSpecMatrixPullRequestBitbucketServerBasicAuth.


        :param username: The username of this IoArgoprojV1alpha1ApplicationSetSpecMatrixPullRequestBitbucketServerBasicAuth.  # noqa: E501
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
        if not isinstance(other, IoArgoprojV1alpha1ApplicationSetSpecMatrixPullRequestBitbucketServerBasicAuth):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojV1alpha1ApplicationSetSpecMatrixPullRequestBitbucketServerBasicAuth):
            return True

        return self.to_dict() != other.to_dict()