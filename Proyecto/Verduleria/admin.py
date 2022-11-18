from tkinter.tix import Form
from django.contrib import admin
from .models import Cliente, Venta, Tipoproducto, Documento, Formapago, Producto, Detalleproductoventa
# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (Cliente.__str__, "telefono","email")
    list_filter = ["apellido"]
    search_fields = ["nombre","apellido","email","telefono"]
admin.site.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = (Venta.__str__, "id", "fecha", "id_formapago.nombre")
    list_filter = ["fecha"]
admin.site.register(Tipoproducto)
class TipoProductoAdmin(admin.ModelAdmin):
    list_display = (Tipoproducto.__str__, "descripcion")
    list_filter = ["nombre"]
    search_fields = ["nombre", "descripcion"]
admin.site.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = (Documento.__str__, "tipo")
    list_filter = ["numero"]
    search_fields = ["tipo", "numero"]
admin.site.register(Formapago)
class FormapagoAdmin(admin.ModelAdmin):
    list_display = (Formapago.__str__, "descripcion")
    list_filter = ["nombre"]
    search_fields = ["nombre", "descripcion"]
admin.site.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (Producto.__str__, "stock","id_tipoproducto.nombre")
    list_filter = ["apellido"]
    search_fields = ["nombre"]
admin.site.register(Detalleproductoventa)
class DetalleproductoventaAdmin(admin.ModelAdmin):
    list_display = (Detalleproductoventa.__str__, "id", "precioproducto", "cantidadproducto")
    list_filter = ["id"]