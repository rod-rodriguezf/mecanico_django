from django.contrib import admin
from django.urls import path, include
from .views import insertar_galeria, devolver, admin_user, vender_rep, modificar, buscar_modificar, eliminar, cerrar_sesion, filtro_marc, buscar_repuesto, filtro_marcas, galeria_ventas, index, registrarse, iniciar, ventas_repuestos, galeria_ventas, detalle_repuestos

urlpatterns = [
    path('', index, name='INDEX'),
    path('registrarse/', registrarse, name='REGISTRARSE'),
    path('iniciar/', iniciar, name='INICIAR'),
    path('ventas/', ventas_repuestos, name='VENTAS'),
    path('res_dispó/', galeria_ventas, name='GALE_VENTAS'),
    path('deta_repues/<id>/', detalle_repuestos, name='DETA_REPUES'),
    path('filtro_marcas/', filtro_marcas, name="FILTRO_MARCA"),
    path('buscar_repuesto/', buscar_repuesto, name="BUSCAR_REP"),
    path('filtro_marc/<id>/', filtro_marc, name="FILTRO_MARC"),
    path('cerrar_sesion/', cerrar_sesion, name="CERRAR_SESION"),
    path('eliminar/<id>/', eliminar, name="ELIMINAR"),
    path('buscar_modificar/<id>/', buscar_modificar, name="BUSCARM"),
    path('modificar/', modificar, name="MODI"),
    path('vender_rep/<id>/', vender_rep, name="VENDER"),
    path('admin_user/', admin_user, name="ADMIN_USER"),
    path('devolver/<id>/', devolver, name="DEVOLVER"),
    path('insertar_galeria/', insertar_galeria, name="INSERT"),
]
