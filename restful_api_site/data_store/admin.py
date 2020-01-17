from django.contrib import admin

from data_store.models import EndSpot, FlowData

class EndSpotAdmin(admin.ModelAdmin):
    pass
admin.site.register(EndSpot, EndSpotAdmin)

class FlowDataAdmin(admin.ModelAdmin):
    pass
admin.site.register(FlowData, FlowDataAdmin)