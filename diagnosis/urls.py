from django.urls import path
from .views import disease_search

urlpatterns = [
    path('search/', disease_search, name='disease_search'),
]
