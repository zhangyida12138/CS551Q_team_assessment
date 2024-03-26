from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Prefetch
from urllib.parse import quote
from django.core.exceptions import FieldError
from .models import Country,DataEntry,Region,IncomeGroup,RegionCountries,IncomeCountries

# Create your views here.
def countries(request):
    # Prefetch the DataEntry objects for each country to minimize database hits
    dataentry_prefetch = Prefetch('dataentry_set', queryset=DataEntry.objects.all())

    countries = Country.objects.select_related('region', 'income_group').all()
    regions=Region.objects.all()
    income_groups=IncomeGroup.objects.all()
    # Merge the three dictionaries into one
    context = {
        'countries': countries,
        'regions': regions,
        "income_groups": income_groups
    }
    return render(request, 'RuralPopulationApp/countries.html', context)


def compare_countries(request):
    countries = Country.objects.all()
 
    country_1 = None
    country_2 = None

    # Check if the request method is GET
    if request.method == 'GET':
        # Retrieve the country codes from the query parameters
        country_code_1 = request.GET.get('country_code_1')
        country_code_2 = request.GET.get('country_code_2')
        
        # If both country codes are provided, fetch the corresponding country objects
        if country_code_1 and country_code_2:
            country_1 = get_object_or_404(Country, country_code=country_code_1)
            country_2 = get_object_or_404(Country, country_code=country_code_2)


    context = {
        'countries': countries,
        'country_1': country_1,
        'country_2': country_2,
    }

    # Render the form and comparison data
    return render(request, 'RuralPopulationApp/compare_countries.html' ,context)

def compare_countries_in_region(request):
    region = None
    countries = None
    error_message = None

    if request.method == 'GET':
        region_id = request.GET.get('region_id')
        if region_id:
            if not region_id.isdigit():
                error_message = "Please enter a number!"
            else:
                try:
                    region = get_object_or_404(Region, id=region_id)
                    country_ids = RegionCountries.objects.filter(region=region).values_list('country_id', flat=True)
                    countries = Country.objects.filter(id__in=country_ids)
                except Exception as e:
                    print(e)
                    error_message ='No Region matches the given query.'
    
    return render(request, 'RuralPopulationApp/compare_countries_in_region.html', {'region': region, 'countries': countries,'error_message':error_message})

def compare_countries_in_income_group(request):
    income_group_id = None
    income_group = None
    countries = None
    error_message = None

    if request.method == 'GET':
        income_group_id = request.GET.get('income_group_id')

        if income_group_id:
            if not income_group_id.isdigit():
                error_message='Please enter a number!'
            else:
                try:
                    income_group = get_object_or_404(IncomeGroup, id=income_group_id)
                    country_ids = IncomeCountries.objects.filter(income_group=income_group).values_list('country_id', flat=True)
                    countries = Country.objects.filter(id__in=country_ids)
                except Exception as e :
                    error_message='No IncomeGroup matches the given query.'

    return render(request, 'RuralPopulationApp/compare_countries_in_income_group.html', {'income_group': income_group, 'countries': countries,'error_message':error_message})

def show(request):
    country_1 = None

    # Check if the request method is GET
    if request.method == 'GET':
        # Retrieve the country codes from the query parameters
        country_code_1 = request.GET.get('country_code_1')
        
        # If both country codes are provided, fetch the corresponding country objects
        if country_code_1:
            country_1 = get_object_or_404(Country, country_code=country_code_1)

    # Render the form and comparison data
    return render(request, 'RuralPopulationApp/show.html', {'country_1': country_1})