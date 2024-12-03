from .base import *
#se va a importar todo, pero el unico cambia va a ser el cambio de debug
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#SE CAMBIA POR LA BASE DE DATOS EN LA NUBE
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "django_prueba",
        "USER": "root",
        "PASSWORD": "Dff19263748",  # Deja la contraseña vacía si es lo que tienes configurado
        "HOST": "localhost",
        "PORT": "3306",  # O el puerto correspondiente de MySQL/MariaDB
    }
}