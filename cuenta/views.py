from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from cuenta.forms import registroUsuario
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from cuenta.models import Cuenta
from django.views import generic

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.template.loader import render_to_string
from proyectoTPI115  import settings


#funcion para enviar correo 
def send_email(request,correo):
    try:
        URL = settings.DOMINIO if not settings.DEBUG else request.META['HTTP_HOST']
        # Establecemos conexion con el servidor smtp de gmail
        mailServer = smtplib.SMTP('smtp.gmail.com', 587)
        print(mailServer.ehlo())
        mailServer.starttls()
        print(mailServer.ehlo())
        mailServer.login("pruebatpi5@gmail.com", "tpiues115")
        print('conectado..')

        # Construimos el mensaje simple
        mensaje = MIMEMultipart()
        mensaje['From'] = "pruebatpi5@gmail.com"
        mensaje['To'] = correo
        mensaje['Subject'] = "Tienes un correo"
       
        content = render_to_string('cuenta/correo.html' ,{
            'user':Cuenta,'link':'http://{}/firstlogin'.format(URL),
            })
        # Adjuntamos el texto
        mensaje.attach(MIMEText(content, 'html'))

        # Envio del mensaje
        mailServer.sendmail("pruebatpi5@gmail.com",
                            correo,
                            mensaje.as_string())

        print('correo enviado ')
    except Exception as e:
        print(e)


# Create your views here.


def registrar(request):
    if not request.user.is_authenticated:
        form = registroUsuario()
        if request.method == 'POST':
            form = registroUsuario(request.POST)
            if form.is_valid():
                #form.save()
                #correo = form.data.get('email')
                correo = request.POST.get('email')
                send_email(request,correo)
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

def cerrarSesion(request):
    logout(request)
    return redirect('loguearse')


def first_loguearse(request):
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