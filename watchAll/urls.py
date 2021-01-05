from django.urls import path

from . import views

urlpatterns = [
    path('', views.listar_videos, name='inicio'),
    path('recurso/', views.agregar_recurso, name='agregarRecurso'),
    path('editar/<int:pk>', views.EditarVideo.as_view(), name='editarRecurso'),
    path('eliminar/<int:pk>', views.EliminarVideo.as_view(), name='eliminarRecurso'),
    path('misVideos/', views.VideosPersonales.as_view(), name='misVideos'),
    path('favoritos/', views.favoritos, name='favoritos'),
    path('add/<int:video_id>/<int:tipo>', views.agregrar_video_lista, name='agregarALista'),
    path('remove/<int:video_id>/<int:tipo>', views.eliminar_video_lista, name='removerALista'),
    path('masTarde/', views.ver_mas_tarde, name='masTarde'),
    path('ver/<int:video_id>', views.ver_video, name='ver_video'),
]