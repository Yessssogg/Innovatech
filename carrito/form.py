from django import forms
class FechaEventoForm(forms.Form):
    fecha_evento = forms.DateTimeField(
        label="Fecha del evento", 
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )