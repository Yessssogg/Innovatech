#funcion que se mostrara
from carrito.views import comprar
from django.urls import path

urlpatterns = [
    #otra url, va a recibir un id, va a mostrar la funcion, y el nombre que me sirve para llamar a esta url desde
    #otras partes
    path("comprar/<int:idProducto>/<int:idBrand>",comprar,name="comprar"),
]