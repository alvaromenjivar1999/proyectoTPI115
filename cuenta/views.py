from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from cuenta.forms import registroUsuario,reset
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from cuenta.models import Cuenta
from django.views import generic

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.template.loader import render_to_string
from proyectoTPI115  import settings
import uuid


#funcion para enviar correo
def send_email(request,correo,usuario):
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
        mensaje['Subject'] = "Activacion de cuenta"
        content = render_to_string('cuenta/correo.html' ,{
            'usuario':usuario,
            'link':'http://{}/firstlogin'.format(URL),
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

def send_email_reset(request,correo,usuario):
    use = Cuenta.objects.get(email = correo)
    use.token = uuid.uuid4()
    use.save()
    try:
        URL = settings.DOMINIO if not settings.DEBUG else request.META['HTTP_HOST']
        # Establecemos conexion con el servidor smtp de gmail
        mailServer = smtplib.SMTP('smtp.gmail.com', 587)
        print(mailServer.ehlo())
        mailServer.starttls()
        print(mailServer.ehlo())
        mailServer.login("pruebatpi5@gmail.com", "tpiues115")
        print('conectado..')
        token = Cuenta.objects.get(email = correo)
        print()
        # Construimos el mensaje simple
        mensaje = MIMEMultipart()
        mensaje['From'] = "pruebatpi5@gmail.com"
        mensaje['To'] = correo
        mensaje['Subject'] = "Cambio de contraseña"
        content = render_to_string('cuenta/reset_correo.html' ,{
            'usuario':usuario,
            'link':'http://{}/new/{}/'.format(URL,str(token.token)),
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
            messages.warning(request,'hasta a qui')

            if form.is_valid():
                form.save()
                correo = request.POST.get('email')
                usuario = request.POST.get('nombre')
                send_email(request,correo,usuario)
                return render(request,'cuenta/envio_correo.html')

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


def first_loguearse(request):
    if not request.user.is_authenticated:

        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            pase = Cuenta.objects.get( email = email)
            pase.is_active = True
            pase.save()
            usuario = authenticate(request, email=email, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect('inicio')
            else:
                messages.error(request, 'Usuario o contraseña incorrecta')
                return render(request, 'cuenta/firts_login.html', context)
        context = {}
        return render(request, 'cuenta/firts_login.html', context)

    else:
        return redirect('inicio')

def reset_password(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            email = request.POST.get('email')
            if Cuenta.objects.filter(email =email).exists():
                p = Cuenta.objects.get(email = email)
                usuario = p.nombre
                send_email_reset(request,email,usuario)
                return render(request,'cuenta/envio_correo.html')
            else:
                return render(request, 'cuenta/reset.html')
        else:
            return render(request,'cuenta/reset.html')
    else:
        return redirect('inicio')

def reset_new_password(request,token):
    if not request.user.is_authenticated:
        if Cuenta.objects.filter(token=token).exists():
            form = reset()
            if  request.method == 'POST':
                password = request.POST.get('password1')
                password2 = request.POST.get('password2')
                if password == password2:
                    usuario = Cuenta.objects.get( token = token)
                    usuario.set_password(password)
                    usuario.save()
                    messages.error(request,'su contraseña a sido actiualizada')
                    return render(request,'cuenta/login.html')
                else:
                    messages.error(request,'las contraseñas deben ser iguales')
                    return render(request, 'cuenta/reset_password.html', {'form': form})
            else:
                return render(request, 'cuenta/reset_password.html', {'form': form})
        else:
            return render(request, 'cuenta/login.html')
    else:
        return redirect('inicio')
