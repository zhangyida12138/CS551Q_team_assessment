from django.shortcuts import render
from django.db.models import Prefetch
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
        # 'regions': regions,
        # "income_groups": income_groups
    }
    return render(request, 'RuralPopulationApp/countries.html', context)
    
def income_groups(request):
    return render(request, 'RuralPopulationApp/income_groups.html')

def regions(request):
    return render(request, 'RuralPopulationApp/regions.html')


