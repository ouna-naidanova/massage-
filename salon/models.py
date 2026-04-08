from django.db import models


class Client(models.Model):
    """Модель клиента"""
    full_name = models.CharField(max_length=200, verbose_name="ФИО")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(unique=True, verbose_name="Email")
    password_hash = models.CharField(max_length=255, verbose_name="Пароль")
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Master(models.Model):
    """Модель мастера"""
    full_name = models.CharField(max_length=200, verbose_name="ФИО")
    specialization = models.CharField(max_length=100, verbose_name="Специализация")
    experience = models.IntegerField(verbose_name="Стаж (лет)")
    photo = models.CharField(max_length=255, blank=True, null=True, verbose_name="Фото")
    bio = models.TextField(blank=True, null=True, verbose_name="Биография")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Мастер"
        verbose_name_plural = "Мастера"


class Service(models.Model):
    """Модель услуги"""
    name = models.CharField(max_length=200, verbose_name="Название услуги")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    duration = models.IntegerField(verbose_name="Продолжительность (мин)")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")
    category = models.CharField(max_length=100, verbose_name="Категория")

    def __str__(self):
        return f"{self.name} - {self.price} руб."

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class Appointment(models.Model):
    """Модель записи"""
    STATUS_CHOICES = [
        ('pending', 'Ожидает подтверждения'),
        ('confirmed', 'Подтверждена'),
        ('completed', 'Выполнена'),
        ('cancelled', 'Отменена'),
    ]

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='appointments',
        verbose_name="Клиент"
    )
    master = models.ForeignKey(
        Master,
        on_delete=models.CASCADE,
        related_name='appointments',
        verbose_name="Мастер"
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='appointments',
        verbose_name="Услуга"
    )
    appointment_date = models.DateField(verbose_name="Дата визита")
    appointment_time = models.TimeField(verbose_name="Время визита")
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name="Статус"
    )

    def __str__(self):
        return f"{self.client} → {self.master} ({self.appointment_date} {self.appointment_time})"

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
