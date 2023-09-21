from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

# Extendemos el 'UserCreateForm'
class CreateUserWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido, máximo 254 caracteres y debe ser válido')

    class Meta:
        model = User
        # Esto se puede hacer de esta manera porque el campo 'email' existe en User
        fields = ('username', 'email', 'password1', 'password2')
