from django.shortcuts import render, redirect
from cuenta.forms import registroUsuario
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def registrar(request):
    if not request.user.is_authenticated:

        form = registroUsuario()
        if request.method == 'POST':
            form = registroUsuario(request.POST)
            messages.warning(request,'hasta a qui')

            if form.is_valid():
                form.save()
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
                context = {'error': 'Usuario o contraseña incorrecta'}
                return render(request, 'cuenta/login.html', context)

        context = {}
        return render(request, 'cuenta/login.html', context)

    else:
        return redirect('inicio')


def cerrar_sesion(request):
    logout(request)
    return redirect('loguearse')

