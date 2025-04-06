from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Introduce una dirección de correo electrónico válida (máximo 254 caracteres).")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email') # recuperamos el email que se envió por formulario
        if User.objects.filter(email=email).exists(): # verificamos si existe
            raise forms.ValidationError("Ya existe un usuario con este correo electrónico.") # si existe, lanzamos un error
        return email # si no existe, lo devolvemos para que se guarde en la base de datos