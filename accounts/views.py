from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout
from carrito.models import Carrito
from django.contrib.auth.models import Permission
# Create your views here.
def login_view(request):
    if request.method=="POST":
        #Se logeara el usuario
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            #se logea
            login(request,user)
            #despues que se logeo
            return redirect("index")
    else:
        form=AuthenticationForm()
    return render(request, 'accounts/login.html',{'form':form})

def log_out(request):
    if request.method=="POST":
        logout(request)
        return redirect("index")
    


def signup(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #crea un nuevo usuario
            user=form.save()
            #creamos los permisos para que pueda leer los comentarios
            permission = Permission.objects.get(codename='view_comment') 
            #creamos el permiso para añadir comentarios
            #parar modificar seria change
            permission2 = Permission.objects.get(codename='add_comment') 
            #añadimos los permisos
            user.user_permissions.add(permission,permission2)
            #se logea
            login(request,user)
            #despues que se logeo
            return redirect("index")
    else:
        form = UserCreationForm(request.POST)
    return render(request,'accounts/signup.html',{'form':form})

def perfil(request):
    if request.method=='GET':
        # Obtener todos los carritos asociados al usuario autenticado
        carritos = Carrito.objects.filter(user=request.user)

        # Puedes obtener detalles de los productos si lo necesitas
        productos_comprados = [carrito.producto for carrito in carritos]

        # Pasar los productos comprados a la plantilla
        return render(request, 'accounts/perfil.html', {
            'carritos': carritos,  # Los carritos completos
            'productos_comprados': productos_comprados  # Los productos comprados
        })