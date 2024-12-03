from django.contrib import admin
from carrito.models import Carrito

"""
Para poder registrar productos en el panel de admin, podemos
agregar lo siguiente

"""
admin.site.register(Carrito)