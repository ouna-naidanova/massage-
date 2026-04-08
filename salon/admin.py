from django.contrib import admin
from .models import Client, Master, Service, Appointment

@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'specialization', 'experience']
    list_filter = ['specialization']
    search_fields = ['full_name']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'duration', 'category']
    list_filter = ['category']

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['client', 'master', 'service', 'appointment_date', 'status']
    list_filter = ['status', 'appointment_date']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'email', 'registration_date']
    search_fields = ['full_name', 'email']
