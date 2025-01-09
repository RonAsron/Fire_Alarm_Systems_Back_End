from django.db import models

class DeviceData(models.Model):
    name = models.CharField(max_length=100)
    
    esp_32 = models.CharField(max_length=255, null=True, blank=False)

    gps_latitude = models.DecimalField(max_digits=11, decimal_places=7, null=True, blank=False)
    gps_longitude = models.DecimalField(max_digits=11, decimal_places=7, null=True, blank=False)

    esp_8266_num1 = models.CharField(max_length=255, default='')
    esp_8266_num2 = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name