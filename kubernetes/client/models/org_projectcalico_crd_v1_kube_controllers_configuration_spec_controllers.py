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


class OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers(object):
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
        'namespace': 'OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllersNamespace',
        'node': 'OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllersNode',
        'policy': 'OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllersPolicy',
        'service_account': 'OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllersServiceAccount',
        'workload_endpoint': 'OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllersWorkloadEndpoint'
    }

    attribute_map = {
        'namespace': 'namespace',
        'node': 'node',
        'policy': 'policy',
        'service_account': 'serviceAccount',
        'workload_endpoint': 'workloadEndpoint'
    }

    def __init__(self, namespace=None, node=None, policy=None, service_account=None, workload_endpoint=None, local_vars_configuration=None):  # noqa: E501
        """OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._namespace = None
        self._node = None
        self._policy = None
        self._service_account = None
        self._workload_endpoint = None
        self.discriminator = None

        if namespace is not None:
            self.namespace = namespace
        if node is not None:
            self.node = node
        if policy is not None:
            self.policy = policy
        if service_account is not None:
            self.service_account = service_account
        if workload_endpoint is not None:
            self.workload_endpoint = workload_endpoint

    @property
    def namespace(self):
        """Gets the namespace of this OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers.  # noqa: E501


        :return: The namespace of this OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers.  # noqa: E501
        :rtype: OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllersNamespace
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers.


        :param namespace: The namespace of this OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers.  # noqa: E501
        :type: OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllersNamespace
        """

        self._namespace = namespace

    @property
    def node(self):
        """Gets the node of this OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers.  # noqa: E501


        :return: The node of this OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers.  # noqa: E501
        :rtype: OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllersNode
        """
        return self._node

    @node.setter
    def node(self, node):
        """Sets the node of this OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers.


        :param node: The node of this OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers.  # noqa: E501
        :type: OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllersNode
        """

        self._node = node

    @property
    def policy(self):
        """Gets the policy of this OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers.  # noqa: E501


        :return: The policy of this OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers.  # noqa: E501
        :rtype: OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllersPolicy
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers.


        :param policy: The policy of this OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers.  # noqa: E501
        :type: OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllersPolicy
        """

        self._policy = policy

    @property
    def service_account(self):
        """Gets the service_account of this OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers.  # noqa: E501


        :return: The service_account of this OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers.  # noqa: E501
        :rtype: OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllersServiceAccount
        """
        return self._service_account

    @service_account.setter
    def service_account(self, service_account):
        """Sets the service_account of this OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers.


        :param service_account: The service_account of this OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers.  # noqa: E501
        :type: OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllersServiceAccount
        """

        self._service_account = service_account

    @property
    def workload_endpoint(self):
        """Gets the workload_endpoint of this OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers.  # noqa: E501


        :return: The workload_endpoint of this OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers.  # noqa: E501
        :rtype: OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllersWorkloadEndpoint
        """
        return self._workload_endpoint

    @workload_endpoint.setter
    def workload_endpoint(self, workload_endpoint):
        """Sets the workload_endpoint of this OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers.


        :param workload_endpoint: The workload_endpoint of this OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers.  # noqa: E501
        :type: OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllersWorkloadEndpoint
        """

        self._workload_endpoint = workload_endpoint

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
        if not isinstance(other, OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers):
            return True

        return self.to_dict() != other.to_dict()
