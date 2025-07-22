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
        telefono = request.POST.get("telefono")
        direccion = request.POST.get("direccion")
        correo = request.POST.get("correo")
        fecha_registro = request.POST.get("fecha_registro")

        Coleccionista.objects.create(
            nombre=nombre,
            telefono=telefono,
            direccion=direccion,
            correo=correo,
            fecha_registro=fecha_registro
        )

        messages.success(request, "Coleccionista guardado correctamente.")
        return redirect('/coleccionista/')
    else:
        return redirect('/coleccionista/nuevo/')

# Mostrar formulario para editar un coleccionista
def editarColeccionista(request, id):
    coleccionista = get_object_or_404(Coleccionista, id=id)
    return render(request, 'coleccionista/editar.html', {"coleccionista": coleccionista})

# Procesar la edición
def procesarColeccionista(request, id):
    if request.method == "POST":
        coleccionista = get_object_or_404(Coleccionista, id=id)
        coleccionista.nombre = request.POST.get("nombre")
        coleccionista.telefono = request.POST.get("telefono")
        coleccionista.direccion = request.POST.get("direccion")
        coleccionista.correo = request.POST.get("correo")
        coleccionista.fecha_registro = request.POST.get("fecha_registro")
        coleccionista.save()
        messages.success(request, "Coleccionista editado correctamente.")
        return redirect('/coleccionista/')
    else:
        return redirect('/coleccionista/')

# Eliminar un coleccionista
def eliminarColeccionista(request, id):
    coleccionista = get_object_or_404(Coleccionista, id=id)
    coleccionista.delete()
    messages.success(request, "Coleccionista eliminado correctamente.")
    return redirect('/coleccionista/')
