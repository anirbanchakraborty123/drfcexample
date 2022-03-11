from django.db import models
#from django.db.models import Model

# Create your models here.

class Engine(models.Model):
    displacement = models.CharField(max_length=50)
    power = models.CharField(max_length=50)
    maker = models.CharField(max_length=30)

class Price(models.Model):
    price = models.IntegerField()

class CarModel(models.Model):
    car_name = models.CharField(max_length=32)
    engine = models.ForeignKey(Engine, on_delete=models.CASCADE, blank=True, null=True)
    price = models.ForeignKey(Price, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.car_name