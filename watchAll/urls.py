from django.urls import path

from . import views

urlpatterns = [
    path('', views.listarVideos, name='inicio'),
    path('recurso/', views.agregar_recurso, name='agregarRecurso'),
    path('editar/<int:pk>', views.editarVideo.as_view(), name='editarRecurso'),
    path('eliminar/<int:pk>', views.eliminarVideo.as_view(), name='eliminarRecurso'),
    path('misVideos/', views.videosPersonales.as_view(), name='misVideos'),
    path('favoritos/', views.favoritos, name='favoritos'),
    path('masTarde/', views.verMasTarde, name='masTarde'),
    path('ver/<int:video_id>', views.verVideo, name='verVideo'),
]