# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.20.7
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.events_v1_event_list import EventsV1EventList  # noqa: E501
from kubernetes.client.rest import ApiException

class TestEventsV1EventList(unittest.TestCase):
    """EventsV1EventList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EventsV1EventList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.events_v1_event_list.EventsV1EventList()  # noqa: E501
        if include_optional :
            return EventsV1EventList(
                api_version = '0', 
                items = [
                    kubernetes.client.models.events/v1/event.events.v1.Event(
                        action = '0', 
                        api_version = '0', 
                        deprecated_count = 56, 
                        deprecated_first_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        deprecated_last_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        deprecated_source = kubernetes.client.models.v1/event_source.v1.EventSource(
                            component = '0', 
                            host = '0', ), 
                        event_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        kind = '0', 
                        metadata = kubernetes.client.models.v1/object_meta.v1.ObjectMeta(
                            annotations = {
                                'key' : '0'
                                }, 
                            cluster_name = '0', 
                            creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            deletion_grace_period_seconds = 56, 
                            deletion_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            finalizers = [
                                '0'
                                ], 
                            generate_name = '0', 
                            generation = 56, 
                            labels = {
                                'key' : '0'
                                }, 
                            managed_fields = [
                                kubernetes.client.models.v1/managed_fields_entry.v1.ManagedFieldsEntry(
                                    api_version = '0', 
                                    fields_type = '0', 
                                    fields_v1 = kubernetes.client.models.fields_v1.fieldsV1(), 
                                    manager = '0', 
                                    operation = '0', 
                                    time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                ], 
                            name = '0', 
                            namespace = '0', 
                            owner_references = [
                                kubernetes.client.models.v1/owner_reference.v1.OwnerReference(
                                    api_version = '0', 
                                    block_owner_deletion = True, 
                                    controller = True, 
                                    kind = '0', 
                                    name = '0', 
                                    uid = '0', )
                                ], 
                            resource_version = '0', 
                            self_link = '0', 
                            uid = '0', ), 
                        note = '0', 
                        reason = '0', 
                        regarding = kubernetes.client.models.v1/object_reference.v1.ObjectReference(
                            api_version = '0', 
                            field_path = '0', 
                            kind = '0', 
                            name = '0', 
                            namespace = '0', 
                            resource_version = '0', 
                            uid = '0', ), 
                        related = kubernetes.client.models.v1/object_reference.v1.ObjectReference(
                            api_version = '0', 
                            field_path = '0', 
                            kind = '0', 
                            name = '0', 
                            namespace = '0', 
                            resource_version = '0', 
                            uid = '0', ), 
                        reporting_controller = '0', 
                        reporting_instance = '0', 
                        series = kubernetes.client.models.events/v1/event_series.events.v1.EventSeries(
                            count = 56, 
                            last_observed_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        type = '0', )
                    ], 
                kind = '0', 
                metadata = kubernetes.client.models.v1/list_meta.v1.ListMeta(
                    continue = '0', 
                    remaining_item_count = 56, 
                    resource_version = '0', 
                    self_link = '0', )
            )
        else :
            return EventsV1EventList(
                items = [
                    kubernetes.client.models.events/v1/event.events.v1.Event(
                        action = '0', 
                        api_version = '0', 
                        deprecated_count = 56, 
                        deprecated_first_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        deprecated_last_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        deprecated_source = kubernetes.client.models.v1/event_source.v1.EventSource(
                            component = '0', 
                            host = '0', ), 
                        event_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        kind = '0', 
                        metadata = kubernetes.client.models.v1/object_meta.v1.ObjectMeta(
                            annotations = {
                                'key' : '0'
                                }, 
                            cluster_name = '0', 
                            creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            deletion_grace_period_seconds = 56, 
                            deletion_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            finalizers = [
                                '0'
                                ], 
                            generate_name = '0', 
                            generation = 56, 
                            labels = {
                                'key' : '0'
                                }, 
                            managed_fields = [
                                kubernetes.client.models.v1/managed_fields_entry.v1.ManagedFieldsEntry(
                                    api_version = '0', 
                                    fields_type = '0', 
                                    fields_v1 = kubernetes.client.models.fields_v1.fieldsV1(), 
                                    manager = '0', 
                                    operation = '0', 
                                    time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                ], 
                            name = '0', 
                            namespace = '0', 
                            owner_references = [
                                kubernetes.client.models.v1/owner_reference.v1.OwnerReference(
                                    api_version = '0', 
                                    block_owner_deletion = True, 
                                    controller = True, 
                                    kind = '0', 
                                    name = '0', 
                                    uid = '0', )
                                ], 
                            resource_version = '0', 
                            self_link = '0', 
                            uid = '0', ), 
                        note = '0', 
                        reason = '0', 
                        regarding = kubernetes.client.models.v1/object_reference.v1.ObjectReference(
                            api_version = '0', 
                            field_path = '0', 
                            kind = '0', 
                            name = '0', 
                            namespace = '0', 
                            resource_version = '0', 
                            uid = '0', ), 
                        related = kubernetes.client.models.v1/object_reference.v1.ObjectReference(
                            api_version = '0', 
                            field_path = '0', 
                            kind = '0', 
                            name = '0', 
                            namespace = '0', 
                            resource_version = '0', 
                            uid = '0', ), 
                        reporting_controller = '0', 
                        reporting_instance = '0', 
                        series = kubernetes.client.models.events/v1/event_series.events.v1.EventSeries(
                            count = 56, 
                            last_observed_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        type = '0', )
                    ],
        )

    def testEventsV1EventList(self):
        """Test EventsV1EventList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
