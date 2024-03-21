from django.shortcuts import render

# Create your views here.

def countries(request):
    return render(request, 'RuralPopulationApp/countries.html')

def income_groups(request):
    return render(request, 'RuralPopulationApp/income_groups.html')

def regions(request):
    return render(request, 'RuralPopulationApp/regions.html')