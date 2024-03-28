from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Prefetch
from urllib.parse import quote
from django.core.exceptions import FieldError
from .models import Country, DataEntry, Region, IncomeGroup, RegionCountries, IncomeCountries
from django.shortcuts import render, get_object_or_404


# Create your views here.
def countries(request):
    # Prefetch the DataEntry objects for each country to minimize database hits
    dataentry_prefetch = Prefetch('dataentry_set', queryset=DataEntry.objects.all())

    countries = Country.objects.select_related('region', 'income_group').all()
    regions = Region.objects.all()
    income_groups = IncomeGroup.objects.all()

    # Merge the three dictionaries into one
    context = {
        'countries': countries,
        'regions': regions,
        "income_groups": income_groups,
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
        # check if they are the same countries
        # If both country codes are provided, fetch the corresponding country objects
        if country_code_1 and country_code_2:
            country_1 = get_object_or_404(Country, country_code=country_code_1)
            country_2 = get_object_or_404(Country, country_code=country_code_2)

        context = {
            'countries': countries,
            'country_1': country_1,
            'country_2': country_2,
            'selected_country_code_1': country_code_1,
            'selected_country_code_2': country_code_2
        }

        # Render the form and comparison data
        return render(request, 'RuralPopulationApp/compare_countries.html', context)


def compare_countries_in_region(request):
    regions = Region.objects.all()
    region = None
    countries = None
    return render(request, 'RuralPopulationApp/compare_countries_in_region.html',
                  {'regions': regions, 'region': region, 'countries': countries})


def countries_in_region(request):
    regions = Region.objects.all()
    countries = None
    if request.method == 'GET':
        region_id = request.GET.get('region_id')
        region = get_object_or_404(Region, id=region_id)
        country_ids = RegionCountries.objects.filter(region=region).values_list('country_id', flat=True)
        countries = Country.objects.filter(id__in=country_ids)

    return render(request, 'RuralPopulationApp/compare_countries_in_region.html',
                      {'regions': regions, 'region': region,  'countries': countries, 'selected_region_id': int(region_id)})


def countries_in_income_group(request):
    income_groups = IncomeGroup.objects.all()
    if request.method == 'GET':
        income_group_id = request.GET.get('income_group_id')
        if income_group_id == '0':
            countries = Country.objects.all()
        else:
            income_group = get_object_or_404(IncomeGroup, id=income_group_id)
            country_ids = IncomeCountries.objects.filter(income_group=income_group).values_list('country_id',
                                                                                                flat=True)
            countries = Country.objects.filter(id__in=country_ids)

    return render(request, 'RuralPopulationApp/countries.html',
                  {'countries': countries, 'income_groups': income_groups,
                   'selected_income_group_id': int(income_group_id)})


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


def about(request):
    context = {
        'content': 'nothing'
    }
    return render(request, 'RuralPopulationApp/about.html', context)
