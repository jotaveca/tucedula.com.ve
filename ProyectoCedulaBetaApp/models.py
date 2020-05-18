from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
# Create your models here.

class Cedula(models.Model):
    tx_nac=models.CharField(max_length=20)
    nu_cedula=models.IntegerField()
    tx_nombre_apellido=models.CharField(max_length=100)
    tx_estado=models.CharField(max_length=100)
    tx_municipio=models.CharField(max_length=100)
    tx_parroquia=models.CharField(max_length=100)
    tx_centro_electoral=models.CharField(max_length=100)
    tx_direccion=models.TextField()
