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


class IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpec(object):
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
        'kubeadm_config_spec': 'IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecKubeadmConfigSpec',
        'machine_template': 'IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecMachineTemplate',
        'replicas': 'int',
        'rollout_after': 'datetime',
        'rollout_strategy': 'IoXK8sClusterControlplaneV1alpha3KubeadmControlPlaneSpecRolloutStrategy',
        'version': 'str'
    }

    attribute_map = {
        'kubeadm_config_spec': 'kubeadmConfigSpec',
        'machine_template': 'machineTemplate',
        'replicas': 'replicas',
        'rollout_after': 'rolloutAfter',
        'rollout_strategy': 'rolloutStrategy',
        'version': 'version'
    }

    def __init__(self, kubeadm_config_spec=None, machine_template=None, replicas=None, rollout_after=None, rollout_strategy=None, version=None, local_vars_configuration=None):  # noqa: E501
        """IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._kubeadm_config_spec = None
        self._machine_template = None
        self._replicas = None
        self._rollout_after = None
        self._rollout_strategy = None
        self._version = None
        self.discriminator = None

        self.kubeadm_config_spec = kubeadm_config_spec
        self.machine_template = machine_template
        if replicas is not None:
            self.replicas = replicas
        if rollout_after is not None:
            self.rollout_after = rollout_after
        if rollout_strategy is not None:
            self.rollout_strategy = rollout_strategy
        self.version = version

    @property
    def kubeadm_config_spec(self):
        """Gets the kubeadm_config_spec of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpec.  # noqa: E501


        :return: The kubeadm_config_spec of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpec.  # noqa: E501
        :rtype: IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecKubeadmConfigSpec
        """
        return self._kubeadm_config_spec

    @kubeadm_config_spec.setter
    def kubeadm_config_spec(self, kubeadm_config_spec):
        """Sets the kubeadm_config_spec of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpec.


        :param kubeadm_config_spec: The kubeadm_config_spec of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpec.  # noqa: E501
        :type: IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecKubeadmConfigSpec
        """
        if self.local_vars_configuration.client_side_validation and kubeadm_config_spec is None:  # noqa: E501
            raise ValueError("Invalid value for `kubeadm_config_spec`, must not be `None`")  # noqa: E501

        self._kubeadm_config_spec = kubeadm_config_spec

    @property
    def machine_template(self):
        """Gets the machine_template of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpec.  # noqa: E501


        :return: The machine_template of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpec.  # noqa: E501
        :rtype: IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecMachineTemplate
        """
        return self._machine_template

    @machine_template.setter
    def machine_template(self, machine_template):
        """Sets the machine_template of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpec.


        :param machine_template: The machine_template of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpec.  # noqa: E501
        :type: IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecMachineTemplate
        """
        if self.local_vars_configuration.client_side_validation and machine_template is None:  # noqa: E501
            raise ValueError("Invalid value for `machine_template`, must not be `None`")  # noqa: E501

        self._machine_template = machine_template

    @property
    def replicas(self):
        """Gets the replicas of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpec.  # noqa: E501

        Number of desired machines. Defaults to 1. When stacked etcd is used only odd numbers are permitted, as per [etcd best practice](https://etcd.io/docs/v3.3.12/faq/#why-an-odd-number-of-cluster-members). This is a pointer to distinguish between explicit zero and not specified.  # noqa: E501

        :return: The replicas of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpec.  # noqa: E501
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpec.

        Number of desired machines. Defaults to 1. When stacked etcd is used only odd numbers are permitted, as per [etcd best practice](https://etcd.io/docs/v3.3.12/faq/#why-an-odd-number-of-cluster-members). This is a pointer to distinguish between explicit zero and not specified.  # noqa: E501

        :param replicas: The replicas of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpec.  # noqa: E501
        :type: int
        """

        self._replicas = replicas

    @property
    def rollout_after(self):
        """Gets the rollout_after of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpec.  # noqa: E501

        RolloutAfter is a field to indicate a rollout should be performed after the specified time even if no changes have been made to the KubeadmControlPlane.  # noqa: E501

        :return: The rollout_after of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpec.  # noqa: E501
        :rtype: datetime
        """
        return self._rollout_after

    @rollout_after.setter
    def rollout_after(self, rollout_after):
        """Sets the rollout_after of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpec.

        RolloutAfter is a field to indicate a rollout should be performed after the specified time even if no changes have been made to the KubeadmControlPlane.  # noqa: E501

        :param rollout_after: The rollout_after of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpec.  # noqa: E501
        :type: datetime
        """

        self._rollout_after = rollout_after

    @property
    def rollout_strategy(self):
        """Gets the rollout_strategy of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpec.  # noqa: E501


        :return: The rollout_strategy of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpec.  # noqa: E501
        :rtype: IoXK8sClusterControlplaneV1alpha3KubeadmControlPlaneSpecRolloutStrategy
        """
        return self._rollout_strategy

    @rollout_strategy.setter
    def rollout_strategy(self, rollout_strategy):
        """Sets the rollout_strategy of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpec.


        :param rollout_strategy: The rollout_strategy of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpec.  # noqa: E501
        :type: IoXK8sClusterControlplaneV1alpha3KubeadmControlPlaneSpecRolloutStrategy
        """

        self._rollout_strategy = rollout_strategy

    @property
    def version(self):
        """Gets the version of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpec.  # noqa: E501

        Version defines the desired Kubernetes version.  # noqa: E501

        :return: The version of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpec.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpec.

        Version defines the desired Kubernetes version.  # noqa: E501

        :param version: The version of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

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
        if not isinstance(other, IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpec):
            return True

        return self.to_dict() != other.to_dict()
