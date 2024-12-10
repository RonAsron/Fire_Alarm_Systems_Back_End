from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DeviceData
from .serializers import DeviceDataSerializer


class DeviceDataList(APIView):
    """
    API endpoint สำหรับดึงข้อมูล Device Data
    """

    def get(self, request):
        # ดึงข้อมูลจาก database
        devices = DeviceData.objects.all()
        # Serialize ข้อมูล
        serializer = DeviceDataSerializer(devices, many=True)
        # Return JSON response
        return Response(serializer.data, status=status.HTTP_200_OK)
