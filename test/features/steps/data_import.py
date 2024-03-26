import pandas as pd
from RuralPopulationApp.models import Country, Region, IncomeGroup, DataEntry, RegionCountries, IncomeCountries
from django.core.management.base import BaseCommand
import os
import sys

@given('has created an empty SQLite database')
