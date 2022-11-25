from django.shortcuts import render
from .models import *

# Create your views here.
# Pagina principal
def home(request):
    dato = Producto.objects.all().filter(id_tipoproducto = 1)[2]
    return render(request, '../templates/Verduleria/index.html')#{'producto':dato})

# Pagina de finalizacion de compra
def compra(request):
    return render(request, '../templates/Verduleria/compra.html')
