from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
#how to display data on a template using pyhon and django
# Create your views here.

# Pagina de inicio
def iniciar(request):
    return render(request, '../templates/Verduleria/iniciar.html')

# Empezar venta
def addVenta(request):
    # Venta
    from datetime import datetime
    now = datetime.now()
    import datetime
    fecha = datetime.date(year=now.year, month=now.month, day=now.day)
    fecha_str = fecha.strftime("20%y-%m-%d")
    ventas = Venta.objects.all()
    detalle = f"Compra N°{len(ventas)}"
    venta = Venta(detalle=detalle, fecha=fecha_str)
    venta.save()

    return HttpResponseRedirect(reverse('home'))

# Pagina principal
def home(request):
    lista_productos = Producto.objects.all()
    carrito = []

    venta = Venta.objects.last()
    for i in Detalleproductoventa.objects.all():
        if i.id_venta == venta:
            carrito.append(i)

    return render(request, '../templates/Verduleria/index.html', {'lista_productos': lista_productos, 'carrito': carrito})

# Agregar productos al carrito
def carrito(request, nombre):
    # Detalle
    producto = Producto.objects.get(nombre=nombre)
    venta = Venta.objects.last()
    cantidad = request.POST['cantidad']
    detalle = Detalleproductoventa(id_producto=producto, cantidadproducto=cantidad, precioproducto=producto.precio, id_venta=venta)
    detalle.save()

    return HttpResponseRedirect(reverse('home'))

#Borrar un producto del carrito
def delete(request, id):
    producto = Detalleproductoventa.objects.get(id=id)
    producto.delete()
    return HttpResponseRedirect(reverse('home'))

# Pagina de explicacion de compra
def como_comprar(request):
    return render(request, '../templates/Verduleria/como-comprar.html')

# Pagina de finalizacion de compra
def compra(request):
    carrito = []
    precio_total = 0

    venta = Venta.objects.last()
    for i in Detalleproductoventa.objects.all():
        if i.id_venta == venta:
            carrito.append(i)
    
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

    venta = Venta(id_cliente=Cliente.objects.last())
    venta.save()

    return HttpResponseRedirect(reverse('inicio'))

# Funcion para iniciar usuario, bueno para verificar mejor dicho
def iniciar_sesion(request):
    email = request.POST['email']
    documento = request.POST['pswd']
    cliente = Cliente.objects.get(email=email)
    documentos = Documento.objects.get(numero=documento)

    venta = Venta.objects.last()
    venta.id_cliente = cliente
    venta.save()
    return HttpResponseRedirect(reverse('inicio'))