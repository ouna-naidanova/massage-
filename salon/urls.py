from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('masters/', views.master_list, name='master_list'),
    path('masters/<int:pk>/', views.master_detail, name='master_detail'),
    path('services/', views.service_list, name='service_list'),
    path('appointment/', views.appointment_create, name='appointment_create'),
    path('appointment/success/', views.appointment_success, name='appointment_success'),
]
