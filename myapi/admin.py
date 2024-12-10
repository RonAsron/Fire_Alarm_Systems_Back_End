from django.contrib import admin
from .models import DeviceData

@admin.register(DeviceData)
class DeviceDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'esp_32', 'gps_latitude', 'gps_longitude')  # แสดงฟิลด์ที่สำคัญ
    search_fields = ('name', 'esp_32')  # เพิ่มช่องค้นหา
    list_filter = ('esp_32',)  # เพิ่มตัวกรองสำหรับ ESP32
