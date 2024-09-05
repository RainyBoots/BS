from django.contrib import admin
from .models import Master, Service, Visit


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'contact_info')
    search_fields = ('first_name', 'last_name', 'contact_info')
    list_filter = ('services',)  

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name', 'price')
    

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'master', 'service')
    list_filter = ('client_name', 'service')
    search_fields = ('client_name', 'service')
 