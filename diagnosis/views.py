from django.shortcuts import render
from .models import PlantDisease


def disease_search(request):
    query = request.GET.get('symptom', '')
    diseases = PlantDisease.objects.filter(
        symptoms_icontains=query) if query else None
    return render(request, 'diagnosis/search.html', {'diseases': diseases, 'query': query})


def index(request):
    return render(request, 'diagnosis/index.html')
