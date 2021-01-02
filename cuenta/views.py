from django.shortcuts import render, redirect
from cuenta.forms import RegistroUsuario
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def registrar(request):
    if not request.user.is_authenticated:
        form = RegistroUsuario()

        if request.method == 'POST':
            form = RegistroUsuario(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request)
                return redirect('loguearse')

        context = {'form': form}
        return render(request, 'cuenta/registro.html', context)
    else:
        return redirect('inicio')


def loguearse(request):
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


def cerrar_sesion(request):
    logout(request)
    return redirect('loguearse')

