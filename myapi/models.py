from django.db import models


class DeviceData(models.Model):
    # ข้อมูลหลัก
    name = models.CharField(max_length=100)
    
    # ESP32
    esp_32 = models.CharField(max_length=255, default='')  # ข้อมูล ESP32

    # GPS
    gps_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    gps_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    # ESP8266 กับ MQ2, MQ5
    esp_8266_num1 = models.CharField(max_length=255, default='')  # ESP8266_num1 (mq2 & mq5)
    esp_8266_num2 = models.CharField(max_length=255, default='')  # ESP8266_num2 (mq2 & mq5)
    esp_8266_num3 = models.CharField(max_length=255, default='')  # ESP8266_num3 (mq2 & mq5)

    # ESP8266 ที่ใช้ SERVO
    esp_8266_num4 = models.CharField(max_length=255, default='')  # ESP8266_num4 (SERVO1 & SERVO2)
    esp_8266_num5 = models.CharField(max_length=255, default='')  # ESP8266_num5 (SERVO1 & SERVO2)

    def __str__(self):
        return self.name
