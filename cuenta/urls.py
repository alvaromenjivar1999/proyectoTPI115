from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar, name='registrar'),
    path('login/', views.loguearse, name='loguearse'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('firstlogin/', views.first_loguearse, name='first_loguearse'),
    path('reset/', views.reset_password, name='reset'),
    path('new/<str:token>/', views.reset_new_password, name='password'),

]
