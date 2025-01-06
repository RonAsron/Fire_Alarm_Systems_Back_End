from django.db import models

class DeviceData(models.Model):
    name = models.CharField(max_length=100)
    
    # ทำให้ esp_32 เป็น nullable
    esp_32 = models.CharField(max_length=255, null=True, blank=True)

    gps_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    gps_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    esp_8266_num1 = models.CharField(max_length=255, default='')
    esp_8266_num2 = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name
