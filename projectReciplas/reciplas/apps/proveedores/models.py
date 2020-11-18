from django.db import models

# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    CUIT = models.IntegerField()
    razon_social = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    localidad = models.CharField(max_length=45)
    provincia = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    mail = models.CharField(max_length=45)
