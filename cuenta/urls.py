from django.urls import path

from . import views

urlpatterns = [
    path('registrar/', views.registrar, name='registrar'),
    path('login/', views.loguearse, name='loguearse'),
    path('logout/', views.cerrarSesion, name='logout'),
    path('firstlogin/', views.first_loguearse, name='first_loguearse'),
]