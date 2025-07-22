from django.shortcuts import render, redirect, get_object_or_404
from .models import Juego
from Aplicaciones.Coleccionista.models import Coleccionista
from Aplicaciones.Editorial.models import Editorial
from django.contrib import messages

# Listar Juegos
def listaJuego(request):
    juegos = Juego.objects.all()
    return render(request, 'juego/inicio.html', {'juegos': juegos})

# Formulario nuevo juego
def nuevoJuego(request):
    coleccionistas = Coleccionista.objects.all()
    editoriales = Editorial.objects.all()
    return render(request, 'juego/nuevo.html', {
        'coleccionistas': coleccionistas,
        'editoriales': editoriales
    })

# Guardar juego
def guardarJuego(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        genero = request.POST.get("genero")
        anio = request.POST.get("anio_lanzamiento")
        coleccionista_id = request.POST.get("coleccionista")
        editorial_id = request.POST.get("editorial")

        Juego.objects.create(
            titulo=titulo,
            genero=genero,
            anio_lanzamiento=anio,
            coleccionista_id=coleccionista_id,
            editorial_id=editorial_id
        )

        messages.success(request, "Juego GUARDADO correctamente.")
        return redirect('/juego/')
    else:
        return redirect('/nuevo/')

# Formulario editar juego
def editarJuego(request, id):
    juego = get_object_or_404(Juego, id=id)
    coleccionistas = Coleccionista.objects.all()
    editoriales = Editorial.objects.all()
    return render(request, 'juego/editar.html', {
        'juego': juego,
        'coleccionistas': coleccionistas,
        'editoriales': editoriales
    })

# Procesar edición
def procesarJuego(request, id):
    juego = get_object_or_404(Juego, id=id)

    if request.method == "POST":
        juego.titulo = request.POST.get("titulo")
        juego.genero = request.POST.get("genero")
        juego.anio_lanzamiento = request.POST.get("anio_lanzamiento")
        juego.coleccionista_id = request.POST.get("coleccionista")
        juego.editorial_id = request.POST.get("editorial")
        juego.save()

        messages.success(request, "Juego EDITADO correctamente.")
        return redirect('/juego/')
    else:
        return redirect('/juego/')

# Eliminar juego
def eliminarJuego(request, id):
    juego = get_object_or_404(Juego, id=id)
    juego.delete()
    messages.success(request, "Juego ELIMINADO correctamente.")
    return redirect('/juego/')
