from django import forms

class BlogFormulario(forms.Form):
    titulo = forms.CharField(max_length=40)
    subtitulo = forms.CharField(max_length=40)
    cuerpo = forms.CharField(max_length=100)
    autor = forms.CharField(max_length=40)
    fecha = forms.CharField(max_length=40)
    imagen = forms.CharField(max_length=40)