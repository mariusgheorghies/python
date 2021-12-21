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


class IoCertManagerV1ClusterIssuerStatusAcme(object):
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
        'last_registered_email': 'str',
        'uri': 'str'
    }

    attribute_map = {
        'last_registered_email': 'lastRegisteredEmail',
        'uri': 'uri'
    }

    def __init__(self, last_registered_email=None, uri=None, local_vars_configuration=None):  # noqa: E501
        """IoCertManagerV1ClusterIssuerStatusAcme - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._last_registered_email = None
        self._uri = None
        self.discriminator = None

        if last_registered_email is not None:
            self.last_registered_email = last_registered_email
        if uri is not None:
            self.uri = uri

    @property
    def last_registered_email(self):
        """Gets the last_registered_email of this IoCertManagerV1ClusterIssuerStatusAcme.  # noqa: E501

        LastRegisteredEmail is the email associated with the latest registered ACME account, in order to track changes made to registered account associated with the  Issuer  # noqa: E501

        :return: The last_registered_email of this IoCertManagerV1ClusterIssuerStatusAcme.  # noqa: E501
        :rtype: str
        """
        return self._last_registered_email

    @last_registered_email.setter
    def last_registered_email(self, last_registered_email):
        """Sets the last_registered_email of this IoCertManagerV1ClusterIssuerStatusAcme.

        LastRegisteredEmail is the email associated with the latest registered ACME account, in order to track changes made to registered account associated with the  Issuer  # noqa: E501

        :param last_registered_email: The last_registered_email of this IoCertManagerV1ClusterIssuerStatusAcme.  # noqa: E501
        :type: str
        """

        self._last_registered_email = last_registered_email

    @property
    def uri(self):
        """Gets the uri of this IoCertManagerV1ClusterIssuerStatusAcme.  # noqa: E501

        URI is the unique account identifier, which can also be used to retrieve account details from the CA  # noqa: E501

        :return: The uri of this IoCertManagerV1ClusterIssuerStatusAcme.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this IoCertManagerV1ClusterIssuerStatusAcme.

        URI is the unique account identifier, which can also be used to retrieve account details from the CA  # noqa: E501

        :param uri: The uri of this IoCertManagerV1ClusterIssuerStatusAcme.  # noqa: E501
        :type: str
        """

        self._uri = uri

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
        if not isinstance(other, IoCertManagerV1ClusterIssuerStatusAcme):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoCertManagerV1ClusterIssuerStatusAcme):
            return True

        return self.to_dict() != other.to_dict()
