from django.urls import path
from .views import DeviceDataList

urlpatterns = [
    path('devices/', DeviceDataList.as_view(), name='device_data_list'),
]
