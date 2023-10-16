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


class IoTigeraOperatorV1ImageSetSpecImages(object):
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
        'digest': 'str',
        'image': 'str'
    }

    attribute_map = {
        'digest': 'digest',
        'image': 'image'
    }

    def __init__(self, digest=None, image=None, local_vars_configuration=None):  # noqa: E501
        """IoTigeraOperatorV1ImageSetSpecImages - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._digest = None
        self._image = None
        self.discriminator = None

        self.digest = digest
        self.image = image

    @property
    def digest(self):
        """Gets the digest of this IoTigeraOperatorV1ImageSetSpecImages.  # noqa: E501

        Digest is the image identifier that will be used for the Image. The field should not include a leading `@` and must be prefixed with `sha256:`.  # noqa: E501

        :return: The digest of this IoTigeraOperatorV1ImageSetSpecImages.  # noqa: E501
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """Sets the digest of this IoTigeraOperatorV1ImageSetSpecImages.

        Digest is the image identifier that will be used for the Image. The field should not include a leading `@` and must be prefixed with `sha256:`.  # noqa: E501

        :param digest: The digest of this IoTigeraOperatorV1ImageSetSpecImages.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and digest is None:  # noqa: E501
            raise ValueError("Invalid value for `digest`, must not be `None`")  # noqa: E501

        self._digest = digest

    @property
    def image(self):
        """Gets the image of this IoTigeraOperatorV1ImageSetSpecImages.  # noqa: E501

        Image is an image that the operator deploys and instead of using the built in tag the operator will use the Digest for the image identifier. The value should be the image name without registry or tag or digest. For the image `docker.io/calico/node:v3.17.1` it should be represented as `calico/node`  # noqa: E501

        :return: The image of this IoTigeraOperatorV1ImageSetSpecImages.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this IoTigeraOperatorV1ImageSetSpecImages.

        Image is an image that the operator deploys and instead of using the built in tag the operator will use the Digest for the image identifier. The value should be the image name without registry or tag or digest. For the image `docker.io/calico/node:v3.17.1` it should be represented as `calico/node`  # noqa: E501

        :param image: The image of this IoTigeraOperatorV1ImageSetSpecImages.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and image is None:  # noqa: E501
            raise ValueError("Invalid value for `image`, must not be `None`")  # noqa: E501

        self._image = image

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
        if not isinstance(other, IoTigeraOperatorV1ImageSetSpecImages):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoTigeraOperatorV1ImageSetSpecImages):
            return True

        return self.to_dict() != other.to_dict()