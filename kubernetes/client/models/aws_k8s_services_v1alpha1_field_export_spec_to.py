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


class AwsK8sServicesV1alpha1FieldExportSpecTo(object):
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
        'key': 'str',
        'kind': 'str',
        'name': 'str',
        'namespace': 'str'
    }

    attribute_map = {
        'key': 'key',
        'kind': 'kind',
        'name': 'name',
        'namespace': 'namespace'
    }

    def __init__(self, key=None, kind=None, name=None, namespace=None, local_vars_configuration=None):  # noqa: E501
        """AwsK8sServicesV1alpha1FieldExportSpecTo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._key = None
        self._kind = None
        self._name = None
        self._namespace = None
        self.discriminator = None

        if key is not None:
            self.key = key
        self.kind = kind
        self.name = name
        if namespace is not None:
            self.namespace = namespace

    @property
    def key(self):
        """Gets the key of this AwsK8sServicesV1alpha1FieldExportSpecTo.  # noqa: E501

        Key overrides the default value (`<namespace>.<FieldExport-resource-name>`) for the FieldExport target  # noqa: E501

        :return: The key of this AwsK8sServicesV1alpha1FieldExportSpecTo.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this AwsK8sServicesV1alpha1FieldExportSpecTo.

        Key overrides the default value (`<namespace>.<FieldExport-resource-name>`) for the FieldExport target  # noqa: E501

        :param key: The key of this AwsK8sServicesV1alpha1FieldExportSpecTo.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def kind(self):
        """Gets the kind of this AwsK8sServicesV1alpha1FieldExportSpecTo.  # noqa: E501

        FieldExportOutputType represents all types that can be produced by a field export operation  # noqa: E501

        :return: The kind of this AwsK8sServicesV1alpha1FieldExportSpecTo.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this AwsK8sServicesV1alpha1FieldExportSpecTo.

        FieldExportOutputType represents all types that can be produced by a field export operation  # noqa: E501

        :param kind: The kind of this AwsK8sServicesV1alpha1FieldExportSpecTo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and kind is None:  # noqa: E501
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501
        allowed_values = ["configmap", "secret"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and kind not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `kind` ({0}), must be one of {1}"  # noqa: E501
                .format(kind, allowed_values)
            )

        self._kind = kind

    @property
    def name(self):
        """Gets the name of this AwsK8sServicesV1alpha1FieldExportSpecTo.  # noqa: E501


        :return: The name of this AwsK8sServicesV1alpha1FieldExportSpecTo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AwsK8sServicesV1alpha1FieldExportSpecTo.


        :param name: The name of this AwsK8sServicesV1alpha1FieldExportSpecTo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this AwsK8sServicesV1alpha1FieldExportSpecTo.  # noqa: E501

        Namespace is marked as optional, so we cannot compose `NamespacedName`  # noqa: E501

        :return: The namespace of this AwsK8sServicesV1alpha1FieldExportSpecTo.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this AwsK8sServicesV1alpha1FieldExportSpecTo.

        Namespace is marked as optional, so we cannot compose `NamespacedName`  # noqa: E501

        :param namespace: The namespace of this AwsK8sServicesV1alpha1FieldExportSpecTo.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

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
        if not isinstance(other, AwsK8sServicesV1alpha1FieldExportSpecTo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AwsK8sServicesV1alpha1FieldExportSpecTo):
            return True

        return self.to_dict() != other.to_dict()
