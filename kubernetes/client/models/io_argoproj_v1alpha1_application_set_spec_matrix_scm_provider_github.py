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


class IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderGithub(object):
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
        'all_branches': 'bool',
        'api': 'str',
        'app_secret_name': 'str',
        'organization': 'str',
        'token_ref': 'IoArgoprojV1alpha1ApplicationSetSpecMatrixPullRequestBitbucketServerBasicAuthPasswordRef'
    }

    attribute_map = {
        'all_branches': 'allBranches',
        'api': 'api',
        'app_secret_name': 'appSecretName',
        'organization': 'organization',
        'token_ref': 'tokenRef'
    }

    def __init__(self, all_branches=None, api=None, app_secret_name=None, organization=None, token_ref=None, local_vars_configuration=None):  # noqa: E501
        """IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderGithub - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._all_branches = None
        self._api = None
        self._app_secret_name = None
        self._organization = None
        self._token_ref = None
        self.discriminator = None

        if all_branches is not None:
            self.all_branches = all_branches
        if api is not None:
            self.api = api
        if app_secret_name is not None:
            self.app_secret_name = app_secret_name
        self.organization = organization
        if token_ref is not None:
            self.token_ref = token_ref

    @property
    def all_branches(self):
        """Gets the all_branches of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderGithub.  # noqa: E501


        :return: The all_branches of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderGithub.  # noqa: E501
        :rtype: bool
        """
        return self._all_branches

    @all_branches.setter
    def all_branches(self, all_branches):
        """Sets the all_branches of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderGithub.


        :param all_branches: The all_branches of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderGithub.  # noqa: E501
        :type: bool
        """

        self._all_branches = all_branches

    @property
    def api(self):
        """Gets the api of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderGithub.  # noqa: E501


        :return: The api of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderGithub.  # noqa: E501
        :rtype: str
        """
        return self._api

    @api.setter
    def api(self, api):
        """Sets the api of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderGithub.


        :param api: The api of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderGithub.  # noqa: E501
        :type: str
        """

        self._api = api

    @property
    def app_secret_name(self):
        """Gets the app_secret_name of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderGithub.  # noqa: E501


        :return: The app_secret_name of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderGithub.  # noqa: E501
        :rtype: str
        """
        return self._app_secret_name

    @app_secret_name.setter
    def app_secret_name(self, app_secret_name):
        """Sets the app_secret_name of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderGithub.


        :param app_secret_name: The app_secret_name of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderGithub.  # noqa: E501
        :type: str
        """

        self._app_secret_name = app_secret_name

    @property
    def organization(self):
        """Gets the organization of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderGithub.  # noqa: E501


        :return: The organization of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderGithub.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderGithub.


        :param organization: The organization of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderGithub.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and organization is None:  # noqa: E501
            raise ValueError("Invalid value for `organization`, must not be `None`")  # noqa: E501

        self._organization = organization

    @property
    def token_ref(self):
        """Gets the token_ref of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderGithub.  # noqa: E501


        :return: The token_ref of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderGithub.  # noqa: E501
        :rtype: IoArgoprojV1alpha1ApplicationSetSpecMatrixPullRequestBitbucketServerBasicAuthPasswordRef
        """
        return self._token_ref

    @token_ref.setter
    def token_ref(self, token_ref):
        """Sets the token_ref of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderGithub.


        :param token_ref: The token_ref of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderGithub.  # noqa: E501
        :type: IoArgoprojV1alpha1ApplicationSetSpecMatrixPullRequestBitbucketServerBasicAuthPasswordRef
        """

        self._token_ref = token_ref

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
        if not isinstance(other, IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderGithub):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderGithub):
            return True

        return self.to_dict() != other.to_dict()
