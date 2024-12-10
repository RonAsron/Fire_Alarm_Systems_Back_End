# myapi/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MyModelSerializer
from .models import MyModel
from rest_framework import status
from .models import DeviceData
from .serializers import DeviceDataSerializer

class MyModelList(APIView):
    def get(self, request):
        items = MyModel.objects.all()
        serializer = MyModelSerializer(items, many=True)
        return Response(serializer.data)

class DeviceDataList(APIView):
    def get(self, request):
        devices = DeviceData.objects.all()
        serializer = DeviceDataSerializer(devices, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DeviceDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
