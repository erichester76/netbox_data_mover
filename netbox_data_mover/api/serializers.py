from ..models import DataMoverConfig, DataMoverDataSource
from netbox.api.serializers import NetBoxModelSerializer


class DataMoverDataSourceSerializer(NetBoxModelSerializer):
    class Meta:
        model = DataMoverDataSource
        fields = ['pk', 'name', 'description', 'schedule', 'source', 'destination', 'last_run_records', 'last_run_status', 'last_run_time']

class DataMoverConfigSerializer(NetBoxModelSerializer):
    class Meta:
        model = DataMoverConfig
        fields = ['pk', 'name', 'type', 'module', 'auth_method', 'auth_function', 'find_function', 'create_function', 'update_function', 'fetch_function', 'auth_args', 'base_urls']
