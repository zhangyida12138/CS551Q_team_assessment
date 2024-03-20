from django.db import models

# Country model would change to have foreign keys to Region and IncomeGroup
class Country(models.Model):
    name = models.TextField()
    country_code = models.CharField(max_length=3)
    region = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True)
    income_group = models.ForeignKey('IncomeGroup', on_delete=models.SET_NULL, null=True)
    special_notes = models.TextField()

class DataEntry(models.Model):
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    year = models.IntegerField(choices=[(year, year) for year in range(2000, 2023)])
    value = models.DecimalField(max_digits=5, decimal_places=2)  # Adjust max_digits as needed

class Region(models.Model):
    name = models.CharField(
        max_length=30,
        choices=[
            ('Latin America & Caribbean', 'Latin America & Caribbean'),
            ('South Asia', 'South Asia'),
            ('Sub-Saharan Africa', 'Sub-Saharan Africa'),
            ('Europe & Central Asia', 'Europe & Central Asia'),
            ('Middle East & North Africa', 'Middle East & North Africa'),
            ('East Asia & Pacific', 'East Asia & Pacific'),
            ('North America', 'North America'),
            ('No region', 'No region')
        ]
    )

class IncomeGroup(models.Model):
    name = models.CharField(
        max_length=20,
        choices=[
            ('Low income', 'Low income'),
            ('Lower middle income', 'Lower middle income'),
            ('Upper middle income', 'Upper middle income'),
            ('High income', 'High income'),
            ('No group', 'No group')
        ]
    )

class RegionCountries(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

class IncomeCountries(models.Model):
    income_group = models.ForeignKey(IncomeGroup, on_delete=models.CASCADE)