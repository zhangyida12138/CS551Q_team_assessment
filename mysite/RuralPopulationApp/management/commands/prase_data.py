import pandas as pd
from RuralPopulationApp.models import Country, Region, IncomeGroup, DataEntry
from django.core.management.base import BaseCommand
import os

# Custom command class for managing data import from an Excel file
class Command(BaseCommand):
    help = 'Load data from Excel file'  # Description of the command

    def handle(self, *args, **kwargs):
        # Constructing the file path to the Excel file
        file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'API_SP.RUR.TOTL.ZS_DS2_en_excel_v2_6552759.xls')
        absolute_file_path = os.path.abspath(file_path)  # Getting absolute path
        
        try:
            # Attempting to read the data from the Excel file
            data_df = pd.read_excel(absolute_file_path, sheet_name='Data', header=3)  # Reading the 'Data' sheet
            metadata_df = pd.read_excel(absolute_file_path, sheet_name='Metadata - Countries')  # Reading the 'Metadata - Countries' sheet
        except FileNotFoundError:  # Handling the case where the file is not found
            print(f"File not found at path: {absolute_file_path}")
            return
        except xlrd.biffh.XLRDError as e:  # Handling errors during file reading
            print(f"Error reading file: {e}")
            return

        # Debugging output: print the column names from both sheets
        print("Data Columns:", data_df.columns.tolist())
        print("Metadata Columns:", metadata_df.columns.tolist())
        
        # Inserting Regions and Income Groups into the database
        regions = {name: Region.objects.get_or_create(name=name)[0] for name in metadata_df['Region'].unique()}
        income_groups = {name: IncomeGroup.objects.get_or_create(name=name)[0] for name in metadata_df['IncomeGroup'].unique()}
        
        # Inserting Countries with metadata into the database
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
        
        # Inserting Data Entries into the database
        for year in range(2000, 2023):
            for _, row in data_df.iterrows():
                country_code = row['Country Code']
                value = row[str(year)]
                if pd.notnull(value):  # Check if the value for the year is not null
                    country = Country.objects.get(country_code=country_code)  # Retrieve the corresponding country
                    DataEntry.objects.update_or_create(
                        country=country,
                        year=year,
                        defaults={'value': value}  # Set the data entry's value
                    )
        
        for _, row in metadata_df.iterrows():
            # Fetch the country instance based on the country code
            country = Country.objects.get(country_code=row['Country Code'])
            
            # Fetch the region and income group instances for the current row
            region = regions.get(row['Region'])
            income_group = income_groups.get(row['IncomeGroup'])
            
            # Only proceed if the region and income group instances exist for the current country
            if region and income_group:
                # Create or update RegionCountries entry
                RegionCountries.objects.update_or_create(country=country, region=region)
                
                # Create or update IncomeCountries entry
                IncomeCountries.objects.update_or_create(country=country, income_group=income_group)

        print('Data import complete.')  # Indicate the completion of the data import process
