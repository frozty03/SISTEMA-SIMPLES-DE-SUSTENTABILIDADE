from django import forms
from .models import UsuarioSustentavel

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = UsuarioSustentavel
        fields = ['nome', 'consumo_energia', 'consumo_agua', 'residuos', 'uso_transporte']
