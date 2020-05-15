from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from ProyectoCedulaBetaApp.models import Cedula
# Create your views here.

def contacto(request):
    if request.method=="POST":
        subject=request.POST["name"]
        message=request.POST["name"]  + " le envia este mensaje. " + request.POST["message"] + ".Correo: " + request.POST["email"] + ".Telefono: " + request.POST["phone"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["eam.rodriguez@gmail.com"]
        send_mail(subject,message,email_from,recipient_list)
        return render(request, "gracias.html")
    return render(request, "contacto.html")

def busqueda_cedula(request):
    return render(request, "busqueda_cedula.html")

def busqueda_nombre(request):
    return render(request, "busqueda_nombre.html")

def index(request):
    return render(request, "index.html")

def buscar_cedula(request):
    if request.GET["ced"]:
        cedula=request.GET["ced"]
        if len(cedula)>9:
            mensaje = "Texto de la cedula es demasiado largo"
        else:
            cedulas=Cedula.objects.filter(cedula__icontains=cedula)  # __icontains es como like nombre ="", en ambos lados
            return render(request, "resultados_busqueda.html",{"cedulas":cedulas,"query":cedula})
    else:
        mensaje="Por favor, debe ingresar el numero de cedula para poder realizar la busqueda."
    return HttpResponse(mensaje)

def buscar_nombre(request):
    if request.GET["nom"]:
        nombre=request.GET["nom"]
        if len(nombre)>20:
            mensaje = "Texto del nombre es demasiado largo"
        else:
            nombres=Cedula.objects.filter(nombre__icontains=nombre)  # __icontains es como like nombre ="", en ambos lados
            return render(request, "resultados_busqueda.html",{"nombres":nombres,"query":nombre})
    else:
        mensaje="Por favor, debe ingresar el nombre para poder realizar la busqueda."
    return HttpResponse(mensaje)