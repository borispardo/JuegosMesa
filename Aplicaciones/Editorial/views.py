from django.shortcuts import render, redirect, get_object_or_404
from .models import Editorial
from django.contrib import messages

# Listar todas las editoriales
def listaEditorial(request):
    editoriales = Editorial.objects.all()
    return render(request, 'editorial/inicio.html', {'editoriales': editoriales})

# Mostrar formulario para crear nueva editorial
def nuevoEditorial(request):
    return render(request, 'editorial/nuevo.html')

# Guardar nueva editorial
def guardarEditorial(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        autor = request.POST.get("autor")
        fecha = request.POST.get("fecha")
        descripcion = request.POST.get("descripcion")

        Editorial.objects.create(
            titulo=titulo,
            autor=autor,
            fecha=fecha,
            descripcion=descripcion
        )

        messages.success(request, "Editorial GUARDADA correctamente.")
        return redirect('/')
    else:
        return redirect('/nuevo/')

# Mostrar formulario para editar una editorial
def editarEditorial(request, id):
    editorial = get_object_or_404(Editorial, id=id)
    return render(request, 'editorial/editar.html', {"editorial": editorial})

# Procesar la edición
def procesarEditorial(request, id):
    editorial = get_object_or_404(Editorial, id=id)

    if request.method == "POST":
        editorial.titulo = request.POST.get("titulo")
        editorial.autor = request.POST.get("autor")
        editorial.fecha = request.POST.get("fecha")
        editorial.descripcion = request.POST.get("descripcion")
        editorial.save()
        messages.success(request, "Editorial EDITADA correctamente.")
        return redirect('/')
    else:
        return redirect('/')

# Eliminar una editorial
def eliminarEditorial(request, id):
    editorial = get_object_or_404(Editorial, id=id)
    editorial.delete()
    messages.success(request, "Editorial ELIMINADA correctamente.")
    return redirect('/')
