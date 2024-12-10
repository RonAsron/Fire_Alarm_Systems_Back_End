# myapi/urls.py
from django.urls import path
from .views import MyModelList

urlpatterns = [
    path('items/', MyModelList.as_view(), name='my_model_list'),
]
