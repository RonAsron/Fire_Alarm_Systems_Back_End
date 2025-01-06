from rest_framework import serializers
from .models import DeviceData

class DeviceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceData
        fields = ['gps_latitude', 'gps_longitude', 'esp_8266_num1', 'esp_8266_num2']  # เพิ่มแค่ข้อมูลที่ต้องการ

    # การแปลงข้อมูลที่ส่งกลับ (to_representation)
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # ส่งข้อมูลในรูปแบบที่ต้องการ
        return {
            "MQ2 Data": instance.esp_8266_num1,  # ค่าของ esp_8266_num1 สำหรับ MQ2
            "MQ5 Data": instance.esp_8266_num2,  # ค่าของ esp_8266_num2 สำหรับ MQ5
            "GPS Data": {
                "Latitude": str(instance.gps_latitude) if instance.gps_latitude is not None else "",
                "Longitude": str(instance.gps_longitude) if instance.gps_longitude is not None else ""
            }
        }

    # การแปลงข้อมูลที่รับเข้ามา (to_internal_value)
    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        
        # ตรวจสอบว่า gps_latitude และ gps_longitude เป็นตัวเลขที่ถูกต้องหรือไม่
        try:
            if 'gps_latitude' in data and data['gps_latitude']:
                data['gps_latitude'] = float(data['gps_latitude'])  # แปลงเป็น float ถ้ามีค่า
            else:
                data['gps_latitude'] = None  # ถ้าไม่มีค่าหรือเป็น None ให้เป็น None
                
            if 'gps_longitude' in data and data['gps_longitude']:
                data['gps_longitude'] = float(data['gps_longitude'])  # แปลงเป็น float ถ้ามีค่า
            else:
                data['gps_longitude'] = None  # ถ้าไม่มีค่าหรือเป็น None ให้เป็น None
        
        except ValueError:
            # ถ้ามีข้อผิดพลาดในการแปลงเป็น float
            raise serializers.ValidationError({
                'gps_latitude': 'GPS Latitude must be a valid number.',
                'gps_longitude': 'GPS Longitude must be a valid number.'
            })

        return data
