from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .models import Juego
from Aplicaciones.Coleccionista.models import Coleccionista
from Aplicaciones.Editorial.models import Editorial
from .forms import JuegoForm  # Importa el formulario para validación

def inicio(request):
    return render(request, 'inicio.html')

# Listar Juegos
def listaJuego(request):
    juegos = Juego.objects.all()
    return render(request, 'juego/inicio.html', {'juegos': juegos})

# Formulario nuevo juego (mostrar y validar)
def nuevoJuego(request):
    if request.method == "POST":
        form = JuegoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Juego guardado correctamente.")
            return redirect(reverse('lista_juego'))
        else:
            # Si hay errores, vuelves a mostrar el formulario con errores
            return render(request, 'juego/nuevo.html', {'form': form})
    else:
        form = JuegoForm()
        return render(request, 'juego/nuevo.html', {'form': form})

# Formulario editar juego (mostrar y validar)
def editarJuego(request, id):
    juego = get_object_or_404(Juego, id=id)
    if request.method == "POST":
        form = JuegoForm(request.POST, instance=juego)
        if form.is_valid():
            form.save()
            messages.success(request, "Juego editado correctamente.")
            return redirect(reverse('lista_juego'))
        else:
            # Mostrar formulario con errores
            return render(request, 'juego/editar.html', {'form': form, 'juego': juego})
    else:
        form = JuegoForm(instance=juego)
        return render(request, 'juego/editar.html', {'form': form, 'juego': juego})

# Eliminar juego
def eliminarJuego(request, id):
    juego = get_object_or_404(Juego, id=id)
    juego.delete()
    messages.success(request, "Juego eliminado correctamente.")
    return redirect(reverse('lista_juego'))
