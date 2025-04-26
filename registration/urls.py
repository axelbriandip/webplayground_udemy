from django.urls import path
from .views import SignUpView, ProfileUpdateView, UserUpdateEmailView

registration_patterns = ([
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('profile/email/update', UserUpdateEmailView.as_view(), name='profile_email_update'),
], 'registration')