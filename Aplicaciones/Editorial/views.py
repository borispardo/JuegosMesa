from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Editorial
from .forms import EditorialForm  # Importa el formulario

def listaEditorial(request):
    editoriales = Editorial.objects.all()
    return render(request, 'editorial/inicio.html', {'editoriales': editoriales})

def nuevoEditorial(request):
    if request.method == "POST":
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Editorial guardada correctamente.")
            return redirect('lista_editorial')
        else:
            return render(request, 'editorial/nuevo.html', {'form': form})
    else:
        form = EditorialForm()
        return render(request, 'editorial/nuevo.html', {'form': form})

def editarEditorial(request, id):
    editorial = get_object_or_404(Editorial, id=id)
    if request.method == "POST":
        form = EditorialForm(request.POST, instance=editorial)
        if form.is_valid():
            form.save()
            messages.success(request, "Editorial editada correctamente.")
            return redirect('lista_editorial')
        else:
            return render(request, 'editorial/editar.html', {'form': form, 'editorial': editorial})
    else:
        form = EditorialForm(instance=editorial)
        return render(request, 'editorial/editar.html', {'form': form, 'editorial': editorial})

def eliminarEditorial(request, id):
    editorial = get_object_or_404(Editorial, id=id)
    editorial.delete()
    messages.success(request, "Editorial eliminada correctamente.")
    return redirect('lista_editorial')
