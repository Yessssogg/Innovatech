from django.contrib import admin
from productos.models import Producto,Brand,Comment

"""
Para poder registrar productos en el panel de admin, podemos
agregar lo siguiente

"""
admin.site.register(Producto)
admin.site.register(Brand)
admin.site.register(Comment)