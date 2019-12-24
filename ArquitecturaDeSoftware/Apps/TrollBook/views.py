from django.shortcuts import render

# Create your views here.
def image(request):
    image_file = request.FILES['image_file'].file.read()
    Troll.objects.create(image=image_file)