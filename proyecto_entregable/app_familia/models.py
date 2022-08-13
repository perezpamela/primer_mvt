from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre = models.CharField(max_length=70)
    apellido = models.CharField(max_length=70)
    fecha_nacimiento = models.DateField()
    cantidad_hijos = models.IntegerField(default=0)
    tiene_mascotas = models.BooleanField()
