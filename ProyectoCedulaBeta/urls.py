"""ProyectoCedulaBeta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path
from ProyectoCedulaBetaApp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('cedula/', views.busqueda_cedula),
    path('buscar_cedula/', views.buscar_cedula),
    path('contacto/', views.contacto),
    path('nombre/', views.busqueda_nombre),
    path('buscar_nombre/', views.buscar_nombre),
    path('buscar_nombre_cantidad/', views.buscar_nombre_cantidad),
    path('mapa/', views.busqueda_mapa),
    path('buscar_mapa/', views.buscar_mapa),
]

urlpatterns += staticfiles_urlpatterns()

