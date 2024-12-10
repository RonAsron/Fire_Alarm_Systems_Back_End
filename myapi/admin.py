from django.contrib import admin
from .models import DeviceData


@admin.register(DeviceData)
class DeviceDataAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'esp_32',
        'gps_latitude',
        'gps_longitude',
        'esp_8266_num1',
        'esp_8266_num2',
        'esp_8266_num3',
        'esp_8266_num4',
        'esp_8266_num5',
    )
    search_fields = (
        'name',
        'esp_32',
        'esp_8266_num1',
    )
    list_filter = ('esp_32', 'gps_latitude')
