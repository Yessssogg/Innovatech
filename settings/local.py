from .base import *
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "django_prueba",
        "USER": "root",
        "PASSWORD": "Dff19263748",  # Deja la contraseña vacía si es lo que tienes configurado
        "HOST": "127.0.0.1",
        "PORT": "3306",  # O el puerto correspondiente de MySQL/MariaDB
    }
}