from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.

def inicio(request):
    if request.user.is_authenticated:
        context = {}
        return render(request, 'cuenta/inicio.html', context)
    else:
        return redirect('logearse')