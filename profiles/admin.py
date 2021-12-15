from django.contrib import admin
from .models import Comement, MyUserModel

# Register your models here.
admin.site.register(MyUserModel)
admin.site.register(Comement)