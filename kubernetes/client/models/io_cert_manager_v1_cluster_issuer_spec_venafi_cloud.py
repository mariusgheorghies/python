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


class IoCertManagerV1ClusterIssuerSpecVenafiCloud(object):
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
        'api_token_secret_ref': 'IoCertManagerV1ClusterIssuerSpecVenafiCloudApiTokenSecretRef',
        'url': 'str'
    }

    attribute_map = {
        'api_token_secret_ref': 'apiTokenSecretRef',
        'url': 'url'
    }

    def __init__(self, api_token_secret_ref=None, url=None, local_vars_configuration=None):  # noqa: E501
        """IoCertManagerV1ClusterIssuerSpecVenafiCloud - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._api_token_secret_ref = None
        self._url = None
        self.discriminator = None

        self.api_token_secret_ref = api_token_secret_ref
        if url is not None:
            self.url = url

    @property
    def api_token_secret_ref(self):
        """Gets the api_token_secret_ref of this IoCertManagerV1ClusterIssuerSpecVenafiCloud.  # noqa: E501


        :return: The api_token_secret_ref of this IoCertManagerV1ClusterIssuerSpecVenafiCloud.  # noqa: E501
        :rtype: IoCertManagerV1ClusterIssuerSpecVenafiCloudApiTokenSecretRef
        """
        return self._api_token_secret_ref

    @api_token_secret_ref.setter
    def api_token_secret_ref(self, api_token_secret_ref):
        """Sets the api_token_secret_ref of this IoCertManagerV1ClusterIssuerSpecVenafiCloud.


        :param api_token_secret_ref: The api_token_secret_ref of this IoCertManagerV1ClusterIssuerSpecVenafiCloud.  # noqa: E501
        :type: IoCertManagerV1ClusterIssuerSpecVenafiCloudApiTokenSecretRef
        """
        if self.local_vars_configuration.client_side_validation and api_token_secret_ref is None:  # noqa: E501
            raise ValueError("Invalid value for `api_token_secret_ref`, must not be `None`")  # noqa: E501

        self._api_token_secret_ref = api_token_secret_ref

    @property
    def url(self):
        """Gets the url of this IoCertManagerV1ClusterIssuerSpecVenafiCloud.  # noqa: E501

        URL is the base URL for Venafi Cloud. Defaults to \"https://api.venafi.cloud/v1\".  # noqa: E501

        :return: The url of this IoCertManagerV1ClusterIssuerSpecVenafiCloud.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this IoCertManagerV1ClusterIssuerSpecVenafiCloud.

        URL is the base URL for Venafi Cloud. Defaults to \"https://api.venafi.cloud/v1\".  # noqa: E501

        :param url: The url of this IoCertManagerV1ClusterIssuerSpecVenafiCloud.  # noqa: E501
        :type: str
        """

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
        if not isinstance(other, IoCertManagerV1ClusterIssuerSpecVenafiCloud):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoCertManagerV1ClusterIssuerSpecVenafiCloud):
            return True

        return self.to_dict() != other.to_dict()
