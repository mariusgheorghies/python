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


class IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAzurekv(object):
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
        'auth_secret_ref': 'IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAzurekvAuthSecretRef',
        'auth_type': 'str',
        'environment_type': 'str',
        'identity_id': 'str',
        'service_account_ref': 'IoExternalSecretsGeneratorsV1alpha1ACRAccessTokenSpecAuthWorkloadIdentityServiceAccountRef',
        'tenant_id': 'str',
        'vault_url': 'str'
    }

    attribute_map = {
        'auth_secret_ref': 'authSecretRef',
        'auth_type': 'authType',
        'environment_type': 'environmentType',
        'identity_id': 'identityId',
        'service_account_ref': 'serviceAccountRef',
        'tenant_id': 'tenantId',
        'vault_url': 'vaultUrl'
    }

    def __init__(self, auth_secret_ref=None, auth_type=None, environment_type=None, identity_id=None, service_account_ref=None, tenant_id=None, vault_url=None, local_vars_configuration=None):  # noqa: E501
        """IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAzurekv - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._auth_secret_ref = None
        self._auth_type = None
        self._environment_type = None
        self._identity_id = None
        self._service_account_ref = None
        self._tenant_id = None
        self._vault_url = None
        self.discriminator = None

        if auth_secret_ref is not None:
            self.auth_secret_ref = auth_secret_ref
        if auth_type is not None:
            self.auth_type = auth_type
        if environment_type is not None:
            self.environment_type = environment_type
        if identity_id is not None:
            self.identity_id = identity_id
        if service_account_ref is not None:
            self.service_account_ref = service_account_ref
        if tenant_id is not None:
            self.tenant_id = tenant_id
        self.vault_url = vault_url

    @property
    def auth_secret_ref(self):
        """Gets the auth_secret_ref of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAzurekv.  # noqa: E501


        :return: The auth_secret_ref of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAzurekv.  # noqa: E501
        :rtype: IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAzurekvAuthSecretRef
        """
        return self._auth_secret_ref

    @auth_secret_ref.setter
    def auth_secret_ref(self, auth_secret_ref):
        """Sets the auth_secret_ref of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAzurekv.


        :param auth_secret_ref: The auth_secret_ref of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAzurekv.  # noqa: E501
        :type: IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAzurekvAuthSecretRef
        """

        self._auth_secret_ref = auth_secret_ref

    @property
    def auth_type(self):
        """Gets the auth_type of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAzurekv.  # noqa: E501

        Auth type defines how to authenticate to the keyvault service. Valid values are: - \"ServicePrincipal\" (default): Using a service principal (tenantId, clientId, clientSecret) - \"ManagedIdentity\": Using Managed Identity assigned to the pod (see aad-pod-identity)  # noqa: E501

        :return: The auth_type of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAzurekv.  # noqa: E501
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAzurekv.

        Auth type defines how to authenticate to the keyvault service. Valid values are: - \"ServicePrincipal\" (default): Using a service principal (tenantId, clientId, clientSecret) - \"ManagedIdentity\": Using Managed Identity assigned to the pod (see aad-pod-identity)  # noqa: E501

        :param auth_type: The auth_type of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAzurekv.  # noqa: E501
        :type: str
        """
        allowed_values = ["ServicePrincipal", "ManagedIdentity", "WorkloadIdentity"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and auth_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `auth_type` ({0}), must be one of {1}"  # noqa: E501
                .format(auth_type, allowed_values)
            )

        self._auth_type = auth_type

    @property
    def environment_type(self):
        """Gets the environment_type of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAzurekv.  # noqa: E501

        EnvironmentType specifies the Azure cloud environment endpoints to use for connecting and authenticating with Azure. By default it points to the public cloud AAD endpoint. The following endpoints are available, also see here: https://github.com/Azure/go-autorest/blob/main/autorest/azure/environments.go#L152 PublicCloud, USGovernmentCloud, ChinaCloud, GermanCloud  # noqa: E501

        :return: The environment_type of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAzurekv.  # noqa: E501
        :rtype: str
        """
        return self._environment_type

    @environment_type.setter
    def environment_type(self, environment_type):
        """Sets the environment_type of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAzurekv.

        EnvironmentType specifies the Azure cloud environment endpoints to use for connecting and authenticating with Azure. By default it points to the public cloud AAD endpoint. The following endpoints are available, also see here: https://github.com/Azure/go-autorest/blob/main/autorest/azure/environments.go#L152 PublicCloud, USGovernmentCloud, ChinaCloud, GermanCloud  # noqa: E501

        :param environment_type: The environment_type of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAzurekv.  # noqa: E501
        :type: str
        """
        allowed_values = ["PublicCloud", "USGovernmentCloud", "ChinaCloud", "GermanCloud"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and environment_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `environment_type` ({0}), must be one of {1}"  # noqa: E501
                .format(environment_type, allowed_values)
            )

        self._environment_type = environment_type

    @property
    def identity_id(self):
        """Gets the identity_id of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAzurekv.  # noqa: E501

        If multiple Managed Identity is assigned to the pod, you can select the one to be used  # noqa: E501

        :return: The identity_id of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAzurekv.  # noqa: E501
        :rtype: str
        """
        return self._identity_id

    @identity_id.setter
    def identity_id(self, identity_id):
        """Sets the identity_id of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAzurekv.

        If multiple Managed Identity is assigned to the pod, you can select the one to be used  # noqa: E501

        :param identity_id: The identity_id of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAzurekv.  # noqa: E501
        :type: str
        """

        self._identity_id = identity_id

    @property
    def service_account_ref(self):
        """Gets the service_account_ref of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAzurekv.  # noqa: E501


        :return: The service_account_ref of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAzurekv.  # noqa: E501
        :rtype: IoExternalSecretsGeneratorsV1alpha1ACRAccessTokenSpecAuthWorkloadIdentityServiceAccountRef
        """
        return self._service_account_ref

    @service_account_ref.setter
    def service_account_ref(self, service_account_ref):
        """Sets the service_account_ref of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAzurekv.


        :param service_account_ref: The service_account_ref of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAzurekv.  # noqa: E501
        :type: IoExternalSecretsGeneratorsV1alpha1ACRAccessTokenSpecAuthWorkloadIdentityServiceAccountRef
        """

        self._service_account_ref = service_account_ref

    @property
    def tenant_id(self):
        """Gets the tenant_id of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAzurekv.  # noqa: E501

        TenantID configures the Azure Tenant to send requests to. Required for ServicePrincipal auth type.  # noqa: E501

        :return: The tenant_id of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAzurekv.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAzurekv.

        TenantID configures the Azure Tenant to send requests to. Required for ServicePrincipal auth type.  # noqa: E501

        :param tenant_id: The tenant_id of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAzurekv.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def vault_url(self):
        """Gets the vault_url of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAzurekv.  # noqa: E501

        Vault Url from which the secrets to be fetched from.  # noqa: E501

        :return: The vault_url of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAzurekv.  # noqa: E501
        :rtype: str
        """
        return self._vault_url

    @vault_url.setter
    def vault_url(self, vault_url):
        """Sets the vault_url of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAzurekv.

        Vault Url from which the secrets to be fetched from.  # noqa: E501

        :param vault_url: The vault_url of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAzurekv.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and vault_url is None:  # noqa: E501
            raise ValueError("Invalid value for `vault_url`, must not be `None`")  # noqa: E501

        self._vault_url = vault_url

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
        if not isinstance(other, IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAzurekv):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAzurekv):
            return True

        return self.to_dict() != other.to_dict()