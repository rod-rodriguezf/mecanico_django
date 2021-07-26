from django.db import models
from django.db.models import fields
from tallerMecanico.models import Repuesto
from rest_framework import serializers

class RepuestosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Repuesto
        #fields = ["nombre", "precio", "descripcion", "marcas", "imagen"]
        fields = "__all__"