from django.contrib import admin
from ArquitecturaDeSoftware.Apps.TrollBook.models import *
from ArquitecturaDeSoftware.Apps.TrollBook.serializers import *

# Register your models here.
admin.site.register(Troll)
admin.site.register(UserSerializer)