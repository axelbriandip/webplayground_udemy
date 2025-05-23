from .forms import UserCreationFormWithEmail, UserUpdateEmailForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django import forms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Profile
from .forms import ProfileUpdateForm

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'
    
    def get_form(self, form_class = None):
        form = super(SignUpView, self).get_form()
        # modificar en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder': 'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder': 'Correo electrónico'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder': 'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder': 'Repetir contraseña'})

        form.fields['username'].label = ''
        form.fields['email'].label = ''
        form.fields['password1'].label = ''
        form.fields['password2'].label = ''
        return form

@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(UpdateView):
    form_class = ProfileUpdateForm
    success_url = reverse_lazy('registration:profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        # recuperar el objeto a editar
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

@method_decorator(login_required, name='dispatch')
class UserUpdateEmailView(UpdateView):
    form_class = UserUpdateEmailForm
    success_url = reverse_lazy('registration:profile')
    template_name = 'registration/profile_email_form.html'

    def get_object(self):
        # recuperar el objeto a editar
        return self.request.user

    def get_form(self, form_class=None):
        form = super(UserUpdateEmailView, self).get_form()
        # modificar en tiempo real
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder': 'Correo electrónico'})
        form.fields['email'].label = ''
        return form