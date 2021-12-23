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


class IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecCloudInit(object):
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
        'insecure_skip_secrets_manager': 'bool',
        'secret_count': 'int',
        'secret_prefix': 'str',
        'secure_secrets_backend': 'str'
    }

    attribute_map = {
        'insecure_skip_secrets_manager': 'insecureSkipSecretsManager',
        'secret_count': 'secretCount',
        'secret_prefix': 'secretPrefix',
        'secure_secrets_backend': 'secureSecretsBackend'
    }

    def __init__(self, insecure_skip_secrets_manager=None, secret_count=None, secret_prefix=None, secure_secrets_backend=None, local_vars_configuration=None):  # noqa: E501
        """IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecCloudInit - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._insecure_skip_secrets_manager = None
        self._secret_count = None
        self._secret_prefix = None
        self._secure_secrets_backend = None
        self.discriminator = None

        if insecure_skip_secrets_manager is not None:
            self.insecure_skip_secrets_manager = insecure_skip_secrets_manager
        if secret_count is not None:
            self.secret_count = secret_count
        if secret_prefix is not None:
            self.secret_prefix = secret_prefix
        if secure_secrets_backend is not None:
            self.secure_secrets_backend = secure_secrets_backend

    @property
    def insecure_skip_secrets_manager(self):
        """Gets the insecure_skip_secrets_manager of this IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecCloudInit.  # noqa: E501

        InsecureSkipSecretsManager, when set to true will not use AWS Secrets Manager or AWS Systems Manager Parameter Store to ensure privacy of userdata. By default, a cloud-init boothook shell script is prepended to download the userdata from Secrets Manager and additionally delete the secret.  # noqa: E501

        :return: The insecure_skip_secrets_manager of this IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecCloudInit.  # noqa: E501
        :rtype: bool
        """
        return self._insecure_skip_secrets_manager

    @insecure_skip_secrets_manager.setter
    def insecure_skip_secrets_manager(self, insecure_skip_secrets_manager):
        """Sets the insecure_skip_secrets_manager of this IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecCloudInit.

        InsecureSkipSecretsManager, when set to true will not use AWS Secrets Manager or AWS Systems Manager Parameter Store to ensure privacy of userdata. By default, a cloud-init boothook shell script is prepended to download the userdata from Secrets Manager and additionally delete the secret.  # noqa: E501

        :param insecure_skip_secrets_manager: The insecure_skip_secrets_manager of this IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecCloudInit.  # noqa: E501
        :type: bool
        """

        self._insecure_skip_secrets_manager = insecure_skip_secrets_manager

    @property
    def secret_count(self):
        """Gets the secret_count of this IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecCloudInit.  # noqa: E501

        SecretCount is the number of secrets used to form the complete secret  # noqa: E501

        :return: The secret_count of this IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecCloudInit.  # noqa: E501
        :rtype: int
        """
        return self._secret_count

    @secret_count.setter
    def secret_count(self, secret_count):
        """Sets the secret_count of this IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecCloudInit.

        SecretCount is the number of secrets used to form the complete secret  # noqa: E501

        :param secret_count: The secret_count of this IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecCloudInit.  # noqa: E501
        :type: int
        """

        self._secret_count = secret_count

    @property
    def secret_prefix(self):
        """Gets the secret_prefix of this IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecCloudInit.  # noqa: E501

        SecretPrefix is the prefix for the secret name. This is stored temporarily, and deleted when the machine registers as a node against the workload cluster.  # noqa: E501

        :return: The secret_prefix of this IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecCloudInit.  # noqa: E501
        :rtype: str
        """
        return self._secret_prefix

    @secret_prefix.setter
    def secret_prefix(self, secret_prefix):
        """Sets the secret_prefix of this IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecCloudInit.

        SecretPrefix is the prefix for the secret name. This is stored temporarily, and deleted when the machine registers as a node against the workload cluster.  # noqa: E501

        :param secret_prefix: The secret_prefix of this IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecCloudInit.  # noqa: E501
        :type: str
        """

        self._secret_prefix = secret_prefix

    @property
    def secure_secrets_backend(self):
        """Gets the secure_secrets_backend of this IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecCloudInit.  # noqa: E501

        SecureSecretsBackend, when set to parameter-store will utilize the AWS Systems Manager Parameter Storage to distribute secrets. By default or with the value of secrets-manager, will use AWS Secrets Manager instead.  # noqa: E501

        :return: The secure_secrets_backend of this IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecCloudInit.  # noqa: E501
        :rtype: str
        """
        return self._secure_secrets_backend

    @secure_secrets_backend.setter
    def secure_secrets_backend(self, secure_secrets_backend):
        """Sets the secure_secrets_backend of this IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecCloudInit.

        SecureSecretsBackend, when set to parameter-store will utilize the AWS Systems Manager Parameter Storage to distribute secrets. By default or with the value of secrets-manager, will use AWS Secrets Manager instead.  # noqa: E501

        :param secure_secrets_backend: The secure_secrets_backend of this IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecCloudInit.  # noqa: E501
        :type: str
        """
        allowed_values = ["secrets-manager", "ssm-parameter-store"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and secure_secrets_backend not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `secure_secrets_backend` ({0}), must be one of {1}"  # noqa: E501
                .format(secure_secrets_backend, allowed_values)
            )

        self._secure_secrets_backend = secure_secrets_backend

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
        if not isinstance(other, IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecCloudInit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecCloudInit):
            return True

        return self.to_dict() != other.to_dict()
