from django.urls import path
from .views import SignUpView, ProfileUpdateView

registration_patterns = ([
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
], 'registration')