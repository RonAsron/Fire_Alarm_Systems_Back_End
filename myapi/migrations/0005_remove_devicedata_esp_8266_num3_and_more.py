# Generated by Django 5.1 on 2025-01-06 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0004_devicedata_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devicedata',
            name='esp_8266_num3',
        ),
        migrations.RemoveField(
            model_name='devicedata',
            name='esp_8266_num4',
        ),
        migrations.RemoveField(
            model_name='devicedata',
            name='esp_8266_num5',
        ),
        migrations.RemoveField(
            model_name='devicedata',
            name='time',
        ),
        migrations.AlterField(
            model_name='devicedata',
            name='esp_32',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
