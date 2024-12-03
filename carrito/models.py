from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#Modelo de la base de datos

class Carrito(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Asociar al usuario
    #Referenciando Tablas
    brand=models.ForeignKey(
        "productos.Brand",
        on_delete=models.CASCADE,
        related_name="fk_animador"
    )
    #Referenciando Tablas
    producto=models.ForeignKey(
        "productos.Producto",
        on_delete=models.CASCADE,
        related_name="fk_evento"
    )
    created_date=models.DateTimeField(default=timezone.now)
    event_date=models.DateTimeField(blank=True,null=True)
    complete=models.BooleanField(default=False)
    def __str__(self) -> str:
        return f"Pedido de evento, animado por {self.brand}"
    