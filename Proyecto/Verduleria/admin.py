from tkinter.tix import Form
from django.contrib import admin
from .models import Cliente, Venta, Tipoproducto, Documento, Formapago, Producto, Detalleproductoventa
# Register your models here.

admin.site.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("telefono","mail")
    list_filter = ("apellido")
admin.site.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ("id", "fecha", "id_formapago.nombre")
    list_filter = ("id")
admin.site.register(Tipoproducto)
class TipoProductoAdmin(admin.ModelAdmin):
    list_display = ("descripcion")
    list_filter = ("nombre")
admin.site.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ("tipo")
    list_filter = ("numero")
admin.site.register(Formapago)
class FormapagoAdmin(admin.ModelAdmin):
    list_display = ("descripcion")
    list_filter = ("nombre")
admin.site.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("stock","id_tipoproducto.nombre")
    list_filter = ("apellido")
admin.site.register(Detalleproductoventa)
class DetalleproductoventaAdmin(admin.ModelAdmin):
    list_display = ("id", "precioproducto", "cantidadproducto")
    list_filter = ("id")