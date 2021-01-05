from watchAll.models import Video
from django import forms
from django.forms import ModelForm


class RecursoForm(ModelForm):
    class Meta:
        model = Video
        fields = [
            "nombre",
            "categoria",
            "palabraClave",
            "recurso",
        ]
        labels = {
            "nombre": 'Titulo',
            "categoria": 'Categoria',
            "palabraClave": 'Palabra clave',
            "recurso": 'Recurso',
        }
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el titutlo del video que publicaras'}),
            "categoria": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe la categoria del video, ej: Musica'}),
            "palabraClave": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe una palabra clave para el video, ej: robotica'}),
            "recurso": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pega el enlace de youtube del video que agregaras, ej: www.youtube.com/watch?v=vAqvbLs77xE'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)