from django.contrib import admin
from .models import DeviceData

@admin.register(DeviceData)
class DeviceDataAdmin(admin.ModelAdmin):
    # การแสดงฟิลด์ในหน้า Admin
    list_display = (
        'name',
        'esp_8266_num1',  # MQ2 Data
        'esp_8266_num2',  # MQ5 Data
        'gps_latitude',
        'gps_longitude',
    )
    
    # การค้นหาในหน้า Admin
    search_fields = (
        'name',
        'esp_8266_num1',  # ค้นหาข้อมูล MQ2
        'esp_8266_num2',  # ค้นหาข้อมูล MQ5
    )
    
    # การกรองข้อมูลในหน้า Admin
    list_filter = (
        'gps_latitude',  # กรองข้อมูลตาม GPS Latitude
    )
