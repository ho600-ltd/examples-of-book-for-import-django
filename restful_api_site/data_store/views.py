from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from data_store.models import FlowData
from data_store.serializers import FlowDataSerializer



class FlowDataModelViewSet(viewsets.ModelViewSet):
    queryset = FlowData.objects.all()
    serializer_class = FlowDataSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, )
    http_method_names = ('get', 'post', )