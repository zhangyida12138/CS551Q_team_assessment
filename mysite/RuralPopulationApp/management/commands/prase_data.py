import pandas as pd
from RuralPopulationApp.models import Country, Region, IncomeGroup, RegionCountries
from django.db.utils import IntegrityError
from django.core.management.base import BaseCommand
import os


# Assume you have pandas and openpyxl already installed.
# If not, you can install them using pip:
# pip install pandas openpyxl
class Command(BaseCommand):
    help = 'Load data from Excel file'

    def handle(self, *args, **kwargs):
        # 构建文件路径，这里 '..' 表示上级目录
        file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'API_SP.RUR.TOTL.ZS_DS2_en_excel_v2_6552759.xls')        # 确保路径是绝对的
        absolute_file_path = os.path.abspath(file_path)
        # 读取 Excel 文件
        data_df = pd.read_excel(absolute_file_path, sheet_name='Data')
        metadata_df = pd.read_excel(absolute_file_path, sheet_name='Metadata - Countries')

        # 导入 Region 和 IncomeGroup 数据
        for _, row in metadata_df.iterrows():
            region, _ = Region.objects.get_or_create(name=row['Region'])
            income_group, _ = IncomeGroup.objects.get_or_create(name=row['IncomeGroup'])

            # 检查 Country 是否存在，如果不存在则创建
            country, created = Country.objects.get_or_create(
                country_code=row['Country Code'],
                defaults={
                    'name': row.get('Country Name', ''),  # 如果 Country Name 列不存在，则使用空字符串
                    'income_group': row['IncomeGroup'],
                    'special_notes': row.get('SpecialNotes', '')  # 如果 SpecialNotes 列不存在，则使用空字符串
                }
            )

            # 如果 Country 是新创建的，需要打印出信息
            if created:
                print(f"Created new country with code: {row['Country Code']}")

            # 尝试创建 RegionCountries 实例
            try:
                RegionCountries.objects.get_or_create(
                    country=country,
                    region=region
                )
            except IntegrityError:
                print(f"RegionCountries entry for {row['Country Code']} already exists.")

        # 处理 Data 表格
        # 注意：由于 Data 表可能不包含足够的信息来创建 Country 实例
        # 因此我们将仅更新存在的 Country 实例
        for _, row in data_df.iterrows():
            # 假设你有列 'Country Code', 'Indicator Name', 和年份如 '1960', '1961', ..., '2022'
            try:
                country = Country.objects.get(country_code=row['Country Code'])
                # 更新现有的国家实例
                country.name = row.get('Country Name', country.name)  # 使用 get 防止 KeyError
                country.income_group = row.get('IncomeGroup', country.income_group)
                country.special_notes = row.get('SpecialNotes', country.special_notes)
                country.save()
            except Country.DoesNotExist:
                print(f"Country with code {row['Country Code']} does not exist and will not be updated.")
            except KeyError as e:
                print(f"Column not found in the DataFrame: {e}")
            except Exception as e:
                print(f"An error occurred: {e}")