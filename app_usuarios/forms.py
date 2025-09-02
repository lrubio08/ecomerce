from django import forms
from .models import Usuarios
import re

class UsuariosForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-input', 'placeholder': 'Ingrese contraseña'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-input', 'placeholder': 'Repita contraseña'
    }))

    class Meta:
        model = Usuarios
        fields = [
            'first_name', 'last_name', 'email', 'username',
            'telefono', 'direccion', 'rut', 'comuna', 'ciudad',
            'fecha_nacimiento', 'genero'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control form-input', 'placeholder': 'Ingrese su nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-input', 'placeholder': 'Ingrese su apellido'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-input', 'placeholder': 'ejemplo@ejemplo.com'}),
            'username': forms.TextInput(attrs={'class': 'form-control form-input', 'placeholder': 'Ingrese su usuario'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control form-input', 'placeholder': 'Ingrese su teléfono'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control form-input', 'placeholder': 'Ingrese su dirección'}),
            'rut': forms.TextInput(attrs={'class': 'form-control form-input', 'placeholder': 'Ingrese su RUT'}),
            'comuna': forms.TextInput(attrs={'class': 'form-control form-input', 'placeholder': 'Ingrese su comuna'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control form-input', 'placeholder': 'Ingrese su ciudad'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control form-input', 'type': 'date'}),
            'genero': forms.Select(attrs={'class': 'form-control form-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Excluye campos innecesarios en la edición
        if 'instance' in kwargs:
            self.fields.pop('password1', None)
            self.fields.pop('password2', None)
            self.fields.pop('username', None)

def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 8 or not any(c.isdigit() for c in password1) or not any(c.isupper() for c in password1) or not re.search(r'[!@#$%^&*(),.?":{}|<>]', password1):
            raise forms.ValidationError("¡La contraseña debe cumplir con los requerimientos!")
        return password1

class RecuperarPasswordForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico')