from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from ProyectoCedulaBetaApp.models import Cedula
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime, timedelta
from django.db.models import Count

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


def buscar_mapa(request):
    ve_dp='0'
    ve_ne='0'
    ve_su='0'
    ve_da='0'
    ve_bo='0'
    ve_ap='0'
    ve_ba='0'
    ve_me='0'
    ve_ta='0'
    ve_tr='0'
    ve_zu='0'
    ve_co='0'
    ve_po='0'
    ve_ca='0'
    ve_la='0'
    ve_ya='0'
    ve_fa='0'
    ve_am='0'
    ve_an='0'
    ve_ar='0'
    ve_df='0'
    ve_gu='0'
    ve_mi='0'
    ve_mo='0'
    ve_lg='0'
    if request.GET["nom"]:
        nombre=request.GET["nom"]
        estado=request.GET["est"]
        print("Nombre ",nombre," Estado ",estado)
        if nombre!="" and estado!="Venezuela":
            if estado == "dependencias federales":
                ve_dp = Cedula.objects.filter(tx_nombre_apellido__icontains=nombre,tx_estado__icontains=estado).count()
            if estado == "esparta":
                ve_ne = Cedula.objects.filter(tx_nombre_apellido__icontains=nombre,tx_estado__icontains=estado).count()
            if estado == "sucre":
                ve_su = Cedula.objects.filter(tx_nombre_apellido__icontains=nombre,tx_estado__icontains=estado).count()
            if estado == "amacuro":
                ve_da = Cedula.objects.filter(tx_nombre_apellido__icontains=nombre,tx_estado__icontains=estado).count()
            if estado == "bolivar":
                ve_bo = Cedula.objects.filter(tx_nombre_apellido__icontains=nombre,tx_estado__icontains=estado).count()
            if estado == "apure":
                ve_ap = Cedula.objects.filter(tx_nombre_apellido__icontains=nombre,tx_estado__icontains=estado).count()
            if estado == "barinas":
                ve_ba = Cedula.objects.filter(tx_nombre_apellido__icontains=nombre,tx_estado__icontains=estado).count()
            if estado == "merida":
                ve_me = Cedula.objects.filter(tx_nombre_apellido__icontains=nombre,tx_estado__icontains=estado).count()
            if estado =="tachira":
                ve_ta = Cedula.objects.filter(tx_nombre_apellido__icontains=nombre,tx_estado__icontains=estado).count()
            if estado =="trujillo":
                ve_tr = Cedula.objects.filter(tx_nombre_apellido__icontains=nombre,tx_estado__icontains=estado).count()
            if estado =="zulia":
                ve_zu = Cedula.objects.filter(tx_nombre_apellido__icontains=nombre,tx_estado__icontains=estado).count()
            if estado =="cojedes":
                ve_co = Cedula.objects.filter(tx_nombre_apellido__icontains=nombre,tx_estado__icontains=estado).count()
            if estado =="portuguesa":
                ve_po = Cedula.objects.filter(tx_nombre_apellido__icontains=nombre,tx_estado__icontains=estado).count()
            if estado =="carabobo":
                ve_ca = Cedula.objects.filter(tx_nombre_apellido__icontains=nombre,tx_estado__icontains=estado).count()
            if estado =="lara":
                ve_la = Cedula.objects.filter(tx_nombre_apellido__icontains=nombre,tx_estado__icontains=estado).count()
            if estado =="yaracuy":
                ve_ya = Cedula.objects.filter(tx_nombre_apellido__icontains=nombre,tx_estado__icontains=estado).count()
            if estado =="falcon":
                ve_fa = Cedula.objects.filter(tx_nombre_apellido__icontains=nombre,tx_estado__icontains=estado).count()
            if estado =="amazonas":
                ve_am = Cedula.objects.filter(tx_nombre_apellido__icontains=nombre,tx_estado__icontains=estado).count()
            if estado =="anzoategui":
                ve_an = Cedula.objects.filter(tx_nombre_apellido__icontains=nombre,tx_estado__icontains=estado).count()
            if estado =="aragua":
                ve_ar = Cedula.objects.filter(tx_nombre_apellido__icontains=nombre,tx_estado__icontains=estado).count()
            if estado =="capital":
                ve_df = Cedula.objects.filter(tx_nombre_apellido__icontains=nombre,tx_estado__icontains=estado).count()
            if estado =="guarico":
                ve_gu = Cedula.objects.filter(tx_nombre_apellido__icontains=nombre,tx_estado__icontains=estado).count()
            if estado =="miranda":
                ve_mi = Cedula.objects.filter(tx_nombre_apellido__icontains=nombre,tx_estado__icontains=estado).count()
            if estado =="monagas":
                ve_mo = Cedula.objects.filter(tx_nombre_apellido__icontains=nombre,tx_estado__icontains=estado).count()
            if estado =="vargas":
                ve_lg = Cedula.objects.filter(tx_nombre_apellido__icontains=nombre,tx_estado__icontains=estado).count()
            nombres=Cedula.objects.filter(tx_nombre_apellido__icontains=nombre,tx_estado__icontains=estado)
            paginator = Paginator(nombres, 10) # Show 10 contacts per page
            page = request.GET.get('page')
            try:
                page_obj = paginator.page(page)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return render(request, 'resultados_busqueda_mapa.html',{"ve_dp":ve_dp, "ve_ne":ve_ne, "ve_su":ve_su, "ve_da":ve_da, "ve_bo":ve_bo,
                                                                    "ve_ap":ve_ap, "ve_ba":ve_ba, "ve_me":ve_me, "ve_ta":ve_ta, "ve_tr":ve_tr,
                                                                    "ve_zu":ve_zu, "ve_co":ve_co, "ve_po":ve_po, "ve_ca":ve_ca, "ve_la":ve_la,
                                                                    "ve_ya":ve_ya, "ve_fa":ve_fa, "ve_am":ve_am, "ve_an":ve_an, "ve_ar":ve_ar,
                                                                    "ve_df":ve_df, "ve_gu":ve_gu, "ve_mi":ve_mi, "ve_mo":ve_mo, "ve_lg":ve_lg,
                                                                    "nombres":nombres,"query":nombre,"query2":estado,'page_obj': page_obj})
            mensaje="Busqueda exitosa."
        elif nombre!="" and estado=="Venezuela":
            estados = Cedula.objects.filter(tx_nombre_apellido__icontains=nombre).values('tx_estado').annotate(total=Count('tx_estado'))
            print("Estados ", estados)
            for rec in estados:
                if rec['tx_estado'] == "EDO. AMAZONAS":
                    ve_am = rec['total']
                    print("Amazonas ",ve_am)
                if rec['tx_estado'] == "EDO. LARA":
                    ve_la = rec['total']
                    print("Lara ",ve_la)
                if rec['tx_estado'] == "DTTO. CAPITAL":
                    ve_df =rec['total']
                    print("Distrito Capital",ve_df)
                if rec['tx_estado'] == "EDO. BARINAS":
                    ve_ba =rec['total']
                    print("Barinas",ve_ba)
                if rec['tx_estado'] == "EDO. GUARICO":
                    ve_gu =rec['total']
                    print("Guarico",ve_gu)
                # if rec['tx_estado'] == "EMBAJADA":
                #     ve_em =rec['total']
                #     print("Embajada ",ve_em)
                # else:
                #     ve_em ='0'
                if rec['tx_estado'] == "DEPENDENCIAS FEDERALES":
                    ve_dp =rec['total']
                    print("Dependencias Federales ",ve_dp)
                if rec['tx_estado'] == "EDO. MERIDA":
                    ve_me =rec['total']
                    print("Merida",ve_me)
                if rec['tx_estado'] == "EDO. ARAGUA":
                    ve_ar =rec['total']
                    print("Aragua ",ve_ar)
                if rec['tx_estado'] == "EDO.NVA.ESPARTA":
                    ve_ne =rec['total']
                    print("Nueva Esparta ",ve_ne)
                if rec['tx_estado'] == "EDO. ANZOATEGUI":
                    ve_an =rec['total']
                    print("Anzoategui",ve_an)
                if rec['tx_estado'] == "EDO. MIRANDA":
                    ve_mi =rec['total']
                    print("Miranda",ve_mi)
                if rec['tx_estado'] == "EDO. BOLIVAR":
                    ve_bo =rec['total']
                    print("Bolivar",ve_bo)
                if rec['tx_estado'] == "EDO. TRUJILLO":
                    ve_tr =rec['total']
                    print("Trujillo",ve_tr)
                if rec['tx_estado'] == "EDO. ZULIA":
                    ve_zu =rec['total']
                    print("Zulia ",ve_zu)
                if rec['tx_estado'] == "EDO. DELTA AMAC":
                    ve_da =rec['total']
                    print("Delta Amacuro",ve_da)
                if rec['tx_estado'] == "EDO. PORTUGUESA":
                    ve_po =rec['total']
                    print("Portuguesa",ve_po)
                if rec['tx_estado'] == "EDO. FALCON":
                    ve_fa =rec['total']
                    print("Falcon ",ve_fa)
                if rec['tx_estado'] == "EDO. CARABOBO":
                    ve_ca =rec['total']
                    print("Carabobo ",ve_ca)
                if rec['tx_estado'] == "EDO. VARGAS":
                    ve_lg =rec['total']
                    print("La Guaira",ve_lg)
                if rec['tx_estado'] == "EDO. SUCRE":
                    ve_su =rec['total']
                    print("Sucre ",ve_su)
                if rec['tx_estado'] == "EDO. APURE":
                    ve_ap =rec['total']
                    print("Apure ",ve_ap)
                if rec['tx_estado'] == "EDO. TACHIRA":
                    ve_ta =rec['total']
                    print("Tachira ",ve_ta)
                if rec['tx_estado'] == "EDO. COJEDES":
                    ve_co =rec['total']
                    print("Cojedes ",ve_co)
                if rec['tx_estado'] == "EDO. MONAGAS":
                    ve_mo =rec['total']
                    print("Monagas ",ve_mo)
                if rec['tx_estado'] == "EDO. YARACUY":
                    ve_ya =rec['total']
                    print("Yaracuy ",ve_ya)
                if rec['tx_estado'] == "DEPENDENCIAS FEDERALES":
                    ve_em =rec['total']
                    print("Embajada ",ve_em)
            nombres = Cedula.objects.filter(tx_nombre_apellido__icontains=nombre)
            paginator = Paginator(nombres, 10) # Show 10 contacts per page
            page = request.GET.get('page')
            try:
                page_obj = paginator.page(page)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return render(request, 'resultados_busqueda_mapa.html',{"ve_dp":ve_dp, "ve_ne":ve_ne, "ve_su":ve_su, "ve_da":ve_da, "ve_bo":ve_bo,
                                                                    "ve_ap":ve_ap, "ve_ba":ve_ba, "ve_me":ve_me, "ve_ta":ve_ta, "ve_tr":ve_tr,
                                                                    "ve_zu":ve_zu, "ve_co":ve_co, "ve_po":ve_po, "ve_ca":ve_ca, "ve_la":ve_la,
                                                                    "ve_ya":ve_ya, "ve_fa":ve_fa, "ve_am":ve_am, "ve_an":ve_an, "ve_ar":ve_ar,
                                                                    "ve_df":ve_df, "ve_gu":ve_gu, "ve_mi":ve_mi, "ve_mo":ve_mo, "ve_lg":ve_lg,
                                                                    "nombres":nombres,"query":nombre,"query2":estado,'page_obj': page_obj})
            mensaje="Busqueda exitosa."
    else:
        mensaje="Por favor, debe ingresar el nombre para poder realizar la busqueda."
    return HttpResponse(mensaje)