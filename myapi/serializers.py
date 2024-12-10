from rest_framework import serializers
from .models import DeviceData


class DeviceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceData
        fields = [
            'id',
            'name',
            'esp_32',
            'gps_latitude',
            'gps_longitude',
            'esp_8266_num1',
            'esp_8266_num2',
            'esp_8266_num3',
            'esp_8266_num4',
            'esp_8266_num5',
        ]
