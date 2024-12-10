# myapi/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MyModelSerializer
from .models import MyModel

class MyModelList(APIView):
    def get(self, request):
        items = MyModel.objects.all()
        serializer = MyModelSerializer(items, many=True)
        return Response(serializer.data)
