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


class IoExternalSecretsV1beta1ClusterExternalSecretStatus(object):
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
        'conditions': 'list[IoExternalSecretsV1beta1ClusterExternalSecretStatusConditions]',
        'failed_namespaces': 'list[IoExternalSecretsV1beta1ClusterExternalSecretStatusFailedNamespaces]',
        'provisioned_namespaces': 'list[str]'
    }

    attribute_map = {
        'conditions': 'conditions',
        'failed_namespaces': 'failedNamespaces',
        'provisioned_namespaces': 'provisionedNamespaces'
    }

    def __init__(self, conditions=None, failed_namespaces=None, provisioned_namespaces=None, local_vars_configuration=None):  # noqa: E501
        """IoExternalSecretsV1beta1ClusterExternalSecretStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._conditions = None
        self._failed_namespaces = None
        self._provisioned_namespaces = None
        self.discriminator = None

        if conditions is not None:
            self.conditions = conditions
        if failed_namespaces is not None:
            self.failed_namespaces = failed_namespaces
        if provisioned_namespaces is not None:
            self.provisioned_namespaces = provisioned_namespaces

    @property
    def conditions(self):
        """Gets the conditions of this IoExternalSecretsV1beta1ClusterExternalSecretStatus.  # noqa: E501


        :return: The conditions of this IoExternalSecretsV1beta1ClusterExternalSecretStatus.  # noqa: E501
        :rtype: list[IoExternalSecretsV1beta1ClusterExternalSecretStatusConditions]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this IoExternalSecretsV1beta1ClusterExternalSecretStatus.


        :param conditions: The conditions of this IoExternalSecretsV1beta1ClusterExternalSecretStatus.  # noqa: E501
        :type: list[IoExternalSecretsV1beta1ClusterExternalSecretStatusConditions]
        """

        self._conditions = conditions

    @property
    def failed_namespaces(self):
        """Gets the failed_namespaces of this IoExternalSecretsV1beta1ClusterExternalSecretStatus.  # noqa: E501

        Failed namespaces are the namespaces that failed to apply an ExternalSecret  # noqa: E501

        :return: The failed_namespaces of this IoExternalSecretsV1beta1ClusterExternalSecretStatus.  # noqa: E501
        :rtype: list[IoExternalSecretsV1beta1ClusterExternalSecretStatusFailedNamespaces]
        """
        return self._failed_namespaces

    @failed_namespaces.setter
    def failed_namespaces(self, failed_namespaces):
        """Sets the failed_namespaces of this IoExternalSecretsV1beta1ClusterExternalSecretStatus.

        Failed namespaces are the namespaces that failed to apply an ExternalSecret  # noqa: E501

        :param failed_namespaces: The failed_namespaces of this IoExternalSecretsV1beta1ClusterExternalSecretStatus.  # noqa: E501
        :type: list[IoExternalSecretsV1beta1ClusterExternalSecretStatusFailedNamespaces]
        """

        self._failed_namespaces = failed_namespaces

    @property
    def provisioned_namespaces(self):
        """Gets the provisioned_namespaces of this IoExternalSecretsV1beta1ClusterExternalSecretStatus.  # noqa: E501

        ProvisionedNamespaces are the namespaces where the ClusterExternalSecret has secrets  # noqa: E501

        :return: The provisioned_namespaces of this IoExternalSecretsV1beta1ClusterExternalSecretStatus.  # noqa: E501
        :rtype: list[str]
        """
        return self._provisioned_namespaces

    @provisioned_namespaces.setter
    def provisioned_namespaces(self, provisioned_namespaces):
        """Sets the provisioned_namespaces of this IoExternalSecretsV1beta1ClusterExternalSecretStatus.

        ProvisionedNamespaces are the namespaces where the ClusterExternalSecret has secrets  # noqa: E501

        :param provisioned_namespaces: The provisioned_namespaces of this IoExternalSecretsV1beta1ClusterExternalSecretStatus.  # noqa: E501
        :type: list[str]
        """

        self._provisioned_namespaces = provisioned_namespaces

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
        if not isinstance(other, IoExternalSecretsV1beta1ClusterExternalSecretStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoExternalSecretsV1beta1ClusterExternalSecretStatus):
            return True

        return self.to_dict() != other.to_dict()
