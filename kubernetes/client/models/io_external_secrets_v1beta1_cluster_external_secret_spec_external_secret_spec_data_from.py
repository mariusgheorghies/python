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


class IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecDataFrom(object):
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
        'extract': 'IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecExtract',
        'find': 'IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecFind',
        'rewrite': 'list[IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecRewrite]',
        'source_ref': 'IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecSourceRef1'
    }

    attribute_map = {
        'extract': 'extract',
        'find': 'find',
        'rewrite': 'rewrite',
        'source_ref': 'sourceRef'
    }

    def __init__(self, extract=None, find=None, rewrite=None, source_ref=None, local_vars_configuration=None):  # noqa: E501
        """IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecDataFrom - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._extract = None
        self._find = None
        self._rewrite = None
        self._source_ref = None
        self.discriminator = None

        if extract is not None:
            self.extract = extract
        if find is not None:
            self.find = find
        if rewrite is not None:
            self.rewrite = rewrite
        if source_ref is not None:
            self.source_ref = source_ref

    @property
    def extract(self):
        """Gets the extract of this IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecDataFrom.  # noqa: E501


        :return: The extract of this IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecDataFrom.  # noqa: E501
        :rtype: IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecExtract
        """
        return self._extract

    @extract.setter
    def extract(self, extract):
        """Sets the extract of this IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecDataFrom.


        :param extract: The extract of this IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecDataFrom.  # noqa: E501
        :type: IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecExtract
        """

        self._extract = extract

    @property
    def find(self):
        """Gets the find of this IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecDataFrom.  # noqa: E501


        :return: The find of this IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecDataFrom.  # noqa: E501
        :rtype: IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecFind
        """
        return self._find

    @find.setter
    def find(self, find):
        """Sets the find of this IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecDataFrom.


        :param find: The find of this IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecDataFrom.  # noqa: E501
        :type: IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecFind
        """

        self._find = find

    @property
    def rewrite(self):
        """Gets the rewrite of this IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecDataFrom.  # noqa: E501

        Used to rewrite secret Keys after getting them from the secret Provider Multiple Rewrite operations can be provided. They are applied in a layered order (first to last)  # noqa: E501

        :return: The rewrite of this IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecDataFrom.  # noqa: E501
        :rtype: list[IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecRewrite]
        """
        return self._rewrite

    @rewrite.setter
    def rewrite(self, rewrite):
        """Sets the rewrite of this IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecDataFrom.

        Used to rewrite secret Keys after getting them from the secret Provider Multiple Rewrite operations can be provided. They are applied in a layered order (first to last)  # noqa: E501

        :param rewrite: The rewrite of this IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecDataFrom.  # noqa: E501
        :type: list[IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecRewrite]
        """

        self._rewrite = rewrite

    @property
    def source_ref(self):
        """Gets the source_ref of this IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecDataFrom.  # noqa: E501


        :return: The source_ref of this IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecDataFrom.  # noqa: E501
        :rtype: IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecSourceRef1
        """
        return self._source_ref

    @source_ref.setter
    def source_ref(self, source_ref):
        """Sets the source_ref of this IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecDataFrom.


        :param source_ref: The source_ref of this IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecDataFrom.  # noqa: E501
        :type: IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecSourceRef1
        """

        self._source_ref = source_ref

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
        if not isinstance(other, IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecDataFrom):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecDataFrom):
            return True

        return self.to_dict() != other.to_dict()