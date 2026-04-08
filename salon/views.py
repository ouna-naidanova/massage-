from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Master, Service, Client, Appointment

def index(request):
    """Главная страница"""
    masters = Master.objects.all()[:4]
    services = Service.objects.all()[:6]
    context = {
        'masters': masters,
        'services': services,
    }
    return render(request, 'salon/index.html', context)

def master_list(request):
    """Список мастеров"""
    masters = Master.objects.all()
    return render(request, 'salon/master_list.html', {'masters': masters})

def master_detail(request, pk):
    """Страница конкретного мастера"""
    master = get_object_or_404(Master, pk=pk)
    return render(request, 'salon/master_detail.html', {'master': master})

def service_list(request):
    """Список услуг"""
    services = Service.objects.all()
    return render(request, 'salon/service_list.html', {'services': services})

def appointment_create(request):
    """Форма записи на массаж"""
    if request.method == 'POST':
        client_name = request.POST.get('client_name')
        client_phone = request.POST.get('client_phone')
        client_email = request.POST.get('client_email', 'temp@temp.com')
        master_id = request.POST.get('master')
        service_id = request.POST.get('service')
        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')
        
        # Создаём или находим клиента
        client, created = Client.objects.get_or_create(
            email=client_email,
            defaults={
                'full_name': client_name,
                'phone': client_phone,
                'password_hash': 'temp_hash'
            }
        )
        
        master = None
        if master_id:
            master = get_object_or_404(Master, id=master_id)
        
        service = get_object_or_404(Service, id=service_id)
        
        appointment = Appointment.objects.create(
            client=client,
            master=master,
            service=service,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            status='pending'
        )
        
        messages.success(request, 'Ваша запись успешно создана! Мы свяжемся с вами для подтверждения.')
        return redirect('appointment_success')
    
    masters = Master.objects.all()
    services = Service.objects.all()
    context = {
        'masters': masters,
        'services': services,
    }
    return render(request, 'salon/appointment_form.html', context)

def appointment_success(request):
    """Страница успешной записи"""
    return render(request, 'salon/appointment_success.html')
