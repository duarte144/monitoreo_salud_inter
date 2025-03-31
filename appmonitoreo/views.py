from django.shortcuts import render, redirect, get_object_or_404
from .models import Gato, RegistroTemperatura
from .forms import GatoForm, RegistroTemperaturaForm
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirige a la página de inicio o dashboard
            return redirect('dashboard')  # Cambia 'dashboard' por el nombre de la URL a la que quieras redirigir
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
            return render(request, 'login.html')
    return render(request, 'login.html')


def index(request):
    gatos = Gato.objects.all()
    registros = RegistroTemperatura.objects.all()
    return render(request, 'appmonitoreo/index.html', {'gatos': gatos, 'registros': registros})

def agregar_gato(request):
    if request.method == 'POST':
        form = GatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GatoForm()
    return render(request, 'appmonitoreo/agregar_gato.html', {'form': form})

def editar_gato(request, gato_id):
    gato = get_object_or_404(Gato, id=gato_id)
    if request.method == 'POST':
        form = GatoForm(request.POST, instance=gato)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GatoForm(instance=gato)
    return render(request, 'appmonitoreo/editar_gato.html', {'form': form, 'gato': gato})

def eliminar_gato(request, gato_id):
    gato = get_object_or_404(Gato, id=gato_id)
    if request.method == 'POST':
        gato.delete()
        return redirect('index')
    return render(request, 'appmonitoreo/eliminar_gato.html', {'gato': gato})

def agregar_registro(request):
    if request.method == 'POST':
        form = RegistroTemperaturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegistroTemperaturaForm()
    return render(request, 'appmonitoreo/agregar_registro.html', {'form': form})

def editar_registro(request, registro_id):
    registro = get_object_or_404(RegistroTemperatura, id=registro_id)
    if request.method == 'POST':
        form = RegistroTemperaturaForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegistroTemperaturaForm(instance=registro)
    return render(request, 'appmonitoreo/editar_registro.html', {'form': form, 'registro': registro})

def eliminar_registro(request, registro_id):
    registro = get_object_or_404(RegistroTemperatura, id=registro_id)
    if request.method == 'POST':
        registro.delete()
        return redirect('index')
    return render(request, 'appmonitoreo/eliminar_registro.html', {'registro': registro})


def custom_logout(request):
    logout(request)
    messages.success(request, "Has cerrado sesión exitosamente.")
    return redirect("login")  # Redirige a la página de inicio de sesión o index
