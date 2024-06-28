from django import forms
from .models import Post,Contacto



class BlogForms(forms.ModelForm):

    class Meta:
        model=Post
        fields='__all__'
        #fields=['imagen'] en caso de querer poner un campo especifico/s

class ContactoForms(forms.ModelForm):
    
    class Meta:
        model= Contacto
        fields='__all__'

