from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

@given(u'the user is on the home page(detail)')
def step_impl(context):
    context.browser.get(context.home_page_url)
    actual_title = context.browser.title
    print(f"Actual page title: '{actual_title}'")  # This will print the actual title to the console.
    assert "Countries" in actual_title

@when(u'the user clicks the "{country_name}" detail button')
def step_impl(context, country_name):
    try:
        detail_button_xpath = f"//tr[td[normalize-space()='{country_name}']]//a[contains(text(), 'details')]"
        print(f"Looking for button with XPath: {detail_button_xpath}")  # Debugging: Print out the XPath being used.
        detail_button = WebDriverWait(context.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, detail_button_xpath))
        )
        detail_button.click()
    except TimeoutException:
        print("Could not find the detail button within the time limit.")
    except NoSuchElementException:
        print("Could not find the detail button on the page.")

@then(u'the details of "{country_name}" should be shown')
def step_impl(context, country_name):
    try:
        # Adjust this XPath to match the actual details page
        detail_locator = (By.XPATH, f"//h1[contains(., '{country_name}')]")
        WebDriverWait(context.browser, 10).until(EC.presence_of_element_located(detail_locator))
        print(f"Found details for {country_name}.")  # Confirm that the details are shown
    except TimeoutException:
        raise AssertionError(f"The details of {country_name} were not displayed.")