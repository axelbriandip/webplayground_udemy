from django.urls import path
from .views import SignUpView

registration_patterns = ([
    path('signup/', SignUpView.as_view(), name='signup'),
], 'registration')