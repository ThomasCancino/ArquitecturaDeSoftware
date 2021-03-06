from django.apps import AppConfig
from rest_framework.response import Response 
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import status 

class TrollbookConfig(AppConfig):
    name = 'TrollBook'

class UserAPI(APIView):
    def post(self,request):
        #los datos estan en el request.data
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED )
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)