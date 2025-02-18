from django.urls import path
from .views import disease_search, index

urlpatterns = [
    path('', index, name='home'),
    path('search/', disease_search, name='disease_search'),
]
