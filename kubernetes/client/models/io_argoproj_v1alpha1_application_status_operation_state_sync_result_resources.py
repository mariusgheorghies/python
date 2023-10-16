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


class IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources(object):
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
        'group': 'str',
        'hook_phase': 'str',
        'hook_type': 'str',
        'kind': 'str',
        'message': 'str',
        'name': 'str',
        'namespace': 'str',
        'status': 'str',
        'sync_phase': 'str',
        'version': 'str'
    }

    attribute_map = {
        'group': 'group',
        'hook_phase': 'hookPhase',
        'hook_type': 'hookType',
        'kind': 'kind',
        'message': 'message',
        'name': 'name',
        'namespace': 'namespace',
        'status': 'status',
        'sync_phase': 'syncPhase',
        'version': 'version'
    }

    def __init__(self, group=None, hook_phase=None, hook_type=None, kind=None, message=None, name=None, namespace=None, status=None, sync_phase=None, version=None, local_vars_configuration=None):  # noqa: E501
        """IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._group = None
        self._hook_phase = None
        self._hook_type = None
        self._kind = None
        self._message = None
        self._name = None
        self._namespace = None
        self._status = None
        self._sync_phase = None
        self._version = None
        self.discriminator = None

        self.group = group
        if hook_phase is not None:
            self.hook_phase = hook_phase
        if hook_type is not None:
            self.hook_type = hook_type
        self.kind = kind
        if message is not None:
            self.message = message
        self.name = name
        self.namespace = namespace
        if status is not None:
            self.status = status
        if sync_phase is not None:
            self.sync_phase = sync_phase
        self.version = version

    @property
    def group(self):
        """Gets the group of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.  # noqa: E501

        Group specifies the API group of the resource  # noqa: E501

        :return: The group of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.

        Group specifies the API group of the resource  # noqa: E501

        :param group: The group of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and group is None:  # noqa: E501
            raise ValueError("Invalid value for `group`, must not be `None`")  # noqa: E501

        self._group = group

    @property
    def hook_phase(self):
        """Gets the hook_phase of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.  # noqa: E501

        HookPhase contains the state of any operation associated with this resource OR hook This can also contain values for non-hook resources.  # noqa: E501

        :return: The hook_phase of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.  # noqa: E501
        :rtype: str
        """
        return self._hook_phase

    @hook_phase.setter
    def hook_phase(self, hook_phase):
        """Sets the hook_phase of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.

        HookPhase contains the state of any operation associated with this resource OR hook This can also contain values for non-hook resources.  # noqa: E501

        :param hook_phase: The hook_phase of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.  # noqa: E501
        :type: str
        """

        self._hook_phase = hook_phase

    @property
    def hook_type(self):
        """Gets the hook_type of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.  # noqa: E501

        HookType specifies the type of the hook. Empty for non-hook resources  # noqa: E501

        :return: The hook_type of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.  # noqa: E501
        :rtype: str
        """
        return self._hook_type

    @hook_type.setter
    def hook_type(self, hook_type):
        """Sets the hook_type of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.

        HookType specifies the type of the hook. Empty for non-hook resources  # noqa: E501

        :param hook_type: The hook_type of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.  # noqa: E501
        :type: str
        """

        self._hook_type = hook_type

    @property
    def kind(self):
        """Gets the kind of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.  # noqa: E501

        Kind specifies the API kind of the resource  # noqa: E501

        :return: The kind of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.

        Kind specifies the API kind of the resource  # noqa: E501

        :param kind: The kind of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and kind is None:  # noqa: E501
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501

        self._kind = kind

    @property
    def message(self):
        """Gets the message of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.  # noqa: E501

        Message contains an informational or error message for the last sync OR operation  # noqa: E501

        :return: The message of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.

        Message contains an informational or error message for the last sync OR operation  # noqa: E501

        :param message: The message of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def name(self):
        """Gets the name of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.  # noqa: E501

        Name specifies the name of the resource  # noqa: E501

        :return: The name of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.

        Name specifies the name of the resource  # noqa: E501

        :param name: The name of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.  # noqa: E501

        Namespace specifies the target namespace of the resource  # noqa: E501

        :return: The namespace of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.

        Namespace specifies the target namespace of the resource  # noqa: E501

        :param namespace: The namespace of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and namespace is None:  # noqa: E501
            raise ValueError("Invalid value for `namespace`, must not be `None`")  # noqa: E501

        self._namespace = namespace

    @property
    def status(self):
        """Gets the status of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.  # noqa: E501

        Status holds the final result of the sync. Will be empty if the resources is yet to be applied/pruned and is always zero-value for hooks  # noqa: E501

        :return: The status of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.

        Status holds the final result of the sync. Will be empty if the resources is yet to be applied/pruned and is always zero-value for hooks  # noqa: E501

        :param status: The status of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def sync_phase(self):
        """Gets the sync_phase of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.  # noqa: E501

        SyncPhase indicates the particular phase of the sync that this result was acquired in  # noqa: E501

        :return: The sync_phase of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.  # noqa: E501
        :rtype: str
        """
        return self._sync_phase

    @sync_phase.setter
    def sync_phase(self, sync_phase):
        """Sets the sync_phase of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.

        SyncPhase indicates the particular phase of the sync that this result was acquired in  # noqa: E501

        :param sync_phase: The sync_phase of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.  # noqa: E501
        :type: str
        """

        self._sync_phase = sync_phase

    @property
    def version(self):
        """Gets the version of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.  # noqa: E501

        Version specifies the API version of the resource  # noqa: E501

        :return: The version of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.

        Version specifies the API version of the resource  # noqa: E501

        :param version: The version of this IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.  # noqa: E501
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
        if not isinstance(other, IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources):
            return True

        return self.to_dict() != other.to_dict()
