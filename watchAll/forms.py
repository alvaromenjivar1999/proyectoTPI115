from django.contrib.auth.forms import UserCreationForm
from watchAll.models import Video
from django import forms
from django.forms import ModelForm

class recursoForm(ModelForm):
    class Meta:
        model = Video
        fields = [
            "nombre",
            "fechaPublicacion",
            "categoria",
            "palabraClave",
            "recurso",
        ]
        labels = {
            "nombre": 'Titulo',
            "fechaPublicacion": 'Fecha de publicacion',
            "categoria": 'Categoria',
            "palabraClave": 'Palabra clave',
            "recurso": 'Recurso',
        }
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control'}),
            "fechaPublicacion": forms.DateInput(attrs={'class': 'form-control'}),
            "categoria": forms.TextInput(attrs={'class': 'form-control'}),
            "palabraClave": forms.TextInput(attrs={'class': 'form-control'}),
            "recurso": forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)