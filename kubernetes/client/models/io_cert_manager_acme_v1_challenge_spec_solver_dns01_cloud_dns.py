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


class IoCertManagerAcmeV1ChallengeSpecSolverDns01CloudDNS(object):
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
        'hosted_zone_name': 'str',
        'project': 'str',
        'service_account_secret_ref': 'IoCertManagerAcmeV1ChallengeSpecSolverDns01AcmeDNSAccountSecretRef'
    }

    attribute_map = {
        'hosted_zone_name': 'hostedZoneName',
        'project': 'project',
        'service_account_secret_ref': 'serviceAccountSecretRef'
    }

    def __init__(self, hosted_zone_name=None, project=None, service_account_secret_ref=None, local_vars_configuration=None):  # noqa: E501
        """IoCertManagerAcmeV1ChallengeSpecSolverDns01CloudDNS - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._hosted_zone_name = None
        self._project = None
        self._service_account_secret_ref = None
        self.discriminator = None

        if hosted_zone_name is not None:
            self.hosted_zone_name = hosted_zone_name
        self.project = project
        if service_account_secret_ref is not None:
            self.service_account_secret_ref = service_account_secret_ref

    @property
    def hosted_zone_name(self):
        """Gets the hosted_zone_name of this IoCertManagerAcmeV1ChallengeSpecSolverDns01CloudDNS.  # noqa: E501

        HostedZoneName is an optional field that tells cert-manager in which Cloud DNS zone the challenge record has to be created. If left empty cert-manager will automatically choose a zone.  # noqa: E501

        :return: The hosted_zone_name of this IoCertManagerAcmeV1ChallengeSpecSolverDns01CloudDNS.  # noqa: E501
        :rtype: str
        """
        return self._hosted_zone_name

    @hosted_zone_name.setter
    def hosted_zone_name(self, hosted_zone_name):
        """Sets the hosted_zone_name of this IoCertManagerAcmeV1ChallengeSpecSolverDns01CloudDNS.

        HostedZoneName is an optional field that tells cert-manager in which Cloud DNS zone the challenge record has to be created. If left empty cert-manager will automatically choose a zone.  # noqa: E501

        :param hosted_zone_name: The hosted_zone_name of this IoCertManagerAcmeV1ChallengeSpecSolverDns01CloudDNS.  # noqa: E501
        :type: str
        """

        self._hosted_zone_name = hosted_zone_name

    @property
    def project(self):
        """Gets the project of this IoCertManagerAcmeV1ChallengeSpecSolverDns01CloudDNS.  # noqa: E501


        :return: The project of this IoCertManagerAcmeV1ChallengeSpecSolverDns01CloudDNS.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this IoCertManagerAcmeV1ChallengeSpecSolverDns01CloudDNS.


        :param project: The project of this IoCertManagerAcmeV1ChallengeSpecSolverDns01CloudDNS.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and project is None:  # noqa: E501
            raise ValueError("Invalid value for `project`, must not be `None`")  # noqa: E501

        self._project = project

    @property
    def service_account_secret_ref(self):
        """Gets the service_account_secret_ref of this IoCertManagerAcmeV1ChallengeSpecSolverDns01CloudDNS.  # noqa: E501


        :return: The service_account_secret_ref of this IoCertManagerAcmeV1ChallengeSpecSolverDns01CloudDNS.  # noqa: E501
        :rtype: IoCertManagerAcmeV1ChallengeSpecSolverDns01AcmeDNSAccountSecretRef
        """
        return self._service_account_secret_ref

    @service_account_secret_ref.setter
    def service_account_secret_ref(self, service_account_secret_ref):
        """Sets the service_account_secret_ref of this IoCertManagerAcmeV1ChallengeSpecSolverDns01CloudDNS.


        :param service_account_secret_ref: The service_account_secret_ref of this IoCertManagerAcmeV1ChallengeSpecSolverDns01CloudDNS.  # noqa: E501
        :type: IoCertManagerAcmeV1ChallengeSpecSolverDns01AcmeDNSAccountSecretRef
        """

        self._service_account_secret_ref = service_account_secret_ref

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
        if not isinstance(other, IoCertManagerAcmeV1ChallengeSpecSolverDns01CloudDNS):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoCertManagerAcmeV1ChallengeSpecSolverDns01CloudDNS):
            return True

        return self.to_dict() != other.to_dict()
