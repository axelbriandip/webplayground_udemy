from django.urls import path
from .views import PageListViews, PageDetailViews
from . import views

urlpatterns = [
    path('', PageListViews.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetailViews.as_view(), name='page'),
]