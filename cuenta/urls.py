from django.urls import path

from . import views

urlpatterns = [
    path('registrar/', views.registrar, name='registrar'),
    path('login/', views.logearse, name='logearse'),
    path('logout/', views.cerrarSesion, name='logout'),
]