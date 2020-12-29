from django.contrib.auth.forms import UserCreationForm
from cuenta.models import Cuenta
from django import forms
from django.forms import CharField, Form


class registroUsuario(UserCreationForm):
    password = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Ingrese su contraseña',
            'id' : 'password',
            'required' : 'required',
        }
    ))
    password2 = forms.CharField(label = 'Contraseña de confirmación', widget = forms.PasswordInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Ingrese nuevamente su contraseña',
            'id' : 'password2',
            'required' : 'required',
        }
    ))
    class Meta:
        model = Cuenta
        fields = [
            "email",
            "nombre",
            "apellido",
            "fechaNacimiento",
            "sexo",
        ]
        labels = {
            "email": 'Correo electronico',
            "nombre": 'Nombre',
            "apellido": 'Apellido',
            "fechaNacimiento": 'Fecha de nacimiento',
            "sexo": 'Sexo',
        }
        widgets = {
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
            "nombre": forms.TextInput(attrs={'class': 'form-control'}),
            "apellido": forms.TextInput(attrs={'class': 'form-control'}),
            "fechaNacimiento": forms.DateInput(attrs={'type':'date', 'class': 'form-control'}),
            "sexo": forms.Select(attrs={'class': 'form-control'}),
        }

   # def __init__(self, *args, **kwargs): 
    #    super().__init__(*args, **kwargs)