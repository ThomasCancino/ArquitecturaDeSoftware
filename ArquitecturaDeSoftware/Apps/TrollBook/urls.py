from django.urls import path 
from views import UserList
from ArquitecturaDeSoftware.Apps.TrollBook.apps import UserAPI

urlpatterns = [
    path('User/', UserList.as_view(), name = 'User_list'),
]