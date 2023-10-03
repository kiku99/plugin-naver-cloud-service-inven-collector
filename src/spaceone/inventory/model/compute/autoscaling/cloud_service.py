from schematics.types import ModelType, StringType, PolyModelType

from spaceone.inventory.model.compute.autoscaling.data import AutoScalingInstance
from spaceone.inventory.libs.schema.metadata.dynamic_field import TextDyField, EnumDyField, ListDyField, SizeField
from spaceone.inventory.libs.schema.metadata.dynamic_layout import ItemDynamicLayout, TableDynamicLayout, \
    ListDynamicLayout
from spaceone.inventory.libs.schema.cloud_service import CloudServiceMeta, CloudServiceResource, \
    CloudServiceResponse

'''
Autoscaling Instance
'''
server_instance = ItemDynamicLayout.set_fields('Autoscaling Instance')



autoscaling_instance_meta = CloudServiceMeta.set_layouts([''])


class ComputeResource(CloudServiceResource):
    cloud_service_group = StringType(default='ComputeServer')


class AutoscalingInstanceResource(ComputeResource):
    cloud_service_type = StringType(default='Autoscaling')
    data = ModelType(AutoScalingInstance)
    _metadata = ModelType(CloudServiceMeta, default=autoscaling_instance_meta, serialized_name='metadata')


class ServerInstanceResponse(CloudServiceResponse):
    resource = PolyModelType(AutoscalingInstanceResource)
