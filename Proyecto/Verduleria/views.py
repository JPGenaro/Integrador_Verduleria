from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
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

def usuario(request):
    template = loader.get_template('../templates/Verduleria/usuario.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    tipo_documento = request.POST['tipo_documento']
    documento = request.POST['Documento']
    documento = Documento(tipo = tipo_documento, numero=documento)
    documento.save()

    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    direccion = request.POST['Direccion']
    email = request.POST['email']
    telefono = request.POST['Telefono']
    cuit = request.POST['cuit']
    usuario = Cliente(nombre=nombre, apellido=apellido, direccion=direccion, email=email, telefono=telefono, cuit=cuit) 
    usuario.save()

    return HttpResponseRedirect(reverse('compra'))

