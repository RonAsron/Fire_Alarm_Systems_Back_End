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
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['gps_latitude'] = str(instance.gps_latitude) if instance.gps_latitude is not None else ""
        representation['gps_longitude'] = str(instance.gps_longitude) if instance.gps_longitude is not None else ""
        return representation

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        try:
            data['gps_latitude'] = float(data['gps_latitude']) if data.get('gps_latitude') else None
            data['gps_longitude'] = float(data['gps_longitude']) if data.get('gps_longitude') else None
        except ValueError:
            raise serializers.ValidationError({
                'gps_latitude': 'GPS Latitude must be a valid number.',
                'gps_longitude': 'GPS Longitude must be a valid number.'
            })
        return data
