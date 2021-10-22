from django import forms
from django.forms import widgets

from .models import persona

class personaForm(forms.ModelForm):

    class Meta:

            model = persona

            fields = [
                'nombre',
                'documento'
            ]

            labels = {
                'nombre' : 'nombre',
                'documento' : 'documento'
    
    
            }
            widgets = {
            'nombre' : forms.TextInput(attrs={'class' : 'form-control','required' : ''}),
            'documento' : forms.TextInput(attrs={'class' : 'form-control','required' : ''})

            }