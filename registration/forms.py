from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .models import Profile

# Extendemos el 'UserCreateForm'
class CreateUserWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido, máximo 254 caracteres y debe ser válido')

    class Meta:
        model = User
        # Esto se puede hacer de esta manera porque el campo 'email' existe en User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        # Obtengo el email que se intenta registrar
        email = self.cleaned_data.get('email')

        # Verifico si existe..
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError('El email ya existe.')

        # Si no entra en el if, lo enviamos..
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'bio': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder':'Bio'}),
            'link': forms.URLInput(attrs={'class':'form-control mt-3', 'placeholder':'Link'}),
        }