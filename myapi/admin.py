from django.contrib import admin
from .models import DeviceData
from django.contrib.admin import SimpleListFilter

# กำหนดตัวกรองแบบกำหนดเอง (optional)
class LatitudeLongitudeFilter(SimpleListFilter):
    title = 'GPS Coordinates'  # ชื่อที่จะแสดงในหน้า Admin
    parameter_name = 'gps_latitude'

    def lookups(self, request, model_admin):
        # การกำหนดการกรองตามค่า Latitude
        return (
            ('positive', 'Positive Latitude'),  # กรองตามค่าละติจูดบวก
            ('negative', 'Negative Latitude'),  # กรองตามค่าละติจูดลบ
        )

    def queryset(self, request, queryset):
        if self.value() == 'positive':
            return queryset.filter(gps_latitude__gte=0)  # ค่า latitude ที่บวก
        if self.value() == 'negative':
            return queryset.filter(gps_latitude__lt=0)  # ค่า latitude ที่ลบ
        return queryset

@admin.register(DeviceData)
class DeviceDataAdmin(admin.ModelAdmin):
    # การแสดงฟิลด์ในหน้า Admin
    list_display = (
        'name',
        'esp_8266_num1',  # ข้อมูล MQ2
        'esp_8266_num2',  # ข้อมูล MQ5
        'formatted_gps_latitude',  # แสดงค่าละติจูดในรูปแบบที่อ่านง่าย
        'formatted_gps_longitude',  # แสดงค่าลองจิจูดในรูปแบบที่อ่านง่าย
    )

    # การค้นหาในหน้า Admin
    search_fields = (
        'name',
        'esp_8266_num1',  # ค้นหาข้อมูล MQ2
        'esp_8266_num2',  # ค้นหาข้อมูล MQ5
    )

    # การกรองข้อมูลในหน้า Admin
    list_filter = (
        LatitudeLongitudeFilter,  # กรองข้อมูลตามค่า Latitude (หรือลองจิจูด)
    )

    # ฟังก์ชันเพื่อจัดรูปแบบการแสดงผล GPS Latitude
    def formatted_gps_latitude(self, obj):
        return f"{obj.gps_latitude:.7f}" if obj.gps_latitude else "Not Available"
    formatted_gps_latitude.admin_order_field = 'gps_latitude'  # ทำให้สามารถเรียงลำดับได้
    formatted_gps_latitude.short_description = 'GPS Latitude'  # ชื่อที่จะแสดงใน admin

    # ฟังก์ชันเพื่อจัดรูปแบบการแสดงผล GPS Longitude
    def formatted_gps_longitude(self, obj):
        return f"{obj.gps_longitude:.7f}" if obj.gps_longitude else "Not Available"
    formatted_gps_longitude.admin_order_field = 'gps_longitude'  # ทำให้สามารถเรียงลำดับได้
    formatted_gps_longitude.short_description = 'GPS Longitude'  # ชื่อที่จะแสดงใน admin
