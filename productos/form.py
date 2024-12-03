from django import forms
from .models import Comment

class Comment_form(forms.ModelForm):
    #informacion que se nesecita para construir el formulario
    class Meta:
        model=Comment
        fields=('text',)#es una tupla