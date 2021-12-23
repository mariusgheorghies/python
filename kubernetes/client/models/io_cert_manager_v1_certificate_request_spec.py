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


class IoCertManagerV1CertificateRequestSpec(object):
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
        'duration': 'str',
        'extra': 'dict(str, list[str])',
        'groups': 'list[str]',
        'is_ca': 'bool',
        'issuer_ref': 'IoCertManagerV1CertificateRequestSpecIssuerRef',
        'request': 'str',
        'uid': 'str',
        'usages': 'list[str]',
        'username': 'str'
    }

    attribute_map = {
        'duration': 'duration',
        'extra': 'extra',
        'groups': 'groups',
        'is_ca': 'isCA',
        'issuer_ref': 'issuerRef',
        'request': 'request',
        'uid': 'uid',
        'usages': 'usages',
        'username': 'username'
    }

    def __init__(self, duration=None, extra=None, groups=None, is_ca=None, issuer_ref=None, request=None, uid=None, usages=None, username=None, local_vars_configuration=None):  # noqa: E501
        """IoCertManagerV1CertificateRequestSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._duration = None
        self._extra = None
        self._groups = None
        self._is_ca = None
        self._issuer_ref = None
        self._request = None
        self._uid = None
        self._usages = None
        self._username = None
        self.discriminator = None

        if duration is not None:
            self.duration = duration
        if extra is not None:
            self.extra = extra
        if groups is not None:
            self.groups = groups
        if is_ca is not None:
            self.is_ca = is_ca
        self.issuer_ref = issuer_ref
        self.request = request
        if uid is not None:
            self.uid = uid
        if usages is not None:
            self.usages = usages
        if username is not None:
            self.username = username

    @property
    def duration(self):
        """Gets the duration of this IoCertManagerV1CertificateRequestSpec.  # noqa: E501

        The requested 'duration' (i.e. lifetime) of the Certificate. This option may be ignored/overridden by some issuer types.  # noqa: E501

        :return: The duration of this IoCertManagerV1CertificateRequestSpec.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this IoCertManagerV1CertificateRequestSpec.

        The requested 'duration' (i.e. lifetime) of the Certificate. This option may be ignored/overridden by some issuer types.  # noqa: E501

        :param duration: The duration of this IoCertManagerV1CertificateRequestSpec.  # noqa: E501
        :type: str
        """

        self._duration = duration

    @property
    def extra(self):
        """Gets the extra of this IoCertManagerV1CertificateRequestSpec.  # noqa: E501

        Extra contains extra attributes of the user that created the CertificateRequest. Populated by the cert-manager webhook on creation and immutable.  # noqa: E501

        :return: The extra of this IoCertManagerV1CertificateRequestSpec.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this IoCertManagerV1CertificateRequestSpec.

        Extra contains extra attributes of the user that created the CertificateRequest. Populated by the cert-manager webhook on creation and immutable.  # noqa: E501

        :param extra: The extra of this IoCertManagerV1CertificateRequestSpec.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._extra = extra

    @property
    def groups(self):
        """Gets the groups of this IoCertManagerV1CertificateRequestSpec.  # noqa: E501

        Groups contains group membership of the user that created the CertificateRequest. Populated by the cert-manager webhook on creation and immutable.  # noqa: E501

        :return: The groups of this IoCertManagerV1CertificateRequestSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this IoCertManagerV1CertificateRequestSpec.

        Groups contains group membership of the user that created the CertificateRequest. Populated by the cert-manager webhook on creation and immutable.  # noqa: E501

        :param groups: The groups of this IoCertManagerV1CertificateRequestSpec.  # noqa: E501
        :type: list[str]
        """

        self._groups = groups

    @property
    def is_ca(self):
        """Gets the is_ca of this IoCertManagerV1CertificateRequestSpec.  # noqa: E501

        IsCA will request to mark the certificate as valid for certificate signing when submitting to the issuer. This will automatically add the `cert sign` usage to the list of `usages`.  # noqa: E501

        :return: The is_ca of this IoCertManagerV1CertificateRequestSpec.  # noqa: E501
        :rtype: bool
        """
        return self._is_ca

    @is_ca.setter
    def is_ca(self, is_ca):
        """Sets the is_ca of this IoCertManagerV1CertificateRequestSpec.

        IsCA will request to mark the certificate as valid for certificate signing when submitting to the issuer. This will automatically add the `cert sign` usage to the list of `usages`.  # noqa: E501

        :param is_ca: The is_ca of this IoCertManagerV1CertificateRequestSpec.  # noqa: E501
        :type: bool
        """

        self._is_ca = is_ca

    @property
    def issuer_ref(self):
        """Gets the issuer_ref of this IoCertManagerV1CertificateRequestSpec.  # noqa: E501


        :return: The issuer_ref of this IoCertManagerV1CertificateRequestSpec.  # noqa: E501
        :rtype: IoCertManagerV1CertificateRequestSpecIssuerRef
        """
        return self._issuer_ref

    @issuer_ref.setter
    def issuer_ref(self, issuer_ref):
        """Sets the issuer_ref of this IoCertManagerV1CertificateRequestSpec.


        :param issuer_ref: The issuer_ref of this IoCertManagerV1CertificateRequestSpec.  # noqa: E501
        :type: IoCertManagerV1CertificateRequestSpecIssuerRef
        """
        if self.local_vars_configuration.client_side_validation and issuer_ref is None:  # noqa: E501
            raise ValueError("Invalid value for `issuer_ref`, must not be `None`")  # noqa: E501

        self._issuer_ref = issuer_ref

    @property
    def request(self):
        """Gets the request of this IoCertManagerV1CertificateRequestSpec.  # noqa: E501

        The PEM-encoded x509 certificate signing request to be submitted to the CA for signing.  # noqa: E501

        :return: The request of this IoCertManagerV1CertificateRequestSpec.  # noqa: E501
        :rtype: str
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this IoCertManagerV1CertificateRequestSpec.

        The PEM-encoded x509 certificate signing request to be submitted to the CA for signing.  # noqa: E501

        :param request: The request of this IoCertManagerV1CertificateRequestSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and request is None:  # noqa: E501
            raise ValueError("Invalid value for `request`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                request is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', request)):  # noqa: E501
            raise ValueError(r"Invalid value for `request`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._request = request

    @property
    def uid(self):
        """Gets the uid of this IoCertManagerV1CertificateRequestSpec.  # noqa: E501

        UID contains the uid of the user that created the CertificateRequest. Populated by the cert-manager webhook on creation and immutable.  # noqa: E501

        :return: The uid of this IoCertManagerV1CertificateRequestSpec.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this IoCertManagerV1CertificateRequestSpec.

        UID contains the uid of the user that created the CertificateRequest. Populated by the cert-manager webhook on creation and immutable.  # noqa: E501

        :param uid: The uid of this IoCertManagerV1CertificateRequestSpec.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def usages(self):
        """Gets the usages of this IoCertManagerV1CertificateRequestSpec.  # noqa: E501

        Usages is the set of x509 usages that are requested for the certificate. If usages are set they SHOULD be encoded inside the CSR spec Defaults to `digital signature` and `key encipherment` if not specified.  # noqa: E501

        :return: The usages of this IoCertManagerV1CertificateRequestSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._usages

    @usages.setter
    def usages(self, usages):
        """Sets the usages of this IoCertManagerV1CertificateRequestSpec.

        Usages is the set of x509 usages that are requested for the certificate. If usages are set they SHOULD be encoded inside the CSR spec Defaults to `digital signature` and `key encipherment` if not specified.  # noqa: E501

        :param usages: The usages of this IoCertManagerV1CertificateRequestSpec.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["signing", "digital signature", "content commitment", "key encipherment", "key agreement", "data encipherment", "cert sign", "crl sign", "encipher only", "decipher only", "any", "server auth", "client auth", "code signing", "email protection", "s/mime", "ipsec end system", "ipsec tunnel", "ipsec user", "timestamping", "ocsp signing", "microsoft sgc", "netscape sgc"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(usages).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `usages` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(usages) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._usages = usages

    @property
    def username(self):
        """Gets the username of this IoCertManagerV1CertificateRequestSpec.  # noqa: E501

        Username contains the name of the user that created the CertificateRequest. Populated by the cert-manager webhook on creation and immutable.  # noqa: E501

        :return: The username of this IoCertManagerV1CertificateRequestSpec.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this IoCertManagerV1CertificateRequestSpec.

        Username contains the name of the user that created the CertificateRequest. Populated by the cert-manager webhook on creation and immutable.  # noqa: E501

        :param username: The username of this IoCertManagerV1CertificateRequestSpec.  # noqa: E501
        :type: str
        """

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
        if not isinstance(other, IoCertManagerV1CertificateRequestSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoCertManagerV1CertificateRequestSpec):
            return True

        return self.to_dict() != other.to_dict()
