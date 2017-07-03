from django.contrib import admin

# Register your models here.
from .models import Plat, Menu

admin.site.register(Plat)
admin.site.register(Menu)
