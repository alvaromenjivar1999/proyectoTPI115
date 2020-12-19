from django.contrib.auth.forms import UserCreationForm
from cuenta.models import Cuenta
from django import forms
from django.forms import CharField, Form, PasswordInput


class registroUsuario(UserCreationForm):
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
            "fechaNacimiento": forms.DateInput(attrs={'class': 'form-control'}),
            "sexo": forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)