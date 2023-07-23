from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Employee, Device, Delegation, Company

# Register your models here.

admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Device)
admin.site.register(Delegation)
