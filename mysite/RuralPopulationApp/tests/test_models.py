from django.core.exceptions import ValidationError
from django.test import TestCase
from RuralPopulationApp.models import Country,DataEntry,Region,IncomeGroup,RegionCountries,IncomeCountries

# Unit tests for the models
class ModelTest(TestCase):
    def setUp(self):
        # Setup run before every test method.
        self.region = Region.objects.create(name='Europe & Central Asia')
        self.income_group = IncomeGroup.objects.create(name='High income')
        self.country = Country.objects.create(
            name="Testland",
            country_code="TST",
            region=self.region,
            income_group=self.income_group,
            special_notes="A test country."
        )

    """Tests that the country was successfully created"""
    def test_country_creation(self):
        self.assertEqual(self.country.name, "Testland")
        self.assertEqual(self.country.country_code, "TST")
        self.assertEqual(self.country.special_notes, "A test country.")
        self.assertEqual(self.country.region.name, 'Europe & Central Asia')
        self.assertEqual(self.country.income_group.name, 'High income')

    """Tests retrieving a Country instance from the database."""
    def test_select_country(self):
        country = Country.objects.get(country_code="TST")
        self.assertEqual(country.name, "Testland")
        self.assertEqual(country.region.name, 'Europe & Central Asia')
        self.assertEqual(country.income_group.name, 'High income')
        self.assertEqual(country.special_notes, "A test country.")

    """Tests editing a Country instance and saving the changes to the database."""
    def test_edit_country(self):
        # Retrieve the country instance to edit
        country = Country.objects.get(country_code="TST")
        # Make some changes
        country.name = "New Testland"
        country.special_notes = "An updated test country."
        # Save the changes
        country.save()
        # Retrieve the updated country instance
        updated_country = Country.objects.get(country_code="TST")
        # Check that the changes were saved
        self.assertEqual(updated_country.name, "New Testland")
        self.assertEqual(updated_country.special_notes, "An updated test country.")

    """Tests creation of a DataEntry for a country"""
    def test_data_entry_creation(self):
        data_entry = DataEntry.objects.create(
            country=self.country,
            year=2021,
            value=50.00
        )
        self.assertEqual(data_entry.year, 2021)
        self.assertEqual(data_entry.value, 50.00)
        self.assertEqual(data_entry.country, self.country)

    """Deletes the 'Testland' country created in setUp."""
    def test_delete_testland_country(self):
        # Optional: Demonstrating the country exists before deletion
        self.assertEqual(Country.objects.filter(name="Testland").count(), 1, "Testland country should exist before deletion.")

        # Perform the deletion
        self.country.delete()

        # Optional: Verifying the country no longer exists after deletion
        self.assertEqual(Country.objects.filter(name="Testland").count(), 0, "Testland country should no longer exist after deletion.")


    """Test creating a DataEntry with a year outside the allowed range raises a ValidationError."""
    def test_create_data_entry_with_invalid_year_raises_error(self):
        country = Country.objects.create(
            name="Testland",
            country_code="TST",
            special_notes="A test country."
        )
        data_entry = DataEntry(
            country=country,
            year=1999,  # This is outside the valid range and should trigger a validation error
            value=50.00
        )
        with self.assertRaises(ValidationError):
            data_entry.full_clean()

    """Tests that creating a Country with an invalid country_code raises ValidationError."""
    def test_create_country_with_invalid_country_code_raises_error(self):
        with self.assertRaises(ValidationError):
            invalid_country = Country(
                name="InvalidCountry",
                country_code="1234",  # this is invalid based on our rule
                region=self.region,
                income_group=self.income_group,
                special_notes="This should fail due to invalid country_code."
            )
            invalid_country.full_clean()  # This method triggers the validation