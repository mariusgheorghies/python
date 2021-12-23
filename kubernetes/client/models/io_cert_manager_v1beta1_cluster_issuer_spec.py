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


class IoCertManagerV1beta1ClusterIssuerSpec(object):
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
        'acme': 'IoCertManagerV1beta1ClusterIssuerSpecAcme',
        'ca': 'IoCertManagerV1ClusterIssuerSpecCa',
        'self_signed': 'IoCertManagerV1ClusterIssuerSpecSelfSigned',
        'vault': 'IoCertManagerV1ClusterIssuerSpecVault',
        'venafi': 'IoCertManagerV1ClusterIssuerSpecVenafi'
    }

    attribute_map = {
        'acme': 'acme',
        'ca': 'ca',
        'self_signed': 'selfSigned',
        'vault': 'vault',
        'venafi': 'venafi'
    }

    def __init__(self, acme=None, ca=None, self_signed=None, vault=None, venafi=None, local_vars_configuration=None):  # noqa: E501
        """IoCertManagerV1beta1ClusterIssuerSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._acme = None
        self._ca = None
        self._self_signed = None
        self._vault = None
        self._venafi = None
        self.discriminator = None

        if acme is not None:
            self.acme = acme
        if ca is not None:
            self.ca = ca
        if self_signed is not None:
            self.self_signed = self_signed
        if vault is not None:
            self.vault = vault
        if venafi is not None:
            self.venafi = venafi

    @property
    def acme(self):
        """Gets the acme of this IoCertManagerV1beta1ClusterIssuerSpec.  # noqa: E501


        :return: The acme of this IoCertManagerV1beta1ClusterIssuerSpec.  # noqa: E501
        :rtype: IoCertManagerV1beta1ClusterIssuerSpecAcme
        """
        return self._acme

    @acme.setter
    def acme(self, acme):
        """Sets the acme of this IoCertManagerV1beta1ClusterIssuerSpec.


        :param acme: The acme of this IoCertManagerV1beta1ClusterIssuerSpec.  # noqa: E501
        :type: IoCertManagerV1beta1ClusterIssuerSpecAcme
        """

        self._acme = acme

    @property
    def ca(self):
        """Gets the ca of this IoCertManagerV1beta1ClusterIssuerSpec.  # noqa: E501


        :return: The ca of this IoCertManagerV1beta1ClusterIssuerSpec.  # noqa: E501
        :rtype: IoCertManagerV1ClusterIssuerSpecCa
        """
        return self._ca

    @ca.setter
    def ca(self, ca):
        """Sets the ca of this IoCertManagerV1beta1ClusterIssuerSpec.


        :param ca: The ca of this IoCertManagerV1beta1ClusterIssuerSpec.  # noqa: E501
        :type: IoCertManagerV1ClusterIssuerSpecCa
        """

        self._ca = ca

    @property
    def self_signed(self):
        """Gets the self_signed of this IoCertManagerV1beta1ClusterIssuerSpec.  # noqa: E501


        :return: The self_signed of this IoCertManagerV1beta1ClusterIssuerSpec.  # noqa: E501
        :rtype: IoCertManagerV1ClusterIssuerSpecSelfSigned
        """
        return self._self_signed

    @self_signed.setter
    def self_signed(self, self_signed):
        """Sets the self_signed of this IoCertManagerV1beta1ClusterIssuerSpec.


        :param self_signed: The self_signed of this IoCertManagerV1beta1ClusterIssuerSpec.  # noqa: E501
        :type: IoCertManagerV1ClusterIssuerSpecSelfSigned
        """

        self._self_signed = self_signed

    @property
    def vault(self):
        """Gets the vault of this IoCertManagerV1beta1ClusterIssuerSpec.  # noqa: E501


        :return: The vault of this IoCertManagerV1beta1ClusterIssuerSpec.  # noqa: E501
        :rtype: IoCertManagerV1ClusterIssuerSpecVault
        """
        return self._vault

    @vault.setter
    def vault(self, vault):
        """Sets the vault of this IoCertManagerV1beta1ClusterIssuerSpec.


        :param vault: The vault of this IoCertManagerV1beta1ClusterIssuerSpec.  # noqa: E501
        :type: IoCertManagerV1ClusterIssuerSpecVault
        """

        self._vault = vault

    @property
    def venafi(self):
        """Gets the venafi of this IoCertManagerV1beta1ClusterIssuerSpec.  # noqa: E501


        :return: The venafi of this IoCertManagerV1beta1ClusterIssuerSpec.  # noqa: E501
        :rtype: IoCertManagerV1ClusterIssuerSpecVenafi
        """
        return self._venafi

    @venafi.setter
    def venafi(self, venafi):
        """Sets the venafi of this IoCertManagerV1beta1ClusterIssuerSpec.


        :param venafi: The venafi of this IoCertManagerV1beta1ClusterIssuerSpec.  # noqa: E501
        :type: IoCertManagerV1ClusterIssuerSpecVenafi
        """

        self._venafi = venafi

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
        if not isinstance(other, IoCertManagerV1beta1ClusterIssuerSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoCertManagerV1beta1ClusterIssuerSpec):
            return True

        return self.to_dict() != other.to_dict()
