from django.urls import path

from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('recurso/', views.agregar_recurso, name='agregarRecurso')
]