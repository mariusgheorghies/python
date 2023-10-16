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


class AwsK8sServicesEc2V1alpha1FlowLogSpec(object):
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
        'deliver_logs_permission_arn': 'str',
        'destination_options': 'AwsK8sServicesEc2V1alpha1FlowLogSpecDestinationOptions',
        'log_destination': 'str',
        'log_destination_type': 'str',
        'log_format': 'str',
        'log_group_name': 'str',
        'max_aggregation_interval': 'int',
        'resource_id': 'str',
        'resource_type': 'str',
        'tags': 'list[AwsK8sServicesEc2V1alpha1DHCPOptionsSpecTags]',
        'traffic_type': 'str'
    }

    attribute_map = {
        'deliver_logs_permission_arn': 'deliverLogsPermissionARN',
        'destination_options': 'destinationOptions',
        'log_destination': 'logDestination',
        'log_destination_type': 'logDestinationType',
        'log_format': 'logFormat',
        'log_group_name': 'logGroupName',
        'max_aggregation_interval': 'maxAggregationInterval',
        'resource_id': 'resourceID',
        'resource_type': 'resourceType',
        'tags': 'tags',
        'traffic_type': 'trafficType'
    }

    def __init__(self, deliver_logs_permission_arn=None, destination_options=None, log_destination=None, log_destination_type=None, log_format=None, log_group_name=None, max_aggregation_interval=None, resource_id=None, resource_type=None, tags=None, traffic_type=None, local_vars_configuration=None):  # noqa: E501
        """AwsK8sServicesEc2V1alpha1FlowLogSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._deliver_logs_permission_arn = None
        self._destination_options = None
        self._log_destination = None
        self._log_destination_type = None
        self._log_format = None
        self._log_group_name = None
        self._max_aggregation_interval = None
        self._resource_id = None
        self._resource_type = None
        self._tags = None
        self._traffic_type = None
        self.discriminator = None

        if deliver_logs_permission_arn is not None:
            self.deliver_logs_permission_arn = deliver_logs_permission_arn
        if destination_options is not None:
            self.destination_options = destination_options
        if log_destination is not None:
            self.log_destination = log_destination
        if log_destination_type is not None:
            self.log_destination_type = log_destination_type
        if log_format is not None:
            self.log_format = log_format
        if log_group_name is not None:
            self.log_group_name = log_group_name
        if max_aggregation_interval is not None:
            self.max_aggregation_interval = max_aggregation_interval
        self.resource_id = resource_id
        self.resource_type = resource_type
        if tags is not None:
            self.tags = tags
        if traffic_type is not None:
            self.traffic_type = traffic_type

    @property
    def deliver_logs_permission_arn(self):
        """Gets the deliver_logs_permission_arn of this AwsK8sServicesEc2V1alpha1FlowLogSpec.  # noqa: E501

        The ARN for the IAM role that permits Amazon EC2 to publish flow logs to a CloudWatch Logs log group in your account.   If you specify LogDestinationType as s3, do not specify DeliverLogsPermissionArn or LogGroupName.  # noqa: E501

        :return: The deliver_logs_permission_arn of this AwsK8sServicesEc2V1alpha1FlowLogSpec.  # noqa: E501
        :rtype: str
        """
        return self._deliver_logs_permission_arn

    @deliver_logs_permission_arn.setter
    def deliver_logs_permission_arn(self, deliver_logs_permission_arn):
        """Sets the deliver_logs_permission_arn of this AwsK8sServicesEc2V1alpha1FlowLogSpec.

        The ARN for the IAM role that permits Amazon EC2 to publish flow logs to a CloudWatch Logs log group in your account.   If you specify LogDestinationType as s3, do not specify DeliverLogsPermissionArn or LogGroupName.  # noqa: E501

        :param deliver_logs_permission_arn: The deliver_logs_permission_arn of this AwsK8sServicesEc2V1alpha1FlowLogSpec.  # noqa: E501
        :type: str
        """

        self._deliver_logs_permission_arn = deliver_logs_permission_arn

    @property
    def destination_options(self):
        """Gets the destination_options of this AwsK8sServicesEc2V1alpha1FlowLogSpec.  # noqa: E501


        :return: The destination_options of this AwsK8sServicesEc2V1alpha1FlowLogSpec.  # noqa: E501
        :rtype: AwsK8sServicesEc2V1alpha1FlowLogSpecDestinationOptions
        """
        return self._destination_options

    @destination_options.setter
    def destination_options(self, destination_options):
        """Sets the destination_options of this AwsK8sServicesEc2V1alpha1FlowLogSpec.


        :param destination_options: The destination_options of this AwsK8sServicesEc2V1alpha1FlowLogSpec.  # noqa: E501
        :type: AwsK8sServicesEc2V1alpha1FlowLogSpecDestinationOptions
        """

        self._destination_options = destination_options

    @property
    def log_destination(self):
        """Gets the log_destination of this AwsK8sServicesEc2V1alpha1FlowLogSpec.  # noqa: E501

        The destination to which the flow log data is to be published. Flow log data can be published to a CloudWatch Logs log group or an Amazon S3 bucket. The value specified for this parameter depends on the value specified for LogDestinationType.   If LogDestinationType is not specified or cloud-watch-logs, specify the Amazon Resource Name (ARN) of the CloudWatch Logs log group. For example, to publish to a log group called my-logs, specify arn:aws:logs:us-east-1:123456789012:log-group:my-logs. Alternatively, use LogGroupName instead.   If LogDestinationType is s3, specify the ARN of the Amazon S3 bucket. You can also specify a subfolder in the bucket. To specify a subfolder in the bucket, use the following ARN format: bucket_ARN/subfolder_name/. For example, to specify a subfolder named my-logs in a bucket named my-bucket, use the following ARN: arn:aws:s3:::my-bucket/my-logs/. You cannot use AWSLogs as a subfolder name. This is a reserved term.  # noqa: E501

        :return: The log_destination of this AwsK8sServicesEc2V1alpha1FlowLogSpec.  # noqa: E501
        :rtype: str
        """
        return self._log_destination

    @log_destination.setter
    def log_destination(self, log_destination):
        """Sets the log_destination of this AwsK8sServicesEc2V1alpha1FlowLogSpec.

        The destination to which the flow log data is to be published. Flow log data can be published to a CloudWatch Logs log group or an Amazon S3 bucket. The value specified for this parameter depends on the value specified for LogDestinationType.   If LogDestinationType is not specified or cloud-watch-logs, specify the Amazon Resource Name (ARN) of the CloudWatch Logs log group. For example, to publish to a log group called my-logs, specify arn:aws:logs:us-east-1:123456789012:log-group:my-logs. Alternatively, use LogGroupName instead.   If LogDestinationType is s3, specify the ARN of the Amazon S3 bucket. You can also specify a subfolder in the bucket. To specify a subfolder in the bucket, use the following ARN format: bucket_ARN/subfolder_name/. For example, to specify a subfolder named my-logs in a bucket named my-bucket, use the following ARN: arn:aws:s3:::my-bucket/my-logs/. You cannot use AWSLogs as a subfolder name. This is a reserved term.  # noqa: E501

        :param log_destination: The log_destination of this AwsK8sServicesEc2V1alpha1FlowLogSpec.  # noqa: E501
        :type: str
        """

        self._log_destination = log_destination

    @property
    def log_destination_type(self):
        """Gets the log_destination_type of this AwsK8sServicesEc2V1alpha1FlowLogSpec.  # noqa: E501

        The type of destination to which the flow log data is to be published. Flow log data can be published to CloudWatch Logs or Amazon S3. To publish flow log data to CloudWatch Logs, specify cloud-watch-logs. To publish flow log data to Amazon S3, specify s3.   If you specify LogDestinationType as s3, do not specify DeliverLogsPermissionArn or LogGroupName.   Default: cloud-watch-logs  # noqa: E501

        :return: The log_destination_type of this AwsK8sServicesEc2V1alpha1FlowLogSpec.  # noqa: E501
        :rtype: str
        """
        return self._log_destination_type

    @log_destination_type.setter
    def log_destination_type(self, log_destination_type):
        """Sets the log_destination_type of this AwsK8sServicesEc2V1alpha1FlowLogSpec.

        The type of destination to which the flow log data is to be published. Flow log data can be published to CloudWatch Logs or Amazon S3. To publish flow log data to CloudWatch Logs, specify cloud-watch-logs. To publish flow log data to Amazon S3, specify s3.   If you specify LogDestinationType as s3, do not specify DeliverLogsPermissionArn or LogGroupName.   Default: cloud-watch-logs  # noqa: E501

        :param log_destination_type: The log_destination_type of this AwsK8sServicesEc2V1alpha1FlowLogSpec.  # noqa: E501
        :type: str
        """

        self._log_destination_type = log_destination_type

    @property
    def log_format(self):
        """Gets the log_format of this AwsK8sServicesEc2V1alpha1FlowLogSpec.  # noqa: E501

        The fields to include in the flow log record, in the order in which they should appear. For a list of available fields, see Flow log records (https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html#flow-log-records). If you omit this parameter, the flow log is created using the default format. If you specify this parameter, you must specify at least one field.   Specify the fields using the ${field-id} format, separated by spaces. For the CLI, surround this parameter value with single quotes on Linux or double quotes on Windows.  # noqa: E501

        :return: The log_format of this AwsK8sServicesEc2V1alpha1FlowLogSpec.  # noqa: E501
        :rtype: str
        """
        return self._log_format

    @log_format.setter
    def log_format(self, log_format):
        """Sets the log_format of this AwsK8sServicesEc2V1alpha1FlowLogSpec.

        The fields to include in the flow log record, in the order in which they should appear. For a list of available fields, see Flow log records (https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html#flow-log-records). If you omit this parameter, the flow log is created using the default format. If you specify this parameter, you must specify at least one field.   Specify the fields using the ${field-id} format, separated by spaces. For the CLI, surround this parameter value with single quotes on Linux or double quotes on Windows.  # noqa: E501

        :param log_format: The log_format of this AwsK8sServicesEc2V1alpha1FlowLogSpec.  # noqa: E501
        :type: str
        """

        self._log_format = log_format

    @property
    def log_group_name(self):
        """Gets the log_group_name of this AwsK8sServicesEc2V1alpha1FlowLogSpec.  # noqa: E501

        The name of a new or existing CloudWatch Logs log group where Amazon EC2 publishes your flow logs.   If you specify LogDestinationType as s3, do not specify DeliverLogsPermissionArn or LogGroupName.  # noqa: E501

        :return: The log_group_name of this AwsK8sServicesEc2V1alpha1FlowLogSpec.  # noqa: E501
        :rtype: str
        """
        return self._log_group_name

    @log_group_name.setter
    def log_group_name(self, log_group_name):
        """Sets the log_group_name of this AwsK8sServicesEc2V1alpha1FlowLogSpec.

        The name of a new or existing CloudWatch Logs log group where Amazon EC2 publishes your flow logs.   If you specify LogDestinationType as s3, do not specify DeliverLogsPermissionArn or LogGroupName.  # noqa: E501

        :param log_group_name: The log_group_name of this AwsK8sServicesEc2V1alpha1FlowLogSpec.  # noqa: E501
        :type: str
        """

        self._log_group_name = log_group_name

    @property
    def max_aggregation_interval(self):
        """Gets the max_aggregation_interval of this AwsK8sServicesEc2V1alpha1FlowLogSpec.  # noqa: E501

        The maximum interval of time during which a flow of packets is captured and aggregated into a flow log record. You can specify 60 seconds (1 minute) or 600 seconds (10 minutes).   When a network interface is attached to a Nitro-based instance (https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#ec2-nitro-instances), the aggregation interval is always 60 seconds or less, regardless of the value that you specify.   Default: 600  # noqa: E501

        :return: The max_aggregation_interval of this AwsK8sServicesEc2V1alpha1FlowLogSpec.  # noqa: E501
        :rtype: int
        """
        return self._max_aggregation_interval

    @max_aggregation_interval.setter
    def max_aggregation_interval(self, max_aggregation_interval):
        """Sets the max_aggregation_interval of this AwsK8sServicesEc2V1alpha1FlowLogSpec.

        The maximum interval of time during which a flow of packets is captured and aggregated into a flow log record. You can specify 60 seconds (1 minute) or 600 seconds (10 minutes).   When a network interface is attached to a Nitro-based instance (https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#ec2-nitro-instances), the aggregation interval is always 60 seconds or less, regardless of the value that you specify.   Default: 600  # noqa: E501

        :param max_aggregation_interval: The max_aggregation_interval of this AwsK8sServicesEc2V1alpha1FlowLogSpec.  # noqa: E501
        :type: int
        """

        self._max_aggregation_interval = max_aggregation_interval

    @property
    def resource_id(self):
        """Gets the resource_id of this AwsK8sServicesEc2V1alpha1FlowLogSpec.  # noqa: E501


        :return: The resource_id of this AwsK8sServicesEc2V1alpha1FlowLogSpec.  # noqa: E501
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this AwsK8sServicesEc2V1alpha1FlowLogSpec.


        :param resource_id: The resource_id of this AwsK8sServicesEc2V1alpha1FlowLogSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and resource_id is None:  # noqa: E501
            raise ValueError("Invalid value for `resource_id`, must not be `None`")  # noqa: E501

        self._resource_id = resource_id

    @property
    def resource_type(self):
        """Gets the resource_type of this AwsK8sServicesEc2V1alpha1FlowLogSpec.  # noqa: E501

        The type of resource for which to create the flow log. For example, if you specified a VPC ID for the ResourceId property, specify VPC for this property.  # noqa: E501

        :return: The resource_type of this AwsK8sServicesEc2V1alpha1FlowLogSpec.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this AwsK8sServicesEc2V1alpha1FlowLogSpec.

        The type of resource for which to create the flow log. For example, if you specified a VPC ID for the ResourceId property, specify VPC for this property.  # noqa: E501

        :param resource_type: The resource_type of this AwsK8sServicesEc2V1alpha1FlowLogSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and resource_type is None:  # noqa: E501
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501

        self._resource_type = resource_type

    @property
    def tags(self):
        """Gets the tags of this AwsK8sServicesEc2V1alpha1FlowLogSpec.  # noqa: E501

        The tags. The value parameter is required, but if you don't want the tag to have a value, specify the parameter with no value, and we set the value to an empty string.  # noqa: E501

        :return: The tags of this AwsK8sServicesEc2V1alpha1FlowLogSpec.  # noqa: E501
        :rtype: list[AwsK8sServicesEc2V1alpha1DHCPOptionsSpecTags]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AwsK8sServicesEc2V1alpha1FlowLogSpec.

        The tags. The value parameter is required, but if you don't want the tag to have a value, specify the parameter with no value, and we set the value to an empty string.  # noqa: E501

        :param tags: The tags of this AwsK8sServicesEc2V1alpha1FlowLogSpec.  # noqa: E501
        :type: list[AwsK8sServicesEc2V1alpha1DHCPOptionsSpecTags]
        """

        self._tags = tags

    @property
    def traffic_type(self):
        """Gets the traffic_type of this AwsK8sServicesEc2V1alpha1FlowLogSpec.  # noqa: E501

        The type of traffic to log. You can log traffic that the resource accepts or rejects, or all traffic.  # noqa: E501

        :return: The traffic_type of this AwsK8sServicesEc2V1alpha1FlowLogSpec.  # noqa: E501
        :rtype: str
        """
        return self._traffic_type

    @traffic_type.setter
    def traffic_type(self, traffic_type):
        """Sets the traffic_type of this AwsK8sServicesEc2V1alpha1FlowLogSpec.

        The type of traffic to log. You can log traffic that the resource accepts or rejects, or all traffic.  # noqa: E501

        :param traffic_type: The traffic_type of this AwsK8sServicesEc2V1alpha1FlowLogSpec.  # noqa: E501
        :type: str
        """

        self._traffic_type = traffic_type

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
        if not isinstance(other, AwsK8sServicesEc2V1alpha1FlowLogSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AwsK8sServicesEc2V1alpha1FlowLogSpec):
            return True

        return self.to_dict() != other.to_dict()
