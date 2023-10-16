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


class StorageV1TokenRequest(object):
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
        'audience': 'str',
        'expiration_seconds': 'int'
    }

    attribute_map = {
        'audience': 'audience',
        'expiration_seconds': 'expirationSeconds'
    }

    def __init__(self, audience=None, expiration_seconds=None, local_vars_configuration=None):  # noqa: E501
        """StorageV1TokenRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._audience = None
        self._expiration_seconds = None
        self.discriminator = None

        self.audience = audience
        if expiration_seconds is not None:
            self.expiration_seconds = expiration_seconds

    @property
    def audience(self):
        """Gets the audience of this StorageV1TokenRequest.  # noqa: E501

        Audience is the intended audience of the token in \"TokenRequestSpec\". It will default to the audiences of kube apiserver.  # noqa: E501

        :return: The audience of this StorageV1TokenRequest.  # noqa: E501
        :rtype: str
        """
        return self._audience

    @audience.setter
    def audience(self, audience):
        """Sets the audience of this StorageV1TokenRequest.

        Audience is the intended audience of the token in \"TokenRequestSpec\". It will default to the audiences of kube apiserver.  # noqa: E501

        :param audience: The audience of this StorageV1TokenRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and audience is None:  # noqa: E501
            raise ValueError("Invalid value for `audience`, must not be `None`")  # noqa: E501

        self._audience = audience

    @property
    def expiration_seconds(self):
        """Gets the expiration_seconds of this StorageV1TokenRequest.  # noqa: E501

        ExpirationSeconds is the duration of validity of the token in \"TokenRequestSpec\". It has the same default value of \"ExpirationSeconds\" in \"TokenRequestSpec\".  # noqa: E501

        :return: The expiration_seconds of this StorageV1TokenRequest.  # noqa: E501
        :rtype: int
        """
        return self._expiration_seconds

    @expiration_seconds.setter
    def expiration_seconds(self, expiration_seconds):
        """Sets the expiration_seconds of this StorageV1TokenRequest.

        ExpirationSeconds is the duration of validity of the token in \"TokenRequestSpec\". It has the same default value of \"ExpirationSeconds\" in \"TokenRequestSpec\".  # noqa: E501

        :param expiration_seconds: The expiration_seconds of this StorageV1TokenRequest.  # noqa: E501
        :type: int
        """

        self._expiration_seconds = expiration_seconds

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
        if not isinstance(other, StorageV1TokenRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StorageV1TokenRequest):
            return True

        return self.to_dict() != other.to_dict()
