from django.contrib import admin
from ProyectoCedulaBetaApp.models import Cedula
 
# Register your models here.

class CedulaAdmin(admin.ModelAdmin):
    list_display=("tx_nac","tx_nombre_apellido","nu_cedula","tx_estado","tx_municipio","tx_parroquia","tx_direccion","tx_centro_electoral") #Panel Vista Lista    nombre=models.CharField(max_length=50)
    search_fields=("tx_nac","tx_nombre_apellido","nu_cedula","tx_estado","tx_municipio","tx_parroquia","tx_direccion","tx_centro_electoral") #Panel de Busqueda 
    list_filter=("tx_nac","tx_nombre_apellido","nu_cedula","tx_estado","tx_municipio","tx_parroquia","tx_direccion","tx_centro_electoral") # Panel Filtro de Busqueda
    
admin.site.register(Cedula,CedulaAdmin)
