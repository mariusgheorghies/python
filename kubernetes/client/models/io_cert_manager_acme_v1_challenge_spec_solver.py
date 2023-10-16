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


class IoCertManagerAcmeV1ChallengeSpecSolver(object):
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
        'dns01': 'IoCertManagerAcmeV1ChallengeSpecSolverDns01',
        'http01': 'IoCertManagerAcmeV1ChallengeSpecSolverHttp01',
        'selector': 'IoCertManagerAcmeV1ChallengeSpecSolverSelector'
    }

    attribute_map = {
        'dns01': 'dns01',
        'http01': 'http01',
        'selector': 'selector'
    }

    def __init__(self, dns01=None, http01=None, selector=None, local_vars_configuration=None):  # noqa: E501
        """IoCertManagerAcmeV1ChallengeSpecSolver - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dns01 = None
        self._http01 = None
        self._selector = None
        self.discriminator = None

        if dns01 is not None:
            self.dns01 = dns01
        if http01 is not None:
            self.http01 = http01
        if selector is not None:
            self.selector = selector

    @property
    def dns01(self):
        """Gets the dns01 of this IoCertManagerAcmeV1ChallengeSpecSolver.  # noqa: E501


        :return: The dns01 of this IoCertManagerAcmeV1ChallengeSpecSolver.  # noqa: E501
        :rtype: IoCertManagerAcmeV1ChallengeSpecSolverDns01
        """
        return self._dns01

    @dns01.setter
    def dns01(self, dns01):
        """Sets the dns01 of this IoCertManagerAcmeV1ChallengeSpecSolver.


        :param dns01: The dns01 of this IoCertManagerAcmeV1ChallengeSpecSolver.  # noqa: E501
        :type: IoCertManagerAcmeV1ChallengeSpecSolverDns01
        """

        self._dns01 = dns01

    @property
    def http01(self):
        """Gets the http01 of this IoCertManagerAcmeV1ChallengeSpecSolver.  # noqa: E501


        :return: The http01 of this IoCertManagerAcmeV1ChallengeSpecSolver.  # noqa: E501
        :rtype: IoCertManagerAcmeV1ChallengeSpecSolverHttp01
        """
        return self._http01

    @http01.setter
    def http01(self, http01):
        """Sets the http01 of this IoCertManagerAcmeV1ChallengeSpecSolver.


        :param http01: The http01 of this IoCertManagerAcmeV1ChallengeSpecSolver.  # noqa: E501
        :type: IoCertManagerAcmeV1ChallengeSpecSolverHttp01
        """

        self._http01 = http01

    @property
    def selector(self):
        """Gets the selector of this IoCertManagerAcmeV1ChallengeSpecSolver.  # noqa: E501


        :return: The selector of this IoCertManagerAcmeV1ChallengeSpecSolver.  # noqa: E501
        :rtype: IoCertManagerAcmeV1ChallengeSpecSolverSelector
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """Sets the selector of this IoCertManagerAcmeV1ChallengeSpecSolver.


        :param selector: The selector of this IoCertManagerAcmeV1ChallengeSpecSolver.  # noqa: E501
        :type: IoCertManagerAcmeV1ChallengeSpecSolverSelector
        """

        self._selector = selector

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
        if not isinstance(other, IoCertManagerAcmeV1ChallengeSpecSolver):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoCertManagerAcmeV1ChallengeSpecSolver):
            return True

        return self.to_dict() != other.to_dict()
