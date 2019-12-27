from django.urls import path
from .views import PersonaList
from .views import dataList

urlpatterns = [
    path('persona/',PersonaList.as_view(), name = 'persona_list'),
    path('data/', dataList.as_view(), name = 'data_list'),
]
