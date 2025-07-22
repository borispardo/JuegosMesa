from django.shortcuts import render, redirect, get_object_or_404
from .models import Coleccionista
from .forms import ColeccionistaForm
from django.contrib import messages

def listaColeccionista(request):
    coleccionistas = Coleccionista.objects.all()
    return render(request, 'coleccionista/inicio.html', {'coleccionistas': coleccionistas})

def nuevoColeccionista(request):
    if request.method == 'POST':
        form = ColeccionistaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Coleccionista guardado correctamente.")
            return redirect('lista_coleccionista')
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")
    else:
        form = ColeccionistaForm()
    return render(request, 'coleccionista/nuevo.html', {'form': form})

def editarColeccionista(request, id):
    coleccionista = get_object_or_404(Coleccionista, id=id)
    if request.method == 'POST':
        form = ColeccionistaForm(request.POST, instance=coleccionista)
        if form.is_valid():
            form.save()
            messages.success(request, "Coleccionista editado correctamente.")
            return redirect('lista_coleccionista')
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")
    else:
        form = ColeccionistaForm(instance=coleccionista)
    return render(request, 'coleccionista/editar.html', {'form': form, 'coleccionista': coleccionista})

def eliminarColeccionista(request, id):
    coleccionista = get_object_or_404(Coleccionista, id=id)
    coleccionista.delete()
    messages.success(request, "Coleccionista eliminado correctamente.")
    return redirect('lista_coleccionista')
