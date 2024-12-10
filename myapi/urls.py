from django.urls import path
from .views import DeviceDataList, DeviceDataDetail


urlpatterns = [
    path('devices/', DeviceDataList.as_view(), name='device_data_list'),
    path('devices/<int:id>/', DeviceDataDetail.as_view(), name='device_data_detail'),
]
