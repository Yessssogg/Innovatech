from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Ruta de donde nos va a buscar las urls
    path("",include("productos.urlsProducts")),
    path("",include("carrito.urlsCarrito")),
    path("accounts/",include("accounts.urlsAccount")),
    path("admin/", admin.site.urls),
    #Comando especifico, para permitir las imagenes
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
