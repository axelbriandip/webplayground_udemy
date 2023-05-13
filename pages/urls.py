from django.urls import path
from .views import PageListViews, PageDetailViews, PageCreate

pages_patterns = ([
    path('', PageListViews.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetailViews.as_view(), name='page'),
    path('create/', PageCreate.as_view(), name='create')
], 'pages')