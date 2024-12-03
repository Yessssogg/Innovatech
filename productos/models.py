from django.db import models
from django.utils import timezone
#Modelo de la base de datos

class Producto(models.Model):
    name=models.CharField(max_length=50)
    price=models.DecimalField(decimal_places=2,max_digits=10)
    sku=models.CharField(max_length=10)
    category=models.CharField(max_length=20)
    #Referenciando Tablas
    brand=models.ForeignKey(
        "productos.Brand",
        on_delete=models.CASCADE,
        related_name="fk_brand"
    )
    #puede ser vacio y nulo, donde se va a guardar las imagenes
    image=models.ImageField(blank=True,null=True,upload_to="media/productos")
    discount=models.IntegerField(blank=True,null=True)
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True,null=True)
    last_update=models.DateTimeField(blank=True,null=True)
    #como se mostrara el objeto, cuando lo mostremos
    def __str__(self) -> str:
        return f"{self.name}, marca=>{self.brand} , codigo=> {self.sku}"
    

class Brand(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(null=True,blank=True)
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True,null=True)
    last_update=models.DateTimeField(blank=True,null=True)
    logo=models.ImageField(blank=True,null=True,upload_to="media/productos")
    def __str__(self) -> str:
        return f"{self.name}"


class Comment(models.Model):
    #un producto puede tener muchos comentarios
    product=models.ForeignKey(
        #haciendo referencia al archivo y al nombre de la clase
        'productos.Producto',
        on_delete=models.CASCADE,
        related_name='fk_producto'
    )
    author=models.CharField(max_length=200)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    approved_comment=models.BooleanField(default=False)
    def approve(self):
        #Que lo ponga en true y lo guarde
        self.approved_comment=True
        self.save()
    def __str__(self) -> str:
        return self.text