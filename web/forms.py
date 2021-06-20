from django import forms


class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    precio = forms.CharField(max_length=100)
    stock = forms.CharField(max_length=100)
