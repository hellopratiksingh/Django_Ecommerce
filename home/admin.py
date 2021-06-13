from django.contrib import admin
from home.models import *

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email")
    

@admin.register(bicycle)
class bicycleAdmin(admin.ModelAdmin):
    list_display = ("firstName", "lastName", "price")
    
