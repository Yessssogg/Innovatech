#funcion que se mostrara
from accounts.views import login_view,log_out,signup,perfil
from django.urls import path

urlpatterns = [
    path("login", login_view,name='login'),
    path("logout", log_out,name='logout'),
    path("signup", signup,name='signup'),
    path("perfil", perfil,name='perfil'),
]