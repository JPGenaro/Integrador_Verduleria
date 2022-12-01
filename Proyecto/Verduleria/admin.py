from tkinter.tix import Form
from django.contrib import admin
from .models import Cliente, Venta, Tipoproducto, Documento, Formapago, Producto, Detalleproductoventa

#Admin site personalization
admin.site.site_header="Verdulería Fénix"
admin.site.index_title="Verdulería Fénix"


# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "telefono","email")
    list_filter = ["apellido"]
    search_fields = ["nombre","apellido","telefono","email"]

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ("id","detalle","fecha","id_cliente")
    list_filter = ["fecha"]

@admin.register(Tipoproducto)
class TipoProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre","descripcion")
    list_filter = ["nombre"]
    search_fields = ["nombre","descripcion"]

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ("tipo","numero")
    list_filter = ["numero"]
    search_fields = ["tipo","numero"]

@admin.register(Formapago)
class FormapagoAdmin(admin.ModelAdmin):
    list_display = ("nombre","descripcion")
    list_filter = ["nombre"]
    search_fields = ["nombre","descripcion"]

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre","id_tipoproducto","precio","stock")
    list_filter = ["nombre"]
    search_fields = ["nombre"]

@admin.register(Detalleproductoventa)
class DetalleproductoventaAdmin(admin.ModelAdmin):
    list_display = ("id","id_producto","precioproducto","cantidadproducto","id_venta")
    list_filter = ["id"]