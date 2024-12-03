#funcion que se mostrara
from productos.views import index,get_product,add_new_comment
from django.urls import path

urlpatterns = [
    path("", index,name='index'),
    #otra url, va a recibir un id, va a mostrar la funcion, y el nombre que me sirve para llamar a esta url desde
    #otras partes
    path("product/<int:id>",get_product,name="get_product"),
    path("product/<int:id>/add_comment",add_new_comment,name="new_comment")
]