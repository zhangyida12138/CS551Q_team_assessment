from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from urllib.parse import urljoin


@given(u'the user is on the Comparison of Countries in Region page')
def step_impl(context):
    compare_countries_url = urljoin(context.home_page_url,'compare_countries_in_region/')
    context.browser.get(compare_countries_url)
    actual_title = context.browser.title
    print(f"Actual page title: '{actual_title}'")  # This will print the actual title to the console.
    assert "Comparison of Countries in Region" in actual_title

@when(u'the user input "{region_code}" in the search bar')
def step_impl(context,region_code):
    wait = WebDriverWait(context.browser, 10)
    input_field = wait.until(EC.element_to_be_clickable((By.NAME, 'region_id')))
    input_field.clear()
    input_field.send_keys(region_code)


@when(u'the user clicks the compare button1')
def step_impl(context):
    submit_button = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
    )
    submit_button.click()

@then(u'the countries for the "{region_name}" group should be displayed1')
def step_impl(context, region_name):
    try:
        wait = WebDriverWait(context.browser, 10)
        # Check if at least one country is displayed
        country_locator = (By.ID, 'container')
        wait.until(EC.presence_of_element_located(country_locator))
        # You may also want to check for the presence of multiple countries, not just one
    except TimeoutException:
        raise AssertionError(f"Countries were not displayed after submitting the form.")