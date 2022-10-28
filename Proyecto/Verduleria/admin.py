from tkinter.tix import Form
from django.contrib import admin
from .models import Cliente, Venta, Tipoproducto, Documento, Formapago, Producto, Detalleproductoventa
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(Tipoproducto)
admin.site.register(Documento)
admin.site.register(Formapago)
admin.site.register(Producto)
admin.site.register(Detalleproductoventa)