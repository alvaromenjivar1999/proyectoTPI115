from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from cuenta.forms import registroUsuario
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from cuenta.models import Cuenta
from django.views import generic


# Create your views here.


def registrar(request):
    form = registroUsuario()

    if request.method == 'POST':
        form = registroUsuario(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request)
            return redirect('logearse')


    context = {'form': form}
    return render(request, 'cuenta/registro.html', context)


def logearse(request):
    if not request.user.is_authenticated:

        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            usuario = authenticate(request, email=email, password=password)

            if usuario is not None:
                login(request, usuario)
                return redirect('inicio')
            else:
                messages.error(request, 'Usuario o contraseña incorrecta')

        context = {}
        return render(request, 'cuenta/login.html', context)

    else:
        return redirect('inicio')

def cerrarSesion(request):
    logout(request)
    return redirect('logearse')

def inicio(request):
    context = {}
    return render(request, 'cuenta/inicio.html', context)