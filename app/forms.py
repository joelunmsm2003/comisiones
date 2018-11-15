from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.forms import *
from app.models import *
from django.forms import ModelForm, TextInput

class AgenteForm(ModelForm):
    class Meta:
        model = Agente
        fields = ('id','nombre','dni','telefono','direccion','equipo')
        widgets = {
            'id':TextInput(attrs={'class':'form-control'}),
            'nombre':TextInput(attrs={'class':'form-control'}),
            'dni':TextInput(attrs={'class':'form-control'}),
            'telefono':TextInput(attrs={'class':'form-control'}),
            'direccion':TextInput(attrs={'class':'form-control'}),
            'equipo':Select(attrs={'class':'form-control'})

        }

class PolizaForm(ModelForm):
    class Meta:
        model = Poliza
        fields = ('agente','codigo','ramo_compania_producto')
        widgets = {

            'agente':Select(attrs={'class':'form-control'}),
            'codigo':TextInput(attrs={'class':'form-control'}),
            'ramo_compania_producto':Select(attrs={'class':'form-control'}),


        }

