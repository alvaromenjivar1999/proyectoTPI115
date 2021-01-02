from django.contrib.auth.forms import UserCreationForm
from cuenta.models import Cuenta
from django import forms


class RegistroUsuario(UserCreationForm):
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
            "email": forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tu correo electronico'}),
            "nombre": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tu primer nombre'}),
            "apellido": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tu primer apellido'}),
            "fechaNacimiento": forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tu fecha de nacimiento'}),
            "sexo": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tu sexo'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)