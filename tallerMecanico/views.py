from .models import Marca, Repuesto, Galeria
from django.shortcuts import render

# IMPORTAR EL MODELO DE TABLA DE USUARIO DESDE EL ADMINISTRADOR
from django.contrib.auth.models import User
# IMPORTAR UNA LIBRERIA DE AUTENTIFICACION
from django.contrib.auth import authenticate, logout, login
# IMPORTAR LIBRERIA DECORADORA QUE EVITA EL INGRESO A LAS PAGINAS SIN AUTORIZACION
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.


def index(request):
    marca = Marca.objects.all()
    repuestos = Repuesto.objects.filter(publicar=True).order_by('-nombre')[:6]
    contexto = {"repuestos": repuestos, "marca": marca}
    return render(request, "index.html", contexto)


def registrarse(request):
    mensaje = ""
    if request.POST:
        usuario = request.POST.get("txtUsuario")
        nombre = request.POST.get("txtNombre")
        apellido = request.POST.get("txtApellido")
        email = request.POST.get("txtEmail")
        pass1 = request.POST.get("txtPass1")

        try:
            usu = User.objects.get(username=usuario)
            mensaje = "Usuario ya existe"
        except:
            usu = User()
            usu.username = usuario
            usu.first_name = nombre
            usu.last_name = apellido
            usu.email = email
            usu.set_password(pass1)
            usu.save()
            mensaje = "Usuario creado"
    contexto = {"mensaje": mensaje}
    return render(request, "registrarse.html", contexto)


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
    cant = Repuesto.objects.filter(publicar=True).count()
    marca = Marca.objects.all()
    contexto = {"repuestos": repuestos, "marca": marca, "cantidad": cant}
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
    galeria = Galeria.objects.filter(repuesto=repuesto)
    contexto["galeria"] = galeria
    return render(request, "ficha.html", contexto)


@login_required(login_url='/iniciar/')
@permission_required('tallerMecanico.add_repuesto', login_url='/iniciar/')
def ventas_repuestos(request):
    mensaje = ""
    usuario_actual = request.user.username
    if request.POST:
        nombre = request.POST.get("txtNombre")
        precio = request.POST.get("txtPrecio")
        desc = request.POST.get("txtDesc")
        cate = request.POST.get("cboCategoria")
        imagen = request.FILES.get("txtImg")
        object_categoria = Marca.objects.get(nombre=cate)
        rep = Repuesto(
            nombre=nombre,
            precio=precio,
            descripcion=desc,
            imagen=imagen,
            marcas=object_categoria,
            usuario=usuario_actual
        )
        rep.save()
        mensaje = "grabo"
    marca = Marca.objects.all()
    usuario_actual = request.user.username
    repuestos = Repuesto.objects.filter(usuario=usuario_actual)
    cant = Repuesto.objects.filter(usuario=usuario_actual).count()
    contexto = {"marca": marca, "mensaje": mensaje,
                "repuestos": repuestos, "cant": cant}
    return render(request, "ventas.html", contexto)


@login_required(login_url='/iniciar/')
@permission_required('tallerMecanico.delete_repuesto', login_url='/iniciar/')
def eliminar(request, id):
    try:
        rep = Repuesto.objects.get(nombre=id)
        rep.delete()
        mensaje = "se elimino un registro"
    except:
        mensaje = "no se elimino el registro"

    marca = Marca.objects.all()
    repuestos = Repuesto.objects.filter(usuario=request.user.username)
    contexto = {"marca": marca, "mensaje": mensaje, "repuestos": repuestos}
    return render(request, "ventas.html", contexto)


@login_required(login_url='/iniciar/')
@permission_required('tallerMecanico.view_repuesto', login_url='/iniciar/')
def buscar_modificar(request, id):
    try:
        rep = Repuesto.objects.get(nombre=id)
        marca = Marca.objects.all()
        contexto = {"marca": marca, "repuesto": rep}
        return render(request, "modificar.html", contexto)
    except:
        mensaje = "no se elimino el registro"

    marca = Marca.objects.all()
    repuestos = Repuesto.objects.all()
    contexto = {"marca": marca, "mensaje": mensaje, "repuestos": repuestos}
    return render(request, "ventas.html", contexto)


@login_required(login_url='/iniciar/')
@permission_required('tallerMecanico.change_repuesto', login_url='/iniciar/')
def modificar(request):
    mensaje = ""
    if request.POST:
        nombre = request.POST.get("txtNombre")
        precio = request.POST.get("txtPrecio")
        desc = request.POST.get("txtDesc")
        cate = request.POST.get("cboCategoria")
        imagen = request.FILES.get("txtImg")
        object_categoria = Marca.objects.get(nombre=cate)
        try:
            rep = Repuesto.objects.get(nombre=nombre)
            rep.precio = precio
            rep.descripcion = desc
            rep.marcas = object_categoria

            if imagen is not None:
                rep.imagen = imagen

            rep.comentario = '--'
            rep.publicar = False
            rep.save()
            mensaje = "Modifico"
        except:
            mensaje = "No Modifico"
    marca = Marca.objects.all()
    repuestos = Repuesto.objects.filter(usuario=request.user.username)
    contexto = {"marca": marca, "mensaje": mensaje, "repuestos": repuestos}
    return render(request, "ventas.html", contexto)


def vender_rep(request, id):
    mensaje = ""
    try:
        rep = Repuesto.objects.filter(publicar=True).get(nombre=id)
        rep.duenno = request.user.username
        rep.publicar = False
        mensaje='--'
        rep.save()
        mensaje = "Gracias por su compra"
    except:
        mensaje = "Error en la compra"
    repuesto = Repuesto.objects.get(nombre=id)
    contexto = {"repuesto": repuesto, "mensaje": mensaje}
    return render(request, "ficha.html", contexto)


def admin_user(request):
    repuesto = Repuesto.objects.filter(duenno=request.user.username)
    contexto = {"repuesto": repuesto}
    return render(request, "admin_user.html", contexto)


def devolver(request, id):
    mensaje = ""
    try:
        rep = Repuesto.objects.filter(publicar=False).get(nombre=id)
        rep.duenno = '--'
        rep.save()
        mensaje = "Repuesto Devuelto con exito"
    except:
        mensaje = "Error en la Devolucion"

    repuesto = Repuesto.objects.filter(duenno=request.user.username)
    contexto = {"repuesto": repuesto, "mensaje": mensaje}
    return render(request, "admin_user.html", contexto)


def insertar_galeria(request):
    mensaje = ""
    if request.POST:
        nom_repuesto = request.POST.get("txtRepuesto")
        imagen = request.FILES.get("txtImg")

        object_rep = Repuesto.objects.get(nombre=nom_repuesto)
        gale = Galeria()
        gale.imagen=imagen
        gale.repuesto = object_rep
        gale.save()
        mensaje="Se guardo imagen en la galeria para el repuesto: "+nom_repuesto

    marca = Marca.objects.all()
    usuario_actual = request.user.username
    repuestos = Repuesto.objects.filter(usuario=usuario_actual)
    cant = Repuesto.objects.filter(usuario=usuario_actual).count()
    contexto = {"marca": marca, "mensaje": mensaje,
                "repuestos": repuestos, "cant": cant}
    return render(request, "ventas.html", contexto)