from django.contrib import admin
from django.urls import path, include
from .views import modificar,buscar_modificar,eliminar, cerrar_sesion, filtro_marc, buscar_repuesto, filtro_marcas, galeria_ventas, index, trabajos, registrarse, iniciar, mantencion1, mantencion2, mantencion3, mantencion4, mantencion5, mantencion6, ventas_repuestos, galeria_ventas, detalle_repuestos

urlpatterns = [
    path('', index, name='INDEX'),
    path('trabajos/', trabajos, name='TRABAJOS'),
    path('registrarse/', registrarse, name='REGISTRARSE'),
    path('iniciar/', iniciar, name='INICIAR'),
    path('ventas/', ventas_repuestos, name='VENTAS'),
    path('mantencion1/', mantencion1, name='MANTENCION1'),
    path('mantencion2/', mantencion2, name='MANTENCION2'),
    path('mantencion3/', mantencion3, name='MANTENCION3'),
    path('mantencion4/', mantencion4, name='MANTENCION4'),
    path('mantencion5/', mantencion5, name='MANTENCION5'),
    path('mantencion6/', mantencion6, name='MANTENCION6'),
    path('res_dispó/', galeria_ventas, name='GALE_VENTAS'),
    path('deta_repues/<id>/', detalle_repuestos, name='DETA_REPUES'),
    path('filtro_marcas/', filtro_marcas, name="FILTRO_MARCA"),
    path('buscar_repuesto/', buscar_repuesto, name="BUSCAR_REP"),
    path('filtro_marc/<id>/', filtro_marc, name="FILTRO_MARC"),
    path('cerrar_sesion/', cerrar_sesion, name="CERRAR_SESION"),
    path('eliminar/<id>/', eliminar, name="ELIMINAR"),
    path('buscar_modificar/<id>/', buscar_modificar, name="BUSCARM"),
    path('modificar/',modificar,name="MODI"),

]
