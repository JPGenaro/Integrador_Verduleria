from django.shortcuts import render
from .models import *
#how to display data on a template using pyhon and django
# Create your views here.
def home(request):
    dato = Producto.objects.all().filter(id_tipoproducto = 1)[2]
    return render(request, '../templates/Verduleria/index.html')#{'producto':dato})