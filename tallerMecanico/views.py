from .models import Marca, Repuesto
from django.shortcuts import render

# IMPORTAR EL MODELO DE TABLA DE USUARIO DESDE EL ADMINISTRADOR
from django.contrib.auth.models import User
# IMPORTAR UNA LIBRERIA DE AUTENTIFICACION
from django.contrib.auth import authenticate, logout, login
# IMPORTAR LIBRERIA DECORADORA QUE EVITA EL INGRESO A LAS PAGINAS SIN AUTORIZACION
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, "index.html")


def trabajos(request):
    return render(request, "trabajos.html")


def registrarse(request):
    return render(request, "registrarse.html")


def cerrar_sesion(request):
    logout(request)
    return render(request, "index.html")


def iniciar(request):
    mensaje = ""
    if request.POST:
        nombre = request.POST.get("txtUsuario")
        contra = request.POST.get("txtPassword")
        us = authenticate(request, username=nombre, password=contra)
        if us is not None and us.is_active:
            login(request, us)
            return render(request, "index.html")
        else:
            mensaje = "Nombre de usuario o Contraseña son incorrectos"
    contexto = {"mensaje": mensaje}
    return render(request, "iniciarSesion.html", contexto)


def galeria_ventas(request):
    repuestos = Repuesto.objects.filter(publicar=True)
    marca = Marca.objects.all()
    contexto = {"repuestos": repuestos, "marca": marca}
    return render(request, "galeria_ventas.html", contexto)


def filtro_marcas(request):
    repuestos = Repuesto.objects.all()
    cant = Repuesto.objects.all().count()
    marca = Marca.objects.all()
    if request.POST:
        marcas = request.POST.get("cboCategoria")
        object_categoria = Marca.objects.get(nombre=marcas)
        repuestos = Repuesto.objects.filter(marcas=object_categoria)
        cant = Repuesto.objects.filter(marcas=object_categoria).count()
    contexto = {"repuestos": repuestos, "marca": marca, "cantidad": cant}
    return render(request, "galeria_ventas.html", contexto)


def filtro_marc(request, id):
    marca = Marca.objects.all()
    object_categoria = Marca.objects.get(nombre=id)
    repuestos = Repuesto.objects.filter(marcas=object_categoria)
    cant = Repuesto.objects.filter(marcas=object_categoria).count()
    contexto = {"repuestos": repuestos, "marca": marca, "cantidad": cant}
    return render(request, "galeria_ventas.html", contexto)


def buscar_repuesto(request):
    repuestos = Repuesto.objects.all()
    cant = Repuesto.objects.all().count()
    marca = Marca.objects.all()
    if request.POST:
        nombre = request.POST.get("txtNombre")
        repuestos = Repuesto.objects.filter(nombre__contains=nombre)
        cant = Repuesto.objects.filter(nombre__contains=nombre).count()
    contexto = {"repuestos": repuestos, "marca": marca, "cantidad": cant}
    return render(request, "galeria_ventas.html", contexto)


def detalle_repuestos(request, id):
    repuesto = Repuesto.objects.get(nombre=id)
    contexto = {"repuesto": repuesto}
    return render(request, "ficha.html", contexto)


@login_required(login_url='/iniciar/')
def ventas_repuestos(request):
    mensaje = ""
    if request.POST:
        nombre = request.POST.get("txtNombre")
        precio = request.POST.get("txtPrecio")
        desc = request.POST.get("txtDesc")
        cate = request.POST.get("cboCategoria")
        imagen = request.FILES.get("txtmg")
        object_categoria = Marca.objects.get(nombre=cate)
        rep = Repuesto(
            nombre=nombre,
            precio=precio,
            descripcion=desc,
            imagen=imagen,
            marcas=object_categoria
        )
        rep.save()
        mensaje = "grabo"
    marca = Marca.objects.all()
    repuestos = Repuesto.objects.all()
    contexto = {"marca": marca, "mensaje": mensaje, "repuestos": repuestos}
    return render(request, "ventas.html", contexto)


def mantencion1(request):
    return render(request, "mantencion1.html")


def mantencion2(request):
    return render(request, "mantencion2.html")


def mantencion3(request):
    return render(request, "mantencion3.html")


def mantencion4(request):
    return render(request, "mantencion4.html")


def mantencion5(request):
    return render(request, "mantencion5.html")


def mantencion6(request):
    return render(request, "mantencion6.html")


@login_required(login_url='/iniciar/')
def eliminar(request, id):
    try:
        rep = Repuesto.objects.get(nombre=id)
        rep.detele()
        mensaje = "se elimino un registro"
    except:
        mensaje = "no se elimino el registro"

    marca = Marca.objects.all()
    repuestos = Repuesto.objects.all()
    contexto = {"marca": marca, "mensaje": mensaje, "repuestos": repuestos}
    return render(request, "ventas.html", contexto)
