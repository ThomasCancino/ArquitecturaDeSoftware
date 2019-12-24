"""Arquitect
  https://medium.com/@diwassharma/starting-a-python-django-project-on-mac-os-x-c089165cf010
  https://www.youtube.com/watch?v=phnJVwtSDLo&t=917s
"""
from django.contrib import admin
from django.urls import path
from ArquitecturaDeSoftware.Apps.TrollBook.apps import UserAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Apps/1.0/create_user',UserAPI.as_view(), name="apps_create_user"),
]
