from .models import evento, contacto
from django import forms

class contactoForm(forms.ModelForm):
    class Meta:
        model = contacto
        fields = ['nombre_persona', 'correo', 'mensaje', 'tipo']
        widgets = {
            'nombre_persona': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control mt-2'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control mt-2', 'rows': 4}),
            'tipo': forms.Select(attrs={'class': 'btn btn-secondary dropdown-toggle'}),
        }
        labels = {
            'nombre_persona': 'Nombre',
            'correo': 'Correo Electrónico',
            'mensaje': 'Mensaje',
        }