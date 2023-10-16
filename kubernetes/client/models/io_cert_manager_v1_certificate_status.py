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


class IoCertManagerV1CertificateStatus(object):
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
        'conditions': 'list[IoCertManagerV1CertificateStatusConditions]',
        'last_failure_time': 'datetime',
        'next_private_key_secret_name': 'str',
        'not_after': 'datetime',
        'not_before': 'datetime',
        'renewal_time': 'datetime',
        'revision': 'int'
    }

    attribute_map = {
        'conditions': 'conditions',
        'last_failure_time': 'lastFailureTime',
        'next_private_key_secret_name': 'nextPrivateKeySecretName',
        'not_after': 'notAfter',
        'not_before': 'notBefore',
        'renewal_time': 'renewalTime',
        'revision': 'revision'
    }

    def __init__(self, conditions=None, last_failure_time=None, next_private_key_secret_name=None, not_after=None, not_before=None, renewal_time=None, revision=None, local_vars_configuration=None):  # noqa: E501
        """IoCertManagerV1CertificateStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._conditions = None
        self._last_failure_time = None
        self._next_private_key_secret_name = None
        self._not_after = None
        self._not_before = None
        self._renewal_time = None
        self._revision = None
        self.discriminator = None

        if conditions is not None:
            self.conditions = conditions
        if last_failure_time is not None:
            self.last_failure_time = last_failure_time
        if next_private_key_secret_name is not None:
            self.next_private_key_secret_name = next_private_key_secret_name
        if not_after is not None:
            self.not_after = not_after
        if not_before is not None:
            self.not_before = not_before
        if renewal_time is not None:
            self.renewal_time = renewal_time
        if revision is not None:
            self.revision = revision

    @property
    def conditions(self):
        """Gets the conditions of this IoCertManagerV1CertificateStatus.  # noqa: E501

        List of status conditions to indicate the status of certificates. Known condition types are `Ready` and `Issuing`.  # noqa: E501

        :return: The conditions of this IoCertManagerV1CertificateStatus.  # noqa: E501
        :rtype: list[IoCertManagerV1CertificateStatusConditions]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this IoCertManagerV1CertificateStatus.

        List of status conditions to indicate the status of certificates. Known condition types are `Ready` and `Issuing`.  # noqa: E501

        :param conditions: The conditions of this IoCertManagerV1CertificateStatus.  # noqa: E501
        :type: list[IoCertManagerV1CertificateStatusConditions]
        """

        self._conditions = conditions

    @property
    def last_failure_time(self):
        """Gets the last_failure_time of this IoCertManagerV1CertificateStatus.  # noqa: E501

        LastFailureTime is the time as recorded by the Certificate controller of the most recent failure to complete a CertificateRequest for this Certificate resource. If set, cert-manager will not re-request another Certificate until 1 hour has elapsed from this time.  # noqa: E501

        :return: The last_failure_time of this IoCertManagerV1CertificateStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._last_failure_time

    @last_failure_time.setter
    def last_failure_time(self, last_failure_time):
        """Sets the last_failure_time of this IoCertManagerV1CertificateStatus.

        LastFailureTime is the time as recorded by the Certificate controller of the most recent failure to complete a CertificateRequest for this Certificate resource. If set, cert-manager will not re-request another Certificate until 1 hour has elapsed from this time.  # noqa: E501

        :param last_failure_time: The last_failure_time of this IoCertManagerV1CertificateStatus.  # noqa: E501
        :type: datetime
        """

        self._last_failure_time = last_failure_time

    @property
    def next_private_key_secret_name(self):
        """Gets the next_private_key_secret_name of this IoCertManagerV1CertificateStatus.  # noqa: E501

        The name of the Secret resource containing the private key to be used for the next certificate iteration. The keymanager controller will automatically set this field if the `Issuing` condition is set to `True`. It will automatically unset this field when the Issuing condition is not set or False.  # noqa: E501

        :return: The next_private_key_secret_name of this IoCertManagerV1CertificateStatus.  # noqa: E501
        :rtype: str
        """
        return self._next_private_key_secret_name

    @next_private_key_secret_name.setter
    def next_private_key_secret_name(self, next_private_key_secret_name):
        """Sets the next_private_key_secret_name of this IoCertManagerV1CertificateStatus.

        The name of the Secret resource containing the private key to be used for the next certificate iteration. The keymanager controller will automatically set this field if the `Issuing` condition is set to `True`. It will automatically unset this field when the Issuing condition is not set or False.  # noqa: E501

        :param next_private_key_secret_name: The next_private_key_secret_name of this IoCertManagerV1CertificateStatus.  # noqa: E501
        :type: str
        """

        self._next_private_key_secret_name = next_private_key_secret_name

    @property
    def not_after(self):
        """Gets the not_after of this IoCertManagerV1CertificateStatus.  # noqa: E501

        The expiration time of the certificate stored in the secret named by this resource in `spec.secretName`.  # noqa: E501

        :return: The not_after of this IoCertManagerV1CertificateStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._not_after

    @not_after.setter
    def not_after(self, not_after):
        """Sets the not_after of this IoCertManagerV1CertificateStatus.

        The expiration time of the certificate stored in the secret named by this resource in `spec.secretName`.  # noqa: E501

        :param not_after: The not_after of this IoCertManagerV1CertificateStatus.  # noqa: E501
        :type: datetime
        """

        self._not_after = not_after

    @property
    def not_before(self):
        """Gets the not_before of this IoCertManagerV1CertificateStatus.  # noqa: E501

        The time after which the certificate stored in the secret named by this resource in spec.secretName is valid.  # noqa: E501

        :return: The not_before of this IoCertManagerV1CertificateStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._not_before

    @not_before.setter
    def not_before(self, not_before):
        """Sets the not_before of this IoCertManagerV1CertificateStatus.

        The time after which the certificate stored in the secret named by this resource in spec.secretName is valid.  # noqa: E501

        :param not_before: The not_before of this IoCertManagerV1CertificateStatus.  # noqa: E501
        :type: datetime
        """

        self._not_before = not_before

    @property
    def renewal_time(self):
        """Gets the renewal_time of this IoCertManagerV1CertificateStatus.  # noqa: E501

        RenewalTime is the time at which the certificate will be next renewed. If not set, no upcoming renewal is scheduled.  # noqa: E501

        :return: The renewal_time of this IoCertManagerV1CertificateStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._renewal_time

    @renewal_time.setter
    def renewal_time(self, renewal_time):
        """Sets the renewal_time of this IoCertManagerV1CertificateStatus.

        RenewalTime is the time at which the certificate will be next renewed. If not set, no upcoming renewal is scheduled.  # noqa: E501

        :param renewal_time: The renewal_time of this IoCertManagerV1CertificateStatus.  # noqa: E501
        :type: datetime
        """

        self._renewal_time = renewal_time

    @property
    def revision(self):
        """Gets the revision of this IoCertManagerV1CertificateStatus.  # noqa: E501

        The current 'revision' of the certificate as issued.   When a CertificateRequest resource is created, it will have the `cert-manager.io/certificate-revision` set to one greater than the current value of this field.   Upon issuance, this field will be set to the value of the annotation on the CertificateRequest resource used to issue the certificate.   Persisting the value on the CertificateRequest resource allows the certificates controller to know whether a request is part of an old issuance or if it is part of the ongoing revision's issuance by checking if the revision value in the annotation is greater than this field.  # noqa: E501

        :return: The revision of this IoCertManagerV1CertificateStatus.  # noqa: E501
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this IoCertManagerV1CertificateStatus.

        The current 'revision' of the certificate as issued.   When a CertificateRequest resource is created, it will have the `cert-manager.io/certificate-revision` set to one greater than the current value of this field.   Upon issuance, this field will be set to the value of the annotation on the CertificateRequest resource used to issue the certificate.   Persisting the value on the CertificateRequest resource allows the certificates controller to know whether a request is part of an old issuance or if it is part of the ongoing revision's issuance by checking if the revision value in the annotation is greater than this field.  # noqa: E501

        :param revision: The revision of this IoCertManagerV1CertificateStatus.  # noqa: E501
        :type: int
        """

        self._revision = revision

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
        if not isinstance(other, IoCertManagerV1CertificateStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoCertManagerV1CertificateStatus):
            return True

        return self.to_dict() != other.to_dict()
