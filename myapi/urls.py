# myapi/urls.py
from django.urls import path
from .views import MyModelList
from .views import DeviceDataList

urlpatterns = [
    path('items/', MyModelList.as_view(), name='my_model_list'),
    path('api/devices/', DeviceDataList.as_view(), name='device_data_list'),

]
