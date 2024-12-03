from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required,permission_required
from .models import Comment 
from .form import Comment_form
from productos.models import Producto

# Create your views here.
def index(request):
    #me trae todos los modelos
    productos=Producto.objects.all()
    return render(request,"list_products.html",{"products":productos})

def get_product(request,id):
    product=Producto.objects.get(id=id)
    #que me traiga todos los comentarios de un producto
    comments=Comment.objects.filter(product=id)
    #formulario de los comentarios
    formCo=Comment_form()
    return render(request,"show_product.html",{"product":product, "comments":comments,"formCo":formCo})

#este decorador, pregunta si el usuario esta logeado o existe
@login_required
@permission_required('productos.add_comment',raise_exception=True)
def add_new_comment(request, id):
    if request.method=="POST":
        #se crea un form que guardar el comentario
        form=Comment_form(data=request.POST)
        if form.is_valid():
            #informacion del usuario logeado
            user=request.user
            #info del producto
            producto=Producto.objects.get(id=id)

            #en False no lo guarda del todo, si no que le decimos que espere que le vamos a pasar mas datos
            new_comment=form.save(commit=False)

            new_comment.author=user
            new_comment.product=producto

            new_comment.save()
            return redirect("get_product",id)
    else: 
        return render(request, 'accounts/login.html',)
