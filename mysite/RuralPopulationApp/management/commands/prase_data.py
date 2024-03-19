import pandas as pd
from RuralPopulationApp.models import Country, Region, IncomeGroup, DataEntry
from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = 'Load data from Excel file'

    def handle(self, *args, **kwargs):
        file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'API_SP.RUR.TOTL.ZS_DS2_en_excel_v2_6552759.xls')
        absolute_file_path = os.path.abspath(file_path)
        
        try:
            data_df = pd.read_excel(absolute_file_path, sheet_name='Data',header=3)
            metadata_df = pd.read_excel(absolute_file_path, sheet_name='Metadata - Countries')
        except FileNotFoundError:
            print(f"File not found at path: {absolute_file_path}")
            return
        except xlrd.biffh.XLRDError as e:
            print(f"Error reading file: {e}")
            return

        # Print column names to debug
        print("Data Columns:", data_df.columns.tolist())
        print("Metadata Columns:", metadata_df.columns.tolist())
        
        # Insert Regions and Income Groups
        regions = {name: Region.objects.get_or_create(name=name)[0] for name in metadata_df['Region'].unique()}
        income_groups = {name: IncomeGroup.objects.get_or_create(name=name)[0] for name in metadata_df['IncomeGroup'].unique()}
        
        # Insert Countries with metadata
        for _, row in metadata_df.iterrows():
            country, created = Country.objects.update_or_create(
                country_code=row['Country Code'],
                defaults={
                    'name': row['TableName'],
                    'region': regions[row['Region']],
                    'income_group': income_groups[row['IncomeGroup']],
                    'special_notes': row.get('SpecialNotes', '')
                }
            )
        
        # Insert Data Entries
        for year in range(2000, 2023):
            for _, row in data_df.iterrows():
                country_code = row['Country Code']
                value = row[str(year)]
                if pd.notnull(value):
                    country = Country.objects.get(country_code=country_code)
                    DataEntry.objects.update_or_create(
                        country=country,
                        year=year,
                        defaults={'value': value}
                    )

        print('Data import complete.')
