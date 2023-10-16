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


class ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints(object):
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
        'authorization': 'ComCoreosMonitoringV1PodMonitorSpecAuthorization',
        'basic_auth': 'ComCoreosMonitoringV1PodMonitorSpecBasicAuth',
        'bearer_token_secret': 'ComCoreosMonitoringV1PodMonitorSpecBearerTokenSecret',
        'enable_http2': 'bool',
        'filter_running': 'bool',
        'follow_redirects': 'bool',
        'honor_labels': 'bool',
        'honor_timestamps': 'bool',
        'interval': 'str',
        'metric_relabelings': 'list[ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings]',
        'oauth2': 'ComCoreosMonitoringV1PodMonitorSpecOauth2',
        'params': 'dict(str, list[str])',
        'path': 'str',
        'port': 'str',
        'proxy_url': 'str',
        'relabelings': 'list[ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings]',
        'scheme': 'str',
        'scrape_timeout': 'str',
        'target_port': 'object',
        'tls_config': 'ComCoreosMonitoringV1PodMonitorSpecTlsConfig'
    }

    attribute_map = {
        'authorization': 'authorization',
        'basic_auth': 'basicAuth',
        'bearer_token_secret': 'bearerTokenSecret',
        'enable_http2': 'enableHttp2',
        'filter_running': 'filterRunning',
        'follow_redirects': 'followRedirects',
        'honor_labels': 'honorLabels',
        'honor_timestamps': 'honorTimestamps',
        'interval': 'interval',
        'metric_relabelings': 'metricRelabelings',
        'oauth2': 'oauth2',
        'params': 'params',
        'path': 'path',
        'port': 'port',
        'proxy_url': 'proxyUrl',
        'relabelings': 'relabelings',
        'scheme': 'scheme',
        'scrape_timeout': 'scrapeTimeout',
        'target_port': 'targetPort',
        'tls_config': 'tlsConfig'
    }

    def __init__(self, authorization=None, basic_auth=None, bearer_token_secret=None, enable_http2=None, filter_running=None, follow_redirects=None, honor_labels=None, honor_timestamps=None, interval=None, metric_relabelings=None, oauth2=None, params=None, path=None, port=None, proxy_url=None, relabelings=None, scheme=None, scrape_timeout=None, target_port=None, tls_config=None, local_vars_configuration=None):  # noqa: E501
        """ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._authorization = None
        self._basic_auth = None
        self._bearer_token_secret = None
        self._enable_http2 = None
        self._filter_running = None
        self._follow_redirects = None
        self._honor_labels = None
        self._honor_timestamps = None
        self._interval = None
        self._metric_relabelings = None
        self._oauth2 = None
        self._params = None
        self._path = None
        self._port = None
        self._proxy_url = None
        self._relabelings = None
        self._scheme = None
        self._scrape_timeout = None
        self._target_port = None
        self._tls_config = None
        self.discriminator = None

        if authorization is not None:
            self.authorization = authorization
        if basic_auth is not None:
            self.basic_auth = basic_auth
        if bearer_token_secret is not None:
            self.bearer_token_secret = bearer_token_secret
        if enable_http2 is not None:
            self.enable_http2 = enable_http2
        if filter_running is not None:
            self.filter_running = filter_running
        if follow_redirects is not None:
            self.follow_redirects = follow_redirects
        if honor_labels is not None:
            self.honor_labels = honor_labels
        if honor_timestamps is not None:
            self.honor_timestamps = honor_timestamps
        if interval is not None:
            self.interval = interval
        if metric_relabelings is not None:
            self.metric_relabelings = metric_relabelings
        if oauth2 is not None:
            self.oauth2 = oauth2
        if params is not None:
            self.params = params
        if path is not None:
            self.path = path
        if port is not None:
            self.port = port
        if proxy_url is not None:
            self.proxy_url = proxy_url
        if relabelings is not None:
            self.relabelings = relabelings
        if scheme is not None:
            self.scheme = scheme
        if scrape_timeout is not None:
            self.scrape_timeout = scrape_timeout
        if target_port is not None:
            self.target_port = target_port
        if tls_config is not None:
            self.tls_config = tls_config

    @property
    def authorization(self):
        """Gets the authorization of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501


        :return: The authorization of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :rtype: ComCoreosMonitoringV1PodMonitorSpecAuthorization
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """Sets the authorization of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.


        :param authorization: The authorization of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :type: ComCoreosMonitoringV1PodMonitorSpecAuthorization
        """

        self._authorization = authorization

    @property
    def basic_auth(self):
        """Gets the basic_auth of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501


        :return: The basic_auth of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :rtype: ComCoreosMonitoringV1PodMonitorSpecBasicAuth
        """
        return self._basic_auth

    @basic_auth.setter
    def basic_auth(self, basic_auth):
        """Sets the basic_auth of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.


        :param basic_auth: The basic_auth of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :type: ComCoreosMonitoringV1PodMonitorSpecBasicAuth
        """

        self._basic_auth = basic_auth

    @property
    def bearer_token_secret(self):
        """Gets the bearer_token_secret of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501


        :return: The bearer_token_secret of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :rtype: ComCoreosMonitoringV1PodMonitorSpecBearerTokenSecret
        """
        return self._bearer_token_secret

    @bearer_token_secret.setter
    def bearer_token_secret(self, bearer_token_secret):
        """Sets the bearer_token_secret of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.


        :param bearer_token_secret: The bearer_token_secret of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :type: ComCoreosMonitoringV1PodMonitorSpecBearerTokenSecret
        """

        self._bearer_token_secret = bearer_token_secret

    @property
    def enable_http2(self):
        """Gets the enable_http2 of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501

        Whether to enable HTTP2.  # noqa: E501

        :return: The enable_http2 of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :rtype: bool
        """
        return self._enable_http2

    @enable_http2.setter
    def enable_http2(self, enable_http2):
        """Sets the enable_http2 of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.

        Whether to enable HTTP2.  # noqa: E501

        :param enable_http2: The enable_http2 of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :type: bool
        """

        self._enable_http2 = enable_http2

    @property
    def filter_running(self):
        """Gets the filter_running of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501

        Drop pods that are not running. (Failed, Succeeded). Enabled by default. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase  # noqa: E501

        :return: The filter_running of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :rtype: bool
        """
        return self._filter_running

    @filter_running.setter
    def filter_running(self, filter_running):
        """Sets the filter_running of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.

        Drop pods that are not running. (Failed, Succeeded). Enabled by default. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase  # noqa: E501

        :param filter_running: The filter_running of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :type: bool
        """

        self._filter_running = filter_running

    @property
    def follow_redirects(self):
        """Gets the follow_redirects of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501

        FollowRedirects configures whether scrape requests follow HTTP 3xx redirects.  # noqa: E501

        :return: The follow_redirects of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :rtype: bool
        """
        return self._follow_redirects

    @follow_redirects.setter
    def follow_redirects(self, follow_redirects):
        """Sets the follow_redirects of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.

        FollowRedirects configures whether scrape requests follow HTTP 3xx redirects.  # noqa: E501

        :param follow_redirects: The follow_redirects of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :type: bool
        """

        self._follow_redirects = follow_redirects

    @property
    def honor_labels(self):
        """Gets the honor_labels of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501

        HonorLabels chooses the metric's labels on collisions with target labels.  # noqa: E501

        :return: The honor_labels of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :rtype: bool
        """
        return self._honor_labels

    @honor_labels.setter
    def honor_labels(self, honor_labels):
        """Sets the honor_labels of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.

        HonorLabels chooses the metric's labels on collisions with target labels.  # noqa: E501

        :param honor_labels: The honor_labels of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :type: bool
        """

        self._honor_labels = honor_labels

    @property
    def honor_timestamps(self):
        """Gets the honor_timestamps of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501

        HonorTimestamps controls whether Prometheus respects the timestamps present in scraped data.  # noqa: E501

        :return: The honor_timestamps of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :rtype: bool
        """
        return self._honor_timestamps

    @honor_timestamps.setter
    def honor_timestamps(self, honor_timestamps):
        """Sets the honor_timestamps of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.

        HonorTimestamps controls whether Prometheus respects the timestamps present in scraped data.  # noqa: E501

        :param honor_timestamps: The honor_timestamps of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :type: bool
        """

        self._honor_timestamps = honor_timestamps

    @property
    def interval(self):
        """Gets the interval of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501

        Interval at which metrics should be scraped If not specified Prometheus' global scrape interval is used.  # noqa: E501

        :return: The interval of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.

        Interval at which metrics should be scraped If not specified Prometheus' global scrape interval is used.  # noqa: E501

        :param interval: The interval of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                interval is not None and not re.search(r'^(0|(([0-9]+)y)?(([0-9]+)w)?(([0-9]+)d)?(([0-9]+)h)?(([0-9]+)m)?(([0-9]+)s)?(([0-9]+)ms)?)$', interval)):  # noqa: E501
            raise ValueError(r"Invalid value for `interval`, must be a follow pattern or equal to `/^(0|(([0-9]+)y)?(([0-9]+)w)?(([0-9]+)d)?(([0-9]+)h)?(([0-9]+)m)?(([0-9]+)s)?(([0-9]+)ms)?)$/`")  # noqa: E501

        self._interval = interval

    @property
    def metric_relabelings(self):
        """Gets the metric_relabelings of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501

        MetricRelabelConfigs to apply to samples before ingestion.  # noqa: E501

        :return: The metric_relabelings of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :rtype: list[ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings]
        """
        return self._metric_relabelings

    @metric_relabelings.setter
    def metric_relabelings(self, metric_relabelings):
        """Sets the metric_relabelings of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.

        MetricRelabelConfigs to apply to samples before ingestion.  # noqa: E501

        :param metric_relabelings: The metric_relabelings of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :type: list[ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings]
        """

        self._metric_relabelings = metric_relabelings

    @property
    def oauth2(self):
        """Gets the oauth2 of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501


        :return: The oauth2 of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :rtype: ComCoreosMonitoringV1PodMonitorSpecOauth2
        """
        return self._oauth2

    @oauth2.setter
    def oauth2(self, oauth2):
        """Sets the oauth2 of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.


        :param oauth2: The oauth2 of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :type: ComCoreosMonitoringV1PodMonitorSpecOauth2
        """

        self._oauth2 = oauth2

    @property
    def params(self):
        """Gets the params of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501

        Optional HTTP URL parameters  # noqa: E501

        :return: The params of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.

        Optional HTTP URL parameters  # noqa: E501

        :param params: The params of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._params = params

    @property
    def path(self):
        """Gets the path of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501

        HTTP path to scrape for metrics. If empty, Prometheus uses the default value (e.g. `/metrics`).  # noqa: E501

        :return: The path of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.

        HTTP path to scrape for metrics. If empty, Prometheus uses the default value (e.g. `/metrics`).  # noqa: E501

        :param path: The path of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def port(self):
        """Gets the port of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501

        Name of the pod port this endpoint refers to. Mutually exclusive with targetPort.  # noqa: E501

        :return: The port of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.

        Name of the pod port this endpoint refers to. Mutually exclusive with targetPort.  # noqa: E501

        :param port: The port of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :type: str
        """

        self._port = port

    @property
    def proxy_url(self):
        """Gets the proxy_url of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501

        ProxyURL eg http://proxyserver:2195 Directs scrapes to proxy through this endpoint.  # noqa: E501

        :return: The proxy_url of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :rtype: str
        """
        return self._proxy_url

    @proxy_url.setter
    def proxy_url(self, proxy_url):
        """Sets the proxy_url of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.

        ProxyURL eg http://proxyserver:2195 Directs scrapes to proxy through this endpoint.  # noqa: E501

        :param proxy_url: The proxy_url of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :type: str
        """

        self._proxy_url = proxy_url

    @property
    def relabelings(self):
        """Gets the relabelings of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501

        RelabelConfigs to apply to samples before scraping. Prometheus Operator automatically adds relabelings for a few standard Kubernetes fields. The original scrape job's name is available via the `__tmp_prometheus_job_name` label. More info: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config  # noqa: E501

        :return: The relabelings of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :rtype: list[ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings]
        """
        return self._relabelings

    @relabelings.setter
    def relabelings(self, relabelings):
        """Sets the relabelings of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.

        RelabelConfigs to apply to samples before scraping. Prometheus Operator automatically adds relabelings for a few standard Kubernetes fields. The original scrape job's name is available via the `__tmp_prometheus_job_name` label. More info: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config  # noqa: E501

        :param relabelings: The relabelings of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :type: list[ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings]
        """

        self._relabelings = relabelings

    @property
    def scheme(self):
        """Gets the scheme of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501

        HTTP scheme to use for scraping.  # noqa: E501

        :return: The scheme of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :rtype: str
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        """Sets the scheme of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.

        HTTP scheme to use for scraping.  # noqa: E501

        :param scheme: The scheme of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :type: str
        """

        self._scheme = scheme

    @property
    def scrape_timeout(self):
        """Gets the scrape_timeout of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501

        Timeout after which the scrape is ended If not specified, the Prometheus global scrape interval is used.  # noqa: E501

        :return: The scrape_timeout of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :rtype: str
        """
        return self._scrape_timeout

    @scrape_timeout.setter
    def scrape_timeout(self, scrape_timeout):
        """Sets the scrape_timeout of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.

        Timeout after which the scrape is ended If not specified, the Prometheus global scrape interval is used.  # noqa: E501

        :param scrape_timeout: The scrape_timeout of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                scrape_timeout is not None and not re.search(r'^(0|(([0-9]+)y)?(([0-9]+)w)?(([0-9]+)d)?(([0-9]+)h)?(([0-9]+)m)?(([0-9]+)s)?(([0-9]+)ms)?)$', scrape_timeout)):  # noqa: E501
            raise ValueError(r"Invalid value for `scrape_timeout`, must be a follow pattern or equal to `/^(0|(([0-9]+)y)?(([0-9]+)w)?(([0-9]+)d)?(([0-9]+)h)?(([0-9]+)m)?(([0-9]+)s)?(([0-9]+)ms)?)$/`")  # noqa: E501

        self._scrape_timeout = scrape_timeout

    @property
    def target_port(self):
        """Gets the target_port of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501

        Deprecated: Use 'port' instead.  # noqa: E501

        :return: The target_port of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :rtype: object
        """
        return self._target_port

    @target_port.setter
    def target_port(self, target_port):
        """Sets the target_port of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.

        Deprecated: Use 'port' instead.  # noqa: E501

        :param target_port: The target_port of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :type: object
        """

        self._target_port = target_port

    @property
    def tls_config(self):
        """Gets the tls_config of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501


        :return: The tls_config of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :rtype: ComCoreosMonitoringV1PodMonitorSpecTlsConfig
        """
        return self._tls_config

    @tls_config.setter
    def tls_config(self, tls_config):
        """Sets the tls_config of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.


        :param tls_config: The tls_config of this ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.  # noqa: E501
        :type: ComCoreosMonitoringV1PodMonitorSpecTlsConfig
        """

        self._tls_config = tls_config

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
        if not isinstance(other, ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints):
            return True

        return self.to_dict() != other.to_dict()