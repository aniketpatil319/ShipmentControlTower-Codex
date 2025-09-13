from django.contrib import admin
from .models import InboundShipment, OutboundShipment


@admin.register(InboundShipment)
class InboundShipmentAdmin(admin.ModelAdmin):
    list_display = ('reference', 'company', 'status', 'expected_date')


@admin.register(OutboundShipment)
class OutboundShipmentAdmin(admin.ModelAdmin):
    list_display = ('reference', 'company', 'status', 'expected_date')
