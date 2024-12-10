from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DeviceData
from .serializers import DeviceDataSerializer


class DeviceDataList(APIView):
    def get(self, request):
        """
        ดึงข้อมูลทั้งหมดจาก database
        """
        devices = DeviceData.objects.all()
        serializer = DeviceDataSerializer(devices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        บันทึกข้อมูลใหม่จาก request
        """
        serializer = DeviceDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
