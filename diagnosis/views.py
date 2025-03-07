from django.shortcuts import render
from .models import PlantDisease
from django.db.models import Q


def disease_search(request):
    query = request.GET.get('symptoms', '')
    diseases = PlantDisease.objects.filter(
        Q(symptoms__icontains=query) |
        Q(name__icontains=query)
    ) if query else None
    return render(request, 'diagnosis/search.html', {'diseases': diseases, 'query': query})


def index(request):
    return render(request, 'diagnosis/index.html')
