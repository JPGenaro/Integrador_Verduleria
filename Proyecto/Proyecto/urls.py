"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from Verduleria.views import iniciar, addVenta, home, compra, usuario, addrecord, como_comprar, iniciar_sesion, carrito, delete

urlpatterns = [
    path('admin/', admin.site.urls),
    # Inicio
    path('', iniciar, name='inicio'),
    path('addVenta/', addVenta, name='addVenta'),
    # Tienda
    path('home/', home, name='home'),
    path('home/delete/<int:id>', delete, name='delete'),
    path('home/carrito/<str:nombre>', carrito, name='carrito'),
    # Tutorial
    path('home/como-comprar', como_comprar, name='como_comprar'),
    # Lista de la compra
    path('home/compra/', compra, name='compra'),
    # Usuario
    path('home/compra/usuario/', usuario, name='usuario'),
    path('home/compra/usuario/addrecord/', addrecord, name='addrecord'),
    path('home/compra/usuario/iniciar_sesion/', iniciar_sesion, name='iniciar_sesion'),
]
