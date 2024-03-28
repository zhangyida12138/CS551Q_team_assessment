from django.http import HttpResponseRedirect,Http404
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
    error_message = None  # Add a variable for the error message

    if request.method == 'GET':
        region_id = request.GET.get('region_id')
        try:
            # Attempt to convert region_id to an integer and retrieve the corresponding Region object
            region_id_int = int(region_id)  # This might raise a ValueError
            region = get_object_or_404(Region, id=region_id_int)  # This might raise a Http404
            country_ids = RegionCountries.objects.filter(region=region).values_list('country_id', flat=True)
            countries = Country.objects.filter(id__in=country_ids)
        except ValueError:
            # If region_id is not an integer
            error_message = "Region ID must be a number."
        except Http404:
            # If the corresponding Region is not found
            error_message = "Region not found."

    return render(request, 'RuralPopulationApp/compare_countries_in_region.html', {
        'regions': regions,
        'region': locals().get('region', None),  # Use 'region' if it's in locals(), else None
        'countries': countries,
        'selected_region_id': region_id if 'region_id_int' in locals() else None,
        'error_message': error_message,  # Pass the error message to the template
    })
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
    error_message = None  # Define a variable to store any potential error messages

    if request.method == 'GET':
        country_code_1 = request.GET.get('country_code_1')

        try:
            if country_code_1:
                # Attempt to retrieve the country object using the provided country code
                country_1 = get_object_or_404(Country, country_code=country_code_1)
        except Http404:
            # Handle the Http404 exception if no corresponding country can be found
            error_message = "The requested country could not be found."
        except Exception as e:
            # Handle any other exceptions that may occur
            error_message = f"An error occurred: {str(e)}"

    context = {
        'country_1': country_1,
        'error_message': error_message,  # Pass the error message to the template
    }

    return render(request, 'RuralPopulationApp/show.html', context)


def about(request):
    context = {
        'content': 'nothing'
    }
    return render(request, 'RuralPopulationApp/about.html', context)
