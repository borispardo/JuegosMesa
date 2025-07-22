from django.urls import path
from . import views

urlpatterns = [
    path('coleccionistas/', views.listaColeccionista, name='lista_coleccionista'),
    path('coleccionistas/nuevo/', views.nuevoColeccionista, name='nuevo_coleccionista'),
    path('coleccionistas/guardar/', views.guardarColeccionista, name='guardar_coleccionista'),
    path('coleccionistas/<int:id>/editar/', views.editarColeccionista, name='editar_coleccionista'),
    path('coleccionistas/<int:id>/actualizar/', views.procesarColeccionista, name='procesar_coleccionista'),
    path('coleccionistas/eliminar/<int:id>/', views.eliminarColeccionista, name='eliminar_coleccionista'),
]
