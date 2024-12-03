from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from carrito.models import Carrito
from django.contrib import messages
from productos.models import Producto,Brand
from carrito.form import FechaEventoForm
from datetime import timedelta


@login_required
def comprar(request, idProducto, idBrand):
    # Obtener el objeto de Brand y Producto de forma segura
    brand = get_object_or_404(Brand, id=idBrand)
    producto = get_object_or_404(Producto, id=idProducto)

    if request.method == "POST":
        # Crear el formulario con los datos del POST
        form = FechaEventoForm(request.POST)
        if form.is_valid():
            # Obtener la fecha del evento proporcionada por el usuario
            fecha_evento = form.cleaned_data['fecha_evento']

            # Verificar si la fecha proporcionada es anterior a la fecha y hora actual
            if fecha_evento < timezone.now():
                messages.error(request, "La fecha del evento no puede ser anterior a la fecha y hora actuales.")
                return redirect('comprar', idProducto=idProducto, idBrand=idBrand)  # Redirigir al mismo formulario

            # Definir el rango de tiempo para la verificación (3 horas antes y después de la fecha del evento)
            tres_horas_antes = fecha_evento - timedelta(hours=3)
            tres_horas_despues = fecha_evento + timedelta(hours=3)

            # Verificar si ya existe un carrito con el mismo usuario y dentro del rango de 3 horas
            existing_carrito = Carrito.objects.filter(
                user=request.user,
                event_date__gte=tres_horas_antes,
                event_date__lte=tres_horas_despues,
                complete=False
            ).exists()

            if existing_carrito:
                # Si existe un carrito dentro del rango de 3 horas, mostrar un mensaje de error
                messages.error(request, "Ya tienes un evento programado dentro de las próximas 3 horas. Elige otra fecha.")
                return redirect('comprar', idProducto=idProducto, idBrand=idBrand)  # Redirigir al mismo formulario

            # Crear el nuevo carrito asociado al usuario actual
            nuevo_carrito = Carrito(
                user=request.user,  # Asociamos el carrito con el usuario logueado
                brand=brand,
                producto=producto,
                event_date=fecha_evento,  # Fecha proporcionada por el usuario
                complete=False  # El carrito no está completo inicialmente
            )

            # Guardar el carrito en la base de datos
            nuevo_carrito.save()

            return redirect('/')

    else:
        # Si la solicitud es GET, mostramos el formulario para que el usuario elija la fecha
        form = FechaEventoForm()

    # Renderizamos el formulario en la vista
    return render(request, 'fecha.html', {'form': form, 'producto': producto, 'brand': brand})
