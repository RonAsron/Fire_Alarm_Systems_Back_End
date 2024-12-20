# Generated by Django 5.1 on 2024-12-10 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('esp_32', models.CharField(default='', max_length=255)),
                ('esp_8266_2', models.CharField(default='', max_length=255)),
                ('esp_8266_3', models.CharField(default='', max_length=255)),
                ('esp_8266_4', models.CharField(default='', max_length=255)),
                ('esp_8266_5', models.CharField(default='', max_length=255)),
                ('gps_latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('gps_longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
            ],
        ),
    ]
