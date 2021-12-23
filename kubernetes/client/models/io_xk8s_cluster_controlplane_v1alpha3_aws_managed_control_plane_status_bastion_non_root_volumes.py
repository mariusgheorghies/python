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


class IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionNonRootVolumes(object):
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
        'device_name': 'str',
        'encrypted': 'bool',
        'encryption_key': 'str',
        'iops': 'int',
        'size': 'int',
        'type': 'str'
    }

    attribute_map = {
        'device_name': 'deviceName',
        'encrypted': 'encrypted',
        'encryption_key': 'encryptionKey',
        'iops': 'iops',
        'size': 'size',
        'type': 'type'
    }

    def __init__(self, device_name=None, encrypted=None, encryption_key=None, iops=None, size=None, type=None, local_vars_configuration=None):  # noqa: E501
        """IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionNonRootVolumes - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._device_name = None
        self._encrypted = None
        self._encryption_key = None
        self._iops = None
        self._size = None
        self._type = None
        self.discriminator = None

        if device_name is not None:
            self.device_name = device_name
        if encrypted is not None:
            self.encrypted = encrypted
        if encryption_key is not None:
            self.encryption_key = encryption_key
        if iops is not None:
            self.iops = iops
        self.size = size
        if type is not None:
            self.type = type

    @property
    def device_name(self):
        """Gets the device_name of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionNonRootVolumes.  # noqa: E501

        Device name  # noqa: E501

        :return: The device_name of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionNonRootVolumes.  # noqa: E501
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionNonRootVolumes.

        Device name  # noqa: E501

        :param device_name: The device_name of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionNonRootVolumes.  # noqa: E501
        :type: str
        """

        self._device_name = device_name

    @property
    def encrypted(self):
        """Gets the encrypted of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionNonRootVolumes.  # noqa: E501

        Encrypted is whether the volume should be encrypted or not.  # noqa: E501

        :return: The encrypted of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionNonRootVolumes.  # noqa: E501
        :rtype: bool
        """
        return self._encrypted

    @encrypted.setter
    def encrypted(self, encrypted):
        """Sets the encrypted of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionNonRootVolumes.

        Encrypted is whether the volume should be encrypted or not.  # noqa: E501

        :param encrypted: The encrypted of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionNonRootVolumes.  # noqa: E501
        :type: bool
        """

        self._encrypted = encrypted

    @property
    def encryption_key(self):
        """Gets the encryption_key of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionNonRootVolumes.  # noqa: E501

        EncryptionKey is the KMS key to use to encrypt the volume. Can be either a KMS key ID or ARN. If Encrypted is set and this is omitted, the default AWS key will be used. The key must already exist and be accessible by the controller.  # noqa: E501

        :return: The encryption_key of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionNonRootVolumes.  # noqa: E501
        :rtype: str
        """
        return self._encryption_key

    @encryption_key.setter
    def encryption_key(self, encryption_key):
        """Sets the encryption_key of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionNonRootVolumes.

        EncryptionKey is the KMS key to use to encrypt the volume. Can be either a KMS key ID or ARN. If Encrypted is set and this is omitted, the default AWS key will be used. The key must already exist and be accessible by the controller.  # noqa: E501

        :param encryption_key: The encryption_key of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionNonRootVolumes.  # noqa: E501
        :type: str
        """

        self._encryption_key = encryption_key

    @property
    def iops(self):
        """Gets the iops of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionNonRootVolumes.  # noqa: E501

        IOPS is the number of IOPS requested for the disk. Not applicable to all types.  # noqa: E501

        :return: The iops of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionNonRootVolumes.  # noqa: E501
        :rtype: int
        """
        return self._iops

    @iops.setter
    def iops(self, iops):
        """Sets the iops of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionNonRootVolumes.

        IOPS is the number of IOPS requested for the disk. Not applicable to all types.  # noqa: E501

        :param iops: The iops of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionNonRootVolumes.  # noqa: E501
        :type: int
        """

        self._iops = iops

    @property
    def size(self):
        """Gets the size of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionNonRootVolumes.  # noqa: E501

        Size specifies size (in Gi) of the storage device. Must be greater than the image snapshot size or 8 (whichever is greater).  # noqa: E501

        :return: The size of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionNonRootVolumes.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionNonRootVolumes.

        Size specifies size (in Gi) of the storage device. Must be greater than the image snapshot size or 8 (whichever is greater).  # noqa: E501

        :param size: The size of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionNonRootVolumes.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and size is None:  # noqa: E501
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                size is not None and size < 8):  # noqa: E501
            raise ValueError("Invalid value for `size`, must be a value greater than or equal to `8`")  # noqa: E501

        self._size = size

    @property
    def type(self):
        """Gets the type of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionNonRootVolumes.  # noqa: E501

        Type is the type of the volume (e.g. gp2, io1, etc...).  # noqa: E501

        :return: The type of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionNonRootVolumes.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionNonRootVolumes.

        Type is the type of the volume (e.g. gp2, io1, etc...).  # noqa: E501

        :param type: The type of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionNonRootVolumes.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionNonRootVolumes):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionNonRootVolumes):
            return True

        return self.to_dict() != other.to_dict()
