from django.shortcuts import render
from .models import PlantDisease
from django.db.models import Q
from django.core.paginator import Paginator


def disease_search(request):
    query = request.GET.get('symptoms', '')
    diseases = PlantDisease.objects.filter(
        Q(symptoms__icontains=query) |
        Q(name__icontains=query)
    ) if query else None

    #Pagination
    paginator=Paginator(diseases, 5) #Show 5 results per page
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    return render(request, 'diagnosis/search.html', {'page_obj': page_obj, 'query': query})


def index(request):
    return render(request, 'diagnosis/index.html')
