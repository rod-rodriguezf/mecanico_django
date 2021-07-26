from django.shortcuts import render
from rest_framework import generics
from tallerMecanico.models import Repuesto
from .serializers import RepuestosSerializers

# Create your views here.


class RepuestosViewSet(generics.ListAPIView):
    queryset = Repuesto.objects.all()
    serializer_class = RepuestosSerializers


class RepuestosCreateViewSet(generics.ListCreateAPIView):
    queryset = Repuesto.objects.all()
    serializer_class = RepuestosSerializers


class RepuestosBuscarViewSet(generics.ListAPIView):
    serializer_class = RepuestosSerializers
    def get_queryset(self):
        nombre_repuesto = self.kwargs['nombre']
        return Repuesto.objects.filter(nombre=nombre_repuesto)

