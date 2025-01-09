from rest_framework import serializers
from .models import DeviceData  # Make sure the model exists and is correctly imported

class DeviceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceData
        fields = '__all__'  # or you can list specific fields
