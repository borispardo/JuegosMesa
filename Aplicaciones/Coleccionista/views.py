from django.shortcuts import render, redirect, get_object_or_404
from .models import Coleccionista
from django.contrib import messages

# Listar todos los coleccionistas
def listaColeccionista(request):
    coleccionistas = Coleccionista.objects.all()
    return render(request, 'coleccionista/inicio.html', {'coleccionistas': coleccionistas})

# Mostrar formulario para crear nuevo coleccionista
def nuevoColeccionista(request):
    return render(request, 'coleccionista/nuevo.html')

# Guardar nuevo coleccionista
def guardarColeccionista(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        correo = request.POST.get("correo")
        fecha_registro = request.POST.get("fecha_registro")

        Coleccionista.objects.create(
            nombre=nombre,
            correo=correo,
            fecha_registro=fecha_registro
        )

        messages.success(request, "Coleccionista GUARDADO correctamente.")
        return redirect('/coleccionistas/')
    else:
        return redirect('/coleccionistas/nuevo/')

# Mostrar formulario para editar un coleccionista
def editarColeccionista(request, id):
    coleccionista = get_object_or_404(Coleccionista, id=id)
    return render(request, 'coleccionista/editar.html', {"coleccionista": coleccionista})

# Procesar la edición
def procesarColeccionista(request, id):
    coleccionista = get_object_or_404(Coleccionista, id=id)

    if request.method == "POST":
        coleccionista.nombre = request.POST.get("nombre")
        coleccionista.correo = request.POST.get("correo")
        coleccionista.fecha_registro = request.POST.get("fecha_registro")
        coleccionista.save()
        messages.success(request, "Coleccionista EDITADO correctamente.")
        return redirect('/coleccionistas/')
    else:
        return redirect('/coleccionistas/')

# Eliminar un coleccionista
def eliminarColeccionista(request, id):
    coleccionista = get_object_or_404(Coleccionista, id=id)
    coleccionista.delete()
    messages.success(request, "Coleccionista ELIMINADO correctamente.")
    return redirect('/coleccionistas/')
