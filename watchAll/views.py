from django.shortcuts import get_object_or_404, render, redirect
from watchAll.models import Video
from cuenta.models import Cuenta
from watchAll.forms import recursoForm
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.http import JsonResponse

# Create your views here.


class listaVideos(ListView):
    template_name = 'cuenta/inicio.html'
    context_object_name = 'videosPublicados'

    def get_queryset(self):
        return Video.objects.order_by('-fechaPublicacion')[:10]

def listarVideos(request):
    if request.user.is_authenticated:
        busqueda = request.GET.get("buscar")
        videosPublicados = Video.objects.order_by('-fechaPublicacion')[:10]

        if busqueda:
            videosPublicados = Video.objects.filter(
                Q(nombre__icontains=busqueda) |

                Q(categoria__icontains=busqueda)
            ).distinct()

        context = {'videosPublicados': videosPublicados}
        return render(request, 'cuenta/inicio.html', context)
    else:
        return redirect('logearse')




class videosPersonales(ListView):
    template_name = 'misVideos.html'
    context_object_name = 'videosPublicados'

    def get_queryset(self):
        return Video.objects.filter(usuario_id=self.request.user.id).order_by('-fechaPublicacion')[:10]


class editarVideo(UpdateView):
    model = Video
    form_class = recursoForm
    template_name = 'agregarRecurso.html'
    success_url = reverse_lazy('inicio')

class eliminarVideo(DeleteView):
    model = Video
    template_name = 'verificacion.html'
    success_url = reverse_lazy('inicio')

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
