from django.db import models


class Master(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    contact_info = models.TextField(max_length=255, verbose_name='Контактная информация')
    photo = models.ImageField(upload_to='masters/photos/', blank=True, null=True, verbose_name='Фотография')
    services = models.ManyToManyField('Service', related_name='masters', verbose_name='Услуги')
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    
    def __str__(self):
        return str(self.name)
    
class Appointment(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return f"Запись {self.name} с мастером {self.master}"
