from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class DeviceData(models.Model):
    name = models.CharField(max_length=100)
    esp_32 = models.CharField(max_length=255, default='')  # ESP32 ตัวที่ 1
    esp_8266_2 = models.CharField(max_length=255, default='')  # ESP8266 ตัวที่ 2
    esp_8266_3 = models.CharField(max_length=255, default='')  # ESP8266 ตัวที่ 3
    esp_8266_4 = models.CharField(max_length=255, default='')  # ESP8266 ตัวที่ 4
    esp_8266_5 = models.CharField(max_length=255, default='')  # ESP8266 ตัวที่ 5
    gps_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    gps_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return self.name
