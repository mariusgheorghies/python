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


class ComGrafanaMonitoringV1alpha1IntegrationSpec(object):
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
        'config': 'object',
        'config_maps': 'list[ComGrafanaMonitoringV1alpha1IntegrationSpecConfigMaps]',
        'name': 'str',
        'secrets': 'list[ComGrafanaMonitoringV1alpha1IntegrationSpecSecrets]',
        'type': 'ComGrafanaMonitoringV1alpha1IntegrationSpecType',
        'volume_mounts': 'list[ComCoreosMonitoringV1AlertmanagerSpecVolumeMounts]',
        'volumes': 'list[ComGrafanaMonitoringV1alpha1GrafanaAgentSpecVolumes]'
    }

    attribute_map = {
        'config': 'config',
        'config_maps': 'configMaps',
        'name': 'name',
        'secrets': 'secrets',
        'type': 'type',
        'volume_mounts': 'volumeMounts',
        'volumes': 'volumes'
    }

    def __init__(self, config=None, config_maps=None, name=None, secrets=None, type=None, volume_mounts=None, volumes=None, local_vars_configuration=None):  # noqa: E501
        """ComGrafanaMonitoringV1alpha1IntegrationSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._config = None
        self._config_maps = None
        self._name = None
        self._secrets = None
        self._type = None
        self._volume_mounts = None
        self._volumes = None
        self.discriminator = None

        self.config = config
        if config_maps is not None:
            self.config_maps = config_maps
        self.name = name
        if secrets is not None:
            self.secrets = secrets
        self.type = type
        if volume_mounts is not None:
            self.volume_mounts = volume_mounts
        if volumes is not None:
            self.volumes = volumes

    @property
    def config(self):
        """Gets the config of this ComGrafanaMonitoringV1alpha1IntegrationSpec.  # noqa: E501

        The configuration for the named integration. Note that Integrations are deployed with the integrations-next feature flag, which has different common settings:   https://grafana.com/docs/agent/latest/configuration/integrations/integrations-next/  # noqa: E501

        :return: The config of this ComGrafanaMonitoringV1alpha1IntegrationSpec.  # noqa: E501
        :rtype: object
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this ComGrafanaMonitoringV1alpha1IntegrationSpec.

        The configuration for the named integration. Note that Integrations are deployed with the integrations-next feature flag, which has different common settings:   https://grafana.com/docs/agent/latest/configuration/integrations/integrations-next/  # noqa: E501

        :param config: The config of this ComGrafanaMonitoringV1alpha1IntegrationSpec.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and config is None:  # noqa: E501
            raise ValueError("Invalid value for `config`, must not be `None`")  # noqa: E501

        self._config = config

    @property
    def config_maps(self):
        """Gets the config_maps of this ComGrafanaMonitoringV1alpha1IntegrationSpec.  # noqa: E501

        An extra list of keys from ConfigMaps in the same namespace as the Integration which will be mounted into the Grafana Agent pod running this Integration.   ConfigMaps are mounted at /etc/grafana-agent/integrations/configMaps/<configmap_namespace>/<configmap_name>/<key>.  # noqa: E501

        :return: The config_maps of this ComGrafanaMonitoringV1alpha1IntegrationSpec.  # noqa: E501
        :rtype: list[ComGrafanaMonitoringV1alpha1IntegrationSpecConfigMaps]
        """
        return self._config_maps

    @config_maps.setter
    def config_maps(self, config_maps):
        """Sets the config_maps of this ComGrafanaMonitoringV1alpha1IntegrationSpec.

        An extra list of keys from ConfigMaps in the same namespace as the Integration which will be mounted into the Grafana Agent pod running this Integration.   ConfigMaps are mounted at /etc/grafana-agent/integrations/configMaps/<configmap_namespace>/<configmap_name>/<key>.  # noqa: E501

        :param config_maps: The config_maps of this ComGrafanaMonitoringV1alpha1IntegrationSpec.  # noqa: E501
        :type: list[ComGrafanaMonitoringV1alpha1IntegrationSpecConfigMaps]
        """

        self._config_maps = config_maps

    @property
    def name(self):
        """Gets the name of this ComGrafanaMonitoringV1alpha1IntegrationSpec.  # noqa: E501

        Name of the integration to run (e.g., \"node_exporter\", \"mysqld_exporter\").  # noqa: E501

        :return: The name of this ComGrafanaMonitoringV1alpha1IntegrationSpec.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComGrafanaMonitoringV1alpha1IntegrationSpec.

        Name of the integration to run (e.g., \"node_exporter\", \"mysqld_exporter\").  # noqa: E501

        :param name: The name of this ComGrafanaMonitoringV1alpha1IntegrationSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def secrets(self):
        """Gets the secrets of this ComGrafanaMonitoringV1alpha1IntegrationSpec.  # noqa: E501

        An extra list of keys from Secrets in the same namespace as the Integration which will be mounted into the Grafana Agent pod running this Integration.   Secrets will be mounted at /etc/grafana-agent/integrations/secrets/<secret_namespace>/<secret_name>/<key>.  # noqa: E501

        :return: The secrets of this ComGrafanaMonitoringV1alpha1IntegrationSpec.  # noqa: E501
        :rtype: list[ComGrafanaMonitoringV1alpha1IntegrationSpecSecrets]
        """
        return self._secrets

    @secrets.setter
    def secrets(self, secrets):
        """Sets the secrets of this ComGrafanaMonitoringV1alpha1IntegrationSpec.

        An extra list of keys from Secrets in the same namespace as the Integration which will be mounted into the Grafana Agent pod running this Integration.   Secrets will be mounted at /etc/grafana-agent/integrations/secrets/<secret_namespace>/<secret_name>/<key>.  # noqa: E501

        :param secrets: The secrets of this ComGrafanaMonitoringV1alpha1IntegrationSpec.  # noqa: E501
        :type: list[ComGrafanaMonitoringV1alpha1IntegrationSpecSecrets]
        """

        self._secrets = secrets

    @property
    def type(self):
        """Gets the type of this ComGrafanaMonitoringV1alpha1IntegrationSpec.  # noqa: E501


        :return: The type of this ComGrafanaMonitoringV1alpha1IntegrationSpec.  # noqa: E501
        :rtype: ComGrafanaMonitoringV1alpha1IntegrationSpecType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ComGrafanaMonitoringV1alpha1IntegrationSpec.


        :param type: The type of this ComGrafanaMonitoringV1alpha1IntegrationSpec.  # noqa: E501
        :type: ComGrafanaMonitoringV1alpha1IntegrationSpecType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def volume_mounts(self):
        """Gets the volume_mounts of this ComGrafanaMonitoringV1alpha1IntegrationSpec.  # noqa: E501

        An extra list of VolumeMounts to be associated with the Grafana Agent pods running this integration. VolumeMount names are mutated to be unique across all used IntegrationSpecs.   Mount paths should include the namespace/name of the Integration CR to avoid potentially colliding with other resources.  # noqa: E501

        :return: The volume_mounts of this ComGrafanaMonitoringV1alpha1IntegrationSpec.  # noqa: E501
        :rtype: list[ComCoreosMonitoringV1AlertmanagerSpecVolumeMounts]
        """
        return self._volume_mounts

    @volume_mounts.setter
    def volume_mounts(self, volume_mounts):
        """Sets the volume_mounts of this ComGrafanaMonitoringV1alpha1IntegrationSpec.

        An extra list of VolumeMounts to be associated with the Grafana Agent pods running this integration. VolumeMount names are mutated to be unique across all used IntegrationSpecs.   Mount paths should include the namespace/name of the Integration CR to avoid potentially colliding with other resources.  # noqa: E501

        :param volume_mounts: The volume_mounts of this ComGrafanaMonitoringV1alpha1IntegrationSpec.  # noqa: E501
        :type: list[ComCoreosMonitoringV1AlertmanagerSpecVolumeMounts]
        """

        self._volume_mounts = volume_mounts

    @property
    def volumes(self):
        """Gets the volumes of this ComGrafanaMonitoringV1alpha1IntegrationSpec.  # noqa: E501

        An extra list of Volumes to be associated with the Grafana Agent pods running this integration. Volume names are mutated to be unique across all Integrations. Note that the specified volumes should be able to tolerate existing on multiple pods at once when type is daemonset.   Don't use volumes for loading Secrets or ConfigMaps from the same namespace as the Integration; use the Secrets and ConfigMaps fields instead.  # noqa: E501

        :return: The volumes of this ComGrafanaMonitoringV1alpha1IntegrationSpec.  # noqa: E501
        :rtype: list[ComGrafanaMonitoringV1alpha1GrafanaAgentSpecVolumes]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this ComGrafanaMonitoringV1alpha1IntegrationSpec.

        An extra list of Volumes to be associated with the Grafana Agent pods running this integration. Volume names are mutated to be unique across all Integrations. Note that the specified volumes should be able to tolerate existing on multiple pods at once when type is daemonset.   Don't use volumes for loading Secrets or ConfigMaps from the same namespace as the Integration; use the Secrets and ConfigMaps fields instead.  # noqa: E501

        :param volumes: The volumes of this ComGrafanaMonitoringV1alpha1IntegrationSpec.  # noqa: E501
        :type: list[ComGrafanaMonitoringV1alpha1GrafanaAgentSpecVolumes]
        """

        self._volumes = volumes

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
        if not isinstance(other, ComGrafanaMonitoringV1alpha1IntegrationSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComGrafanaMonitoringV1alpha1IntegrationSpec):
            return True

        return self.to_dict() != other.to_dict()