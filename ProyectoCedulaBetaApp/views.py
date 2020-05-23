from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from ProyectoCedulaBetaApp.models import Cedula
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime, timedelta

# Create your views here.

def contacto(request):
    if request.method=="POST":
        subject=request.POST["name"]
        message=request.POST["name"]  + " le envia este mensaje. " + request.POST["message"] + ".Correo: " + request.POST["email"] + ".Telefono: " + request.POST["phone"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["tucedulavenezuela@gmail.com"]
        send_mail(subject,message,email_from,recipient_list)
        return render(request, "gracias.html")
    return render(request, "contacto.html")

def busqueda_cedula(request):
    return render(request, "busqueda_cedula.html")

def busqueda_nombre(request):
    return render(request, "busqueda_nombre.html")

def busqueda_mapa(request):
    return render(request, "busqueda_mapa.html")

def index(request):
    return render(request, "index.html")

def buscar_cedula(request):
    if request.GET["ced"]:
        cedula=request.GET["ced"]
        if len(cedula)>9:
            mensaje = "Texto de la cedula es demasiado largo"
        else:
            cedulas=Cedula.objects.filter(nu_cedula__icontains=cedula)  # __icontains es como like nombre ="", en ambos lados
            paginator = Paginator(cedulas, 10) # Show 10 contacts per page
            page = request.GET.get('page')
            try:
                page_obj = paginator.page(page)
            except PageNotAnInteger:page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return render(request, 'resultados_busqueda_cedula.html',{"cedulas":cedulas,"query":cedula,'page_obj': page_obj})
    else:
        mensaje="Por favor, debe ingresar el numero de cedula para poder realizar la busqueda."
    return HttpResponse(mensaje)  

def buscar_nombre(request):
    if request.GET["nom"]:
        nombre=request.GET["nom"]
        if len(nombre)>30:
            mensaje = "Texto del nombre y/o apellido es demasiado largo"
        else:
            nombres=Cedula.objects.filter(tx_nombre_apellido__icontains=nombre)
            paginator = Paginator(nombres, 10) # Show 10 contacts per page
            page = request.GET.get('page')
            try:
                page_obj = paginator.page(page)
            except PageNotAnInteger:page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return render(request, 'resultados_busqueda_nombre.html',{"nombres":nombres,"query":nombre,'page_obj': page_obj})
    else:
        mensaje="Por favor, debe ingresar el nombre y/o apellido para poder realizar la busqueda."
    return HttpResponse(mensaje)        
    
def buscar_nombre_cantidad(request):
    if request.GET["nom"]:
        nombre=request.GET["nom"]
        if len(nombre)>50:
            mensaje = "Texto del nombre es demasiado largo"
        else:
            nombres=Cedula.objects.filter(tx_nombre_apellido__icontains=nombre)  # __icontains es como like nombre ="", en ambos lados
            return render(request, "busqueda_nombre_cantidad.html",{"nombres":nombres,"query":nombre})
    else:
        mensaje="Por favor, debe ingresar el nombre para poder realizar la busqueda."
    return HttpResponse(mensaje)