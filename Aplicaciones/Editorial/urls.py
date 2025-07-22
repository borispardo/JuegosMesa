from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaEditorial, name='lista_editorial'),
    path('nuevo/', views.nuevoEditorial, name='nuevo_editorial'),           
    path('<int:id>/editar/', views.editarEditorial, name='editar_editorial'), 
    path('eliminar/<int:id>/', views.eliminarEditorial, name='eliminar_editorial'),
]
