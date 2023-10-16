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


class IoCertManagerAcmeV1ChallengeSpecSolverHttp01Ingress(object):
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
        '_class': 'str',
        'ingress_template': 'IoCertManagerAcmeV1ChallengeSpecSolverHttp01IngressIngressTemplate',
        'name': 'str',
        'pod_template': 'IoCertManagerAcmeV1ChallengeSpecSolverHttp01IngressPodTemplate',
        'service_type': 'str'
    }

    attribute_map = {
        '_class': 'class',
        'ingress_template': 'ingressTemplate',
        'name': 'name',
        'pod_template': 'podTemplate',
        'service_type': 'serviceType'
    }

    def __init__(self, _class=None, ingress_template=None, name=None, pod_template=None, service_type=None, local_vars_configuration=None):  # noqa: E501
        """IoCertManagerAcmeV1ChallengeSpecSolverHttp01Ingress - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self.__class = None
        self._ingress_template = None
        self._name = None
        self._pod_template = None
        self._service_type = None
        self.discriminator = None

        if _class is not None:
            self._class = _class
        if ingress_template is not None:
            self.ingress_template = ingress_template
        if name is not None:
            self.name = name
        if pod_template is not None:
            self.pod_template = pod_template
        if service_type is not None:
            self.service_type = service_type

    @property
    def _class(self):
        """Gets the _class of this IoCertManagerAcmeV1ChallengeSpecSolverHttp01Ingress.  # noqa: E501

        The ingress class to use when creating Ingress resources to solve ACME challenges that use this challenge solver. Only one of 'class' or 'name' may be specified.  # noqa: E501

        :return: The _class of this IoCertManagerAcmeV1ChallengeSpecSolverHttp01Ingress.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this IoCertManagerAcmeV1ChallengeSpecSolverHttp01Ingress.

        The ingress class to use when creating Ingress resources to solve ACME challenges that use this challenge solver. Only one of 'class' or 'name' may be specified.  # noqa: E501

        :param _class: The _class of this IoCertManagerAcmeV1ChallengeSpecSolverHttp01Ingress.  # noqa: E501
        :type: str
        """

        self.__class = _class

    @property
    def ingress_template(self):
        """Gets the ingress_template of this IoCertManagerAcmeV1ChallengeSpecSolverHttp01Ingress.  # noqa: E501


        :return: The ingress_template of this IoCertManagerAcmeV1ChallengeSpecSolverHttp01Ingress.  # noqa: E501
        :rtype: IoCertManagerAcmeV1ChallengeSpecSolverHttp01IngressIngressTemplate
        """
        return self._ingress_template

    @ingress_template.setter
    def ingress_template(self, ingress_template):
        """Sets the ingress_template of this IoCertManagerAcmeV1ChallengeSpecSolverHttp01Ingress.


        :param ingress_template: The ingress_template of this IoCertManagerAcmeV1ChallengeSpecSolverHttp01Ingress.  # noqa: E501
        :type: IoCertManagerAcmeV1ChallengeSpecSolverHttp01IngressIngressTemplate
        """

        self._ingress_template = ingress_template

    @property
    def name(self):
        """Gets the name of this IoCertManagerAcmeV1ChallengeSpecSolverHttp01Ingress.  # noqa: E501

        The name of the ingress resource that should have ACME challenge solving routes inserted into it in order to solve HTTP01 challenges. This is typically used in conjunction with ingress controllers like ingress-gce, which maintains a 1:1 mapping between external IPs and ingress resources.  # noqa: E501

        :return: The name of this IoCertManagerAcmeV1ChallengeSpecSolverHttp01Ingress.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IoCertManagerAcmeV1ChallengeSpecSolverHttp01Ingress.

        The name of the ingress resource that should have ACME challenge solving routes inserted into it in order to solve HTTP01 challenges. This is typically used in conjunction with ingress controllers like ingress-gce, which maintains a 1:1 mapping between external IPs and ingress resources.  # noqa: E501

        :param name: The name of this IoCertManagerAcmeV1ChallengeSpecSolverHttp01Ingress.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def pod_template(self):
        """Gets the pod_template of this IoCertManagerAcmeV1ChallengeSpecSolverHttp01Ingress.  # noqa: E501


        :return: The pod_template of this IoCertManagerAcmeV1ChallengeSpecSolverHttp01Ingress.  # noqa: E501
        :rtype: IoCertManagerAcmeV1ChallengeSpecSolverHttp01IngressPodTemplate
        """
        return self._pod_template

    @pod_template.setter
    def pod_template(self, pod_template):
        """Sets the pod_template of this IoCertManagerAcmeV1ChallengeSpecSolverHttp01Ingress.


        :param pod_template: The pod_template of this IoCertManagerAcmeV1ChallengeSpecSolverHttp01Ingress.  # noqa: E501
        :type: IoCertManagerAcmeV1ChallengeSpecSolverHttp01IngressPodTemplate
        """

        self._pod_template = pod_template

    @property
    def service_type(self):
        """Gets the service_type of this IoCertManagerAcmeV1ChallengeSpecSolverHttp01Ingress.  # noqa: E501

        Optional service type for Kubernetes solver service. Supported values are NodePort or ClusterIP. If unset, defaults to NodePort.  # noqa: E501

        :return: The service_type of this IoCertManagerAcmeV1ChallengeSpecSolverHttp01Ingress.  # noqa: E501
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this IoCertManagerAcmeV1ChallengeSpecSolverHttp01Ingress.

        Optional service type for Kubernetes solver service. Supported values are NodePort or ClusterIP. If unset, defaults to NodePort.  # noqa: E501

        :param service_type: The service_type of this IoCertManagerAcmeV1ChallengeSpecSolverHttp01Ingress.  # noqa: E501
        :type: str
        """

        self._service_type = service_type

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
        if not isinstance(other, IoCertManagerAcmeV1ChallengeSpecSolverHttp01Ingress):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoCertManagerAcmeV1ChallengeSpecSolverHttp01Ingress):
            return True

        return self.to_dict() != other.to_dict()
