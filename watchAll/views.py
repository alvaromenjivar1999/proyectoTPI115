from django.shortcuts import get_object_or_404, render, redirect
from watchAll.models import Video
from cuenta.models import Cuenta
from watchAll.forms import recursoForm
from cuenta.forms import registroUsuario
from django.views.generic import ListView

# Create your views here.

'''
class VideoListView(ListView):
    model = Video
    videosPublicados = Video.objects.order_by('-fechaPublicacion')[:10]
    context = {'videosPublicados': videosPublicados}
    template_name = "cuenta/inicio.html"

'''


def agregar_recurso(request):
    if request.user.is_authenticated:
        form = recursoForm()

        if request.method == 'POST':
            form = recursoForm(request.POST)
            if form.is_valid():


                nuevo_Recurso = Video(
                    nombre=form.cleaned_data.get('nombre'),
                    fechaPublicacion=form.cleaned_data.get('fechaPublicacion'),
                    categoria=form.cleaned_data.get('categoria'),
                    palabraClave=form.cleaned_data.get('palabraClave'),
                )

                nuevo_Recurso = form.save(commit=False)
                nuevo_Recurso.usuario = Cuenta.objects.get(
                    id=request.user.id)
                recurso = str(form.cleaned_data.get('recurso'))
                splitRecurso = recurso.split("=")
                recursoPartida = splitRecurso[1]
                nuevo_Recurso.recurso = recursoPartida
                nuevo_Recurso.save()
                return redirect('inicio')

        context = {'form': form}
        return render(request, 'agregarRecurso.html', context)

    else:
        return redirect('registrar')

def inicio(request):
    if request.user.is_authenticated:
        videosPublicados = Video.objects.order_by('-fechaPublicacion')[:10]
        context = {'videosPublicados': videosPublicados}
        return render(request, 'cuenta/inicio.html', context)
    else:
        return redirect('logearse')
