from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from .serializers import UserModelSerializer

# Create your views here.
def image(request):
    image_file = request.FILES['image_file'].file.read()
    Troll.objects.create(image=image_file)

#
class UserList(generics.ListCreateAPIView):
    queryset = UserSerializer.objects.all()
    serializer_class = UserModelSerializer