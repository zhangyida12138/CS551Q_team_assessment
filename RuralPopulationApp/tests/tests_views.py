from django.test import TestCase
from django.urls import reverse
from RuralPopulationApp.models import Country, Region, IncomeGroup,RegionCountries

class ViewTestCase(TestCase):
    def setUp(self):
        # Setup test data
        self.region = Region.objects.create(name="Test Region")
        self.income_group = IncomeGroup.objects.create(name="Test Income Group")
        self.country = Country.objects.create(name="Test Country", country_code="TC", region=self.region, income_group=self.income_group)

    def test_countries_view(self):
        # Test the countries view
        response = self.client.get(reverse('countries'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'RuralPopulationApp/countries.html')
        self.assertIn('countries', response.context)
        self.assertIn('regions', response.context)
        self.assertIn('income_groups', response.context)

    def test_compare_countries_view(self):
        # Test the compare_countries view
        # Create another country for comparison
        country2 = Country.objects.create(name="Another Test Country", country_code="ATC", region=self.region, income_group=self.income_group)
        response = self.client.get(reverse('compare_countries'), {'country_code_1': 'TC', 'country_code_2': 'ATC'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'RuralPopulationApp/compare_countries.html')
        self.assertIn('country_1', response.context)
        self.assertIn('country_2', response.context)
        self.assertEqual(response.context['country_1'].name, "Test Country")
        self.assertEqual(response.context['country_2'].name, "Another Test Country")

    def test_compare_region_with_correct_input(self):
        # Test the compare_countries_in_region view with correct input
        country1 = Country.objects.create(name="Another Test Country", country_code="ATC", region=self.region, income_group=self.income_group)
        RegionCountries1 = RegionCountries.objects.create(region=self.region, country=country1)
        response = self.client.get(reverse('compare_countries_in_region'), {"region_id": 1}, follow=True)
        self.assertEqual(response.status_code, 200) # Check if the site is accessible
        self.assertTemplateUsed(response, 'RuralPopulationApp/compare_countries_in_region.html') # Check if the correct template is rendered
        self.assertContains(response, "Test Region")

    def test_compare_region_with_string_input(self):
        # Test the compare_countries_in_region view with string input
        response = self.client.get(reverse('countries_in_region'), {"region_id": "asdasc"}, follow=True)
        self.assertContains(response, "Region ID must be a number.") # Check if NaN exception will be raised

    def test_compare_region_with_out_of_range_input(self):
        # Test the compare_countries_in_region view with out-of-range input
        response = self.client.get(reverse('countries_in_region'), {"region_id": "999"}, follow=True) # Check if out-of-range number will be accepted
        self.assertContains(response, "Region not found.")

    def about_page_test(self):
        # Test the about page
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "RuralPopulationApp/about.html")

    def test_show_with_valid_country_code(self):
        """
        The show view should return the country's details for a valid country code.
        """
        url = reverse('show') + '?country_code_1=ABW'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Year")

    def test_show_with_invalid_country_code(self):
        """
        The show view should handle invalid country codes gracefully, possibly showing an error message.
        """
        url = reverse('show') + '?country_code_1=INVALID'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # Assuming you're handling errors without returning a 404.
        self.assertContains(response, "The requested country could not be found.")  # Match your actual error message.







