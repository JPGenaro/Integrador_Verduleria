from django.shortcuts import render
from .models import *

# Create your views here.
# Pagina principal
def home(request):
    return render(request, '../templates/Verduleria/index.html')#{'producto':dato})

# Pagina de finalizacion de compra
def compra(request):
    carrito = Detalleproductoventa.objects.all()
    precio_total = 0
    for i in carrito:
        precio_total += i.cantidadproducto * i.precioproducto
    return render(request, '../templates/Verduleria/compra.html', {'carrito':carrito, 'precio_total':precio_total})
