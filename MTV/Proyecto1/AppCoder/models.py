from django.db import models

# Create your models here.
class familiares(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_de_nacimiento = models.DateField()