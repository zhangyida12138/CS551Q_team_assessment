from django.db import models

# The Country model represents a country with attributes including
# name, country code, associated region, income group, and any special notes.
class Country(models.Model):
    # The name of the country.
    name = models.TextField()
    # A unique 3-letter country code.
    country_code = models.CharField(max_length=3)
    # A foreign key link to the Region model. If the referenced Region is deleted, 
    # the region field in Country model will be set to NULL.
    region = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True)
    # A foreign key link to the IncomeGroup model. Similar to region, 
    # if the IncomeGroup is deleted, this field will be set to NULL.
    income_group = models.ForeignKey('IncomeGroup', on_delete=models.SET_NULL, null=True)
    # Any special notes related to the country.
    special_notes = models.TextField()

# DataEntry model represents a record of data for a country for a specific year and value.
class DataEntry(models.Model):
    # A foreign key link to the Country model. If the referenced Country is deleted,
    # all DataEntry records associated with it will also be deleted (CASCADE).
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    # The year of the data entry. Choices are limited to years from 2000 to 2022.
    year = models.IntegerField(choices=[(year, year) for year in range(2000, 2023)])
    # The value of the data entry. Adjust max_digits as needed based on expected values.
    value = models.DecimalField(max_digits=5, decimal_places=2)

# Region model represents a geographical region.
class Region(models.Model):
    # The name of the region with pre-defined choices.
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

# IncomeGroup model represents a financial classification for countries.
class IncomeGroup(models.Model):
    # The name of the income group with pre-defined choices.
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

# The RegionCountries model seems to be an incomplete attempt to link regions with countries,
# but it lacks a country field to make the link meaningful.
class RegionCountries(models.Model):
    # A foreign key link to the Region model. If the referenced Region is deleted,
    # the RegionCountries record will also be deleted (CASCADE).
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

# Similar to RegionCountries, the IncomeCountries model intends to link income groups with countries,
# but it is missing a country field to complete the relationship.
class IncomeCountries(models.Model):
    # A foreign key link to the IncomeGroup model. If the referenced IncomeGroup is deleted,
    # the IncomeCountries record will also be deleted (CASCADE).
    income_group = models.ForeignKey(IncomeGroup, on_delete=models.CASCADE)
