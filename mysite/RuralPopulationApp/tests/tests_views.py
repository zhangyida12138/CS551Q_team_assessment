from django.test import TestCase
from django.urls import reverse
from RuralPopulationApp.models import Country, Region, IncomeGroup


class ViewTestCase(TestCase):
    def setUp(self):
        # Setup test data
        self.region = Region.objects.create(name="Test Region")
        self.income_group = IncomeGroup.objects.create(name="Test Income Group")
        self.country = Country.objects.create(name="Test Country", country_code="TC", region=self.region, income_group=self.income_group)


    def test_countries_view(self):
        response = self.client.get(reverse('countries'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'RuralPopulationApp/countries.html')
        self.assertIn('countries', response.context)
        self.assertIn('regions', response.context)
        self.assertIn('income_groups', response.context)

    def test_compare_countries_view(self):
        # Create another country for comparison
        country2 = Country.objects.create(name="Another Test Country", country_code="ATC", region=self.region, income_group=self.income_group)
        response = self.client.get(reverse('compare_countries'), {'country_code_1': 'TC', 'country_code_2': 'ATC'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'RuralPopulationApp/compare_countries.html')
        self.assertIn('country_1', response.context)
        self.assertIn('country_2', response.context)
        self.assertEqual(response.context['country_1'].name, "Test Country")
        self.assertEqual(response.context['country_2'].name, "Another Test Country")

