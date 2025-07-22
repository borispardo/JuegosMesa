"""
URL configuration for JuegosMesa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from Aplicaciones.Juego.views import inicio

urlpatterns = [
    path('', inicio, name='inicio'),
    path('inicio/', inicio, name='inicio_directo'),
    path('admin/', admin.site.urls),
    path('editorial/', include('Aplicaciones.Editorial.urls')),
    path('coleccionista/', include('Aplicaciones.Coleccionista.urls')),
    path('juego/', include('Aplicaciones.Juego.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

