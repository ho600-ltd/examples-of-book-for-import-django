from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from data_store.models import FlowData


class FlowDataSerializer(ModelSerializer):
    resource_uri = HyperlinkedIdentityField(
        view_name="data_store_api_root:flowdata-detail", lookup_field='pk')

    class Meta:
        model = FlowData
        fields = '__all__'