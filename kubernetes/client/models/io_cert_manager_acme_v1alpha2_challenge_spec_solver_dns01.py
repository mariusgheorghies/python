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


class IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01(object):
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
        'acmedns': 'IoCertManagerAcmeV1ChallengeSpecSolverDns01AcmeDNS',
        'akamai': 'IoCertManagerAcmeV1ChallengeSpecSolverDns01Akamai',
        'azuredns': 'IoCertManagerAcmeV1ChallengeSpecSolverDns01AzureDNS',
        'clouddns': 'IoCertManagerAcmeV1ChallengeSpecSolverDns01CloudDNS',
        'cloudflare': 'IoCertManagerAcmeV1ChallengeSpecSolverDns01Cloudflare',
        'cname_strategy': 'str',
        'digitalocean': 'IoCertManagerAcmeV1ChallengeSpecSolverDns01Digitalocean',
        'rfc2136': 'IoCertManagerAcmeV1ChallengeSpecSolverDns01Rfc2136',
        'route53': 'IoCertManagerAcmeV1ChallengeSpecSolverDns01Route53',
        'webhook': 'IoCertManagerAcmeV1ChallengeSpecSolverDns01Webhook'
    }

    attribute_map = {
        'acmedns': 'acmedns',
        'akamai': 'akamai',
        'azuredns': 'azuredns',
        'clouddns': 'clouddns',
        'cloudflare': 'cloudflare',
        'cname_strategy': 'cnameStrategy',
        'digitalocean': 'digitalocean',
        'rfc2136': 'rfc2136',
        'route53': 'route53',
        'webhook': 'webhook'
    }

    def __init__(self, acmedns=None, akamai=None, azuredns=None, clouddns=None, cloudflare=None, cname_strategy=None, digitalocean=None, rfc2136=None, route53=None, webhook=None, local_vars_configuration=None):  # noqa: E501
        """IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._acmedns = None
        self._akamai = None
        self._azuredns = None
        self._clouddns = None
        self._cloudflare = None
        self._cname_strategy = None
        self._digitalocean = None
        self._rfc2136 = None
        self._route53 = None
        self._webhook = None
        self.discriminator = None

        if acmedns is not None:
            self.acmedns = acmedns
        if akamai is not None:
            self.akamai = akamai
        if azuredns is not None:
            self.azuredns = azuredns
        if clouddns is not None:
            self.clouddns = clouddns
        if cloudflare is not None:
            self.cloudflare = cloudflare
        if cname_strategy is not None:
            self.cname_strategy = cname_strategy
        if digitalocean is not None:
            self.digitalocean = digitalocean
        if rfc2136 is not None:
            self.rfc2136 = rfc2136
        if route53 is not None:
            self.route53 = route53
        if webhook is not None:
            self.webhook = webhook

    @property
    def acmedns(self):
        """Gets the acmedns of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.  # noqa: E501


        :return: The acmedns of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.  # noqa: E501
        :rtype: IoCertManagerAcmeV1ChallengeSpecSolverDns01AcmeDNS
        """
        return self._acmedns

    @acmedns.setter
    def acmedns(self, acmedns):
        """Sets the acmedns of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.


        :param acmedns: The acmedns of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.  # noqa: E501
        :type: IoCertManagerAcmeV1ChallengeSpecSolverDns01AcmeDNS
        """

        self._acmedns = acmedns

    @property
    def akamai(self):
        """Gets the akamai of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.  # noqa: E501


        :return: The akamai of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.  # noqa: E501
        :rtype: IoCertManagerAcmeV1ChallengeSpecSolverDns01Akamai
        """
        return self._akamai

    @akamai.setter
    def akamai(self, akamai):
        """Sets the akamai of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.


        :param akamai: The akamai of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.  # noqa: E501
        :type: IoCertManagerAcmeV1ChallengeSpecSolverDns01Akamai
        """

        self._akamai = akamai

    @property
    def azuredns(self):
        """Gets the azuredns of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.  # noqa: E501


        :return: The azuredns of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.  # noqa: E501
        :rtype: IoCertManagerAcmeV1ChallengeSpecSolverDns01AzureDNS
        """
        return self._azuredns

    @azuredns.setter
    def azuredns(self, azuredns):
        """Sets the azuredns of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.


        :param azuredns: The azuredns of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.  # noqa: E501
        :type: IoCertManagerAcmeV1ChallengeSpecSolverDns01AzureDNS
        """

        self._azuredns = azuredns

    @property
    def clouddns(self):
        """Gets the clouddns of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.  # noqa: E501


        :return: The clouddns of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.  # noqa: E501
        :rtype: IoCertManagerAcmeV1ChallengeSpecSolverDns01CloudDNS
        """
        return self._clouddns

    @clouddns.setter
    def clouddns(self, clouddns):
        """Sets the clouddns of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.


        :param clouddns: The clouddns of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.  # noqa: E501
        :type: IoCertManagerAcmeV1ChallengeSpecSolverDns01CloudDNS
        """

        self._clouddns = clouddns

    @property
    def cloudflare(self):
        """Gets the cloudflare of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.  # noqa: E501


        :return: The cloudflare of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.  # noqa: E501
        :rtype: IoCertManagerAcmeV1ChallengeSpecSolverDns01Cloudflare
        """
        return self._cloudflare

    @cloudflare.setter
    def cloudflare(self, cloudflare):
        """Sets the cloudflare of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.


        :param cloudflare: The cloudflare of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.  # noqa: E501
        :type: IoCertManagerAcmeV1ChallengeSpecSolverDns01Cloudflare
        """

        self._cloudflare = cloudflare

    @property
    def cname_strategy(self):
        """Gets the cname_strategy of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.  # noqa: E501

        CNAMEStrategy configures how the DNS01 provider should handle CNAME records when found in DNS zones.  # noqa: E501

        :return: The cname_strategy of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.  # noqa: E501
        :rtype: str
        """
        return self._cname_strategy

    @cname_strategy.setter
    def cname_strategy(self, cname_strategy):
        """Sets the cname_strategy of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.

        CNAMEStrategy configures how the DNS01 provider should handle CNAME records when found in DNS zones.  # noqa: E501

        :param cname_strategy: The cname_strategy of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Follow"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and cname_strategy not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `cname_strategy` ({0}), must be one of {1}"  # noqa: E501
                .format(cname_strategy, allowed_values)
            )

        self._cname_strategy = cname_strategy

    @property
    def digitalocean(self):
        """Gets the digitalocean of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.  # noqa: E501


        :return: The digitalocean of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.  # noqa: E501
        :rtype: IoCertManagerAcmeV1ChallengeSpecSolverDns01Digitalocean
        """
        return self._digitalocean

    @digitalocean.setter
    def digitalocean(self, digitalocean):
        """Sets the digitalocean of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.


        :param digitalocean: The digitalocean of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.  # noqa: E501
        :type: IoCertManagerAcmeV1ChallengeSpecSolverDns01Digitalocean
        """

        self._digitalocean = digitalocean

    @property
    def rfc2136(self):
        """Gets the rfc2136 of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.  # noqa: E501


        :return: The rfc2136 of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.  # noqa: E501
        :rtype: IoCertManagerAcmeV1ChallengeSpecSolverDns01Rfc2136
        """
        return self._rfc2136

    @rfc2136.setter
    def rfc2136(self, rfc2136):
        """Sets the rfc2136 of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.


        :param rfc2136: The rfc2136 of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.  # noqa: E501
        :type: IoCertManagerAcmeV1ChallengeSpecSolverDns01Rfc2136
        """

        self._rfc2136 = rfc2136

    @property
    def route53(self):
        """Gets the route53 of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.  # noqa: E501


        :return: The route53 of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.  # noqa: E501
        :rtype: IoCertManagerAcmeV1ChallengeSpecSolverDns01Route53
        """
        return self._route53

    @route53.setter
    def route53(self, route53):
        """Sets the route53 of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.


        :param route53: The route53 of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.  # noqa: E501
        :type: IoCertManagerAcmeV1ChallengeSpecSolverDns01Route53
        """

        self._route53 = route53

    @property
    def webhook(self):
        """Gets the webhook of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.  # noqa: E501


        :return: The webhook of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.  # noqa: E501
        :rtype: IoCertManagerAcmeV1ChallengeSpecSolverDns01Webhook
        """
        return self._webhook

    @webhook.setter
    def webhook(self, webhook):
        """Sets the webhook of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.


        :param webhook: The webhook of this IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.  # noqa: E501
        :type: IoCertManagerAcmeV1ChallengeSpecSolverDns01Webhook
        """

        self._webhook = webhook

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
        if not isinstance(other, IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01):
            return True

        return self.to_dict() != other.to_dict()
