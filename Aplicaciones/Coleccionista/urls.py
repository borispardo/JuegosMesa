from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaColeccionista, name='lista_coleccionista'),
    path('nuevo/', views.nuevoColeccionista, name='nuevo_coleccionista'),
    path('guardar/', views.guardarColeccionista, name='guardar_coleccionista'),
    path('<int:id>/editar/', views.editarColeccionista, name='editar_coleccionista'),
    path('<int:id>/actualizar/', views.procesarColeccionista, name='procesar_coleccionista'),
    path('eliminar/<int:id>/', views.eliminarColeccionista, name='eliminar_coleccionista'),
]
