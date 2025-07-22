from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaJuego, name='lista_juego'),
    path('nuevo/', views.nuevoJuego, name='nuevo_juego'),
    path('guardar/', views.guardarJuego, name='guardar_juego'),
    path('<int:id>/editar/', views.editarJuego, name='editar_juego'),
    path('<int:id>/actualizar/', views.procesarJuego, name='procesar_juego'),
    path('eliminar/<int:id>/', views.eliminarJuego, name='eliminar_juego'),
]
