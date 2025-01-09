from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from .models import DeviceData
from .serializers import DeviceDataSerializer

class DeviceDataList(APIView):
    # GET: ดึงข้อมูลทั้งหมด
    def get(self, request):
        devices = DeviceData.objects.all()
        serializer = DeviceDataSerializer(devices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST: เพิ่มข้อมูลใหม่
    def post(self, request):
        serializer = DeviceDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # OPTIONS: ส่งคืน Headers สำหรับตรวจสอบ Methods ที่อนุญาต
    def options(self, request, *args, **kwargs):
        allowed_methods = ['GET', 'POST', 'OPTIONS']
        headers = {'Allow': ', '.join(allowed_methods)}
        return Response(headers, headers=headers, status=status.HTTP_200_OK)


class DeviceDataDetail(APIView):
    # GET: ดึงข้อมูลตาม ID
    def get(self, request, id):
        device = get_object_or_404(DeviceData, id=id)
        serializer = DeviceDataSerializer(device)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # PUT: อัพเดทข้อมูลทั้งหมดตาม ID
    def put(self, request, id):
        device = get_object_or_404(DeviceData, id=id)
        serializer = DeviceDataSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PATCH: อัพเดทข้อมูลบางส่วนตาม ID
    def patch(self, request, id):
        device = get_object_or_404(DeviceData, id=id)
        serializer = DeviceDataSerializer(device, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE: ลบข้อมูลตาม ID
    def delete(self, request, id):
        device = get_object_or_404(DeviceData, id=id)
        device.delete()
        return Response({"message": "Device deleted successfully"}, status=status.HTTP_200_OK)

    # OPTIONS: ส่งคืน Headers สำหรับตรวจสอบ Methods ที่อนุญาต
    def options(self, request, *args, **kwargs):
        allowed_methods = ['GET', 'PUT', 'PATCH', 'DELETE', 'OPTIONS']
        headers = {'Allow': ', '.join(allowed_methods)}
        return Response(headers, headers=headers, status=status.HTTP_200_OK)
