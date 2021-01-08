from time import gmtime, strftime

from django.shortcuts import render, redirect
from watchAll.models import Video, Favoritos, VerMasTarde
from cuenta.models import Cuenta
from watchAll.forms import RecursoForm
from django.db.models import Q
from django.views.generic import UpdateView, DeleteView, ListView, TemplateView
from django.urls import reverse_lazy
from pytube import YouTube as YT


def ver_video(request, video_id):
    if request.user.is_authenticated:
        video = Video.objects.get(id=video_id)
        context = {'id': video_id, 'video': video}
        return render(request, 'ver.html', context)
    else:
        return redirect('loguearse')

def descarga(request, video_url, video_id):
    if request.user.is_authenticated:
        YT("www.youtube.com/watch?v="+video_url).streams.first().download()
        return redirect('inicio')
    else:
        return redirect('loguearse') 

def agregrar_video_lista(request, video_id, tipo):
    if request.user.is_authenticated:
        if tipo == 1:
            video = Video.objects.get(id=video_id)
            favoritos = Favoritos.objects.get(usuario=request.user)
            favoritos.videos.add(video)
            return redirect('favoritos')
        elif tipo == 2:
            video = Video.objects.get(id=video_id)
            ver_mas_tarde = VerMasTarde.objects.get(usuario=request.user)
            ver_mas_tarde.videos.add(video)
            return redirect('masTarde')
        else:
            return redirect('inicio')
    else:
        return redirect('loguearse')


def eliminar_video_lista(request, video_id, tipo):
    if request.user.is_authenticated:
        if tipo == 1:
            video = Video.objects.get(id=video_id)
            favoritos = Favoritos.objects.get(usuario=request.user)
            favoritos.videos.remove(video)
            return redirect('favoritos')
        elif tipo == 2:
            video = Video.objects.get(id=video_id)
            ver_mas_tarde = VerMasTarde.objects.get(usuario=request.user)
            ver_mas_tarde.videos.remove(video)
            return redirect('masTarde')
        else:
            return redirect('inicio')
    else:
        return redirect('loguearse')


def favoritos(request):
    if request.user.is_authenticated:
        videos_publicados = Favoritos.objects.filter(usuario=request.user).get
        tipoLista = "Favoritos"

        context = {'tipo': 1, 'titulo': tipoLista, 'videosPublicados': videos_publicados}
        return render(request, 'lista.html', context)
    else:
        return redirect('loguearse')


def ver_mas_tarde(request):
    if request.user.is_authenticated:
        videosPublicados = VerMasTarde.objects.filter(usuario=request.user).get
        tipoLista = "Ver mas tarde"

        context = {'tipo': 2, 'titulo': tipoLista, 'videosPublicados': videosPublicados}
        return render(request, 'lista.html', context)
    else:
        return redirect('loguearse')


def listar_videos(request):
    if request.user.is_authenticated:
        busqueda = request.GET.get("buscar")
        videosPublicados = Video.objects.order_by('-fechaPublicacion')[:10]

        if busqueda:
            videosPublicados = Video.objects.filter(
                Q(nombre__icontains=busqueda) |
                Q(palabraClave__icontains=busqueda) |
                Q(categoria__icontains=busqueda)
            ).distinct()

        context = {'videosPublicados': videosPublicados}
        return render(request, 'cuenta/inicio.html', context)
    else:
        return redirect('loguearse')


def agregar_recurso(request):
    if request.user.is_authenticated:
        form = RecursoForm()
        if request.method == 'POST':
            form = RecursoForm(request.POST)
            if form.is_valid():
                if "www.youtube.com/watch?v" in form.cleaned_data.get('recurso'):
                    fechaActual = strftime("%Y-%m-%d", gmtime())
                    nuevo_Recurso = Video(
                        nombre=form.cleaned_data.get('nombre'),
                        categoria=form.cleaned_data.get('categoria'),
                        palabraClave=form.cleaned_data.get('palabraClave'),
                    )
                    nuevo_Recurso = form.save(commit=False)
                    nuevo_Recurso.usuario = Cuenta.objects.get(
                        id=request.user.id)
                    nuevo_Recurso.fechaPublicacion = fechaActual
                    nuevo_Recurso.recurso = str(form.cleaned_data.get('recurso')).split("=")[1]
                    nuevo_Recurso.save()
                    return redirect('inicio')
                else:
                    context = {'form': form, 'error': 'No ingresaste correctamente el enlace de youtube'}
                    return render(request, 'agregarRecurso.html', context)
        context = {'form': form}
        return render(request, 'agregarRecurso.html', context)

    else:
        return redirect('loguearse')


class VideosPersonales(ListView):
    template_name = 'misVideos.html'
    context_object_name = 'videosPublicados'

    def get_queryset(self):
        return Video.objects.filter(usuario_id=self.request.user.id).order_by('-fechaPublicacion')[:10]


class VistaPrincipal(TemplateView):
    template_name = 'principal.html'


class EditarVideo(UpdateView):
    model = Video
    form_class = RecursoForm
    template_name = 'agregarRecurso.html'
    success_url = reverse_lazy('inicio')


class EditarCuenta(UpdateView):
    model = Cuenta
    form_class = RecursoForm
    template_name = 'agregarRecurso.html'
    success_url = reverse_lazy('inicio')


class EliminarVideo(DeleteView):
    model = Video
    template_name = 'verificacion.html'
    success_url = reverse_lazy('inicio')

