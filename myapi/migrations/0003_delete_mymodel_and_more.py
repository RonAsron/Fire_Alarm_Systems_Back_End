# Generated by Django 5.1 on 2024-12-10 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_devicedata'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyModel',
        ),
        migrations.RenameField(
            model_name='devicedata',
            old_name='esp_8266_2',
            new_name='esp_8266_num1',
        ),
        migrations.RenameField(
            model_name='devicedata',
            old_name='esp_8266_3',
            new_name='esp_8266_num2',
        ),
        migrations.RenameField(
            model_name='devicedata',
            old_name='esp_8266_4',
            new_name='esp_8266_num3',
        ),
        migrations.RenameField(
            model_name='devicedata',
            old_name='esp_8266_5',
            new_name='esp_8266_num4',
        ),
        migrations.AddField(
            model_name='devicedata',
            name='esp_8266_num5',
            field=models.CharField(default='', max_length=255),
        ),
    ]