from .models import Marca, Repuesto
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")


def trabajos(request):
    return render(request, "trabajos.html")


def registrarse(request):
    return render(request, "registrarse.html")


def iniciar(request):
    return render(request, "iniciarSesion.html")


def galeria_ventas(request):
    repuestos = Repuesto.objects.all()
    contexto = {"repuestos":repuestos}
    return render(request, "galeria_ventas.html",contexto)


def ventas_repuestos(request):
    marca = Marca.objects.all()
    contexto = {"marca": marca}
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
