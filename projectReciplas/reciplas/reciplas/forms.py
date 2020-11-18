

from django.forms import ModelForm
from apps.proveedores.models import Proveedor
from django import forms


class ProvForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre','apellido','CUIT','razon_social','direccion','localidad','provincia','telefono','mail']
        widgets= {
                'nombre':forms.TextInput(attrs={'class':'form-control  mb-4',},),
                'apellido': forms.TextInput(attrs={'class': 'form-control mb-4'}),
                'CUIT': forms.TextInput(attrs={'class': 'form-control mb-4'}),
                'razon_social': forms.TextInput(attrs={'class': 'form-control mb-4'}),
                'direccion': forms.TextInput(attrs={'class': 'form-control mb-4'}),
                'localidad': forms.TextInput(attrs={'class': 'form-control mb-4'}),
                'provincia': forms.TextInput(attrs={'class': 'form-control mb-4'}),
                'telefono': forms.TextInput(attrs={'class': 'form-control mb-4'}),
                'mail': forms.TextInput(attrs={'class': 'form-control mb-4'}),
        }
    