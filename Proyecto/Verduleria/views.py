from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
import datetime
#how to display data on a template using pyhon and django
# Create your views here.

# Pagina principal
def home(request):
    lista_productos = Producto.objects.all()
    carrito = Detalleproductoventa.objects.all()
    return render(request, '../templates/Verduleria/index.html', {'lista_productos': lista_productos, 'carrito': carrito})

# Agregar productos al carrito
def carrito(request):
    # Venta
    ventas = Venta.objects.all()
    cant = len(ventas)
    detalle = f"Compra{cant}"
    venta = Venta(detalle=detalle, fecha='2022-12-15')
    venta.save()

    # Detalle
    nombre = request.POST.get('producto')
    precio = request.POST.get('precio')
    cantidad = request.POST('cantidad')
    producto = Producto.objects.filter(nombre=nombre)
    venta_last = Venta.objects.last()
    detalle = Detalleproductoventa(precio=precio, cantidad=cantidad)
    detalle.save()

    return HttpResponseRedirect(reverse('home'))

# Pagina de explicacion de compra
def como_comprar(request):
    return render(request, '../templates/Verduleria/como-comprar.html')

# Pagina de finalizacion de compra
def compra(request):
    carrito = Detalleproductoventa.objects.all()
    precio_total = 0
    for i in carrito:
        precio_total += i.cantidadproducto * i.precioproducto
    return render(request, '../templates/Verduleria/compra.html', {'carrito':carrito, 'precio_total':precio_total})

# Pagina de usuario
def usuario(request):
    template = loader.get_template('../templates/Verduleria/usuario.html')
    return HttpResponse(template.render({}, request))

# Funcion para registrar usuarios
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
    usuario = Cliente(nombre=nombre, apellido=apellido, direccion=direccion, email=email, telefono=telefono, cuit=cuit, id_documento=Documento.objects.last()) 
    usuario.save()

    return HttpResponseRedirect(reverse('compra'))

# Funcion para iniciar usuario, bueno para verificar mejor dicho
def iniciar_sesion(request):
    email = request.POST['email']
    documento = request.POST['pswd']
    clientes = Cliente.objects.values_list("email","id_documento").filter(email=email)
    documentos = Documento.objects.values_list("id", "numero").filter(numero=documento)
    if len(clientes) == 1 and len(documentos) == 1:
        return HttpResponseRedirect(reverse('compra'))
    if len(clientes) == 0 and len(documentos) == 0:
        #Usuario no existente, por favor registrese
        return None