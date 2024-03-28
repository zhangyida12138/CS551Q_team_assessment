from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from urllib.parse import urljoin

@given(u'the user is on the Compare Countries Rural Population page')
def step_impl(context):
    compare_countries_url = urljoin(context.home_page_url,'compare_countries/')
    context.browser.get(compare_countries_url)
    actual_title = context.browser.title
    print(f"Actual page title: '{actual_title}'")  # This will print the actual title to the console.
    assert "Comparison of Countries" in actual_title

@when(u'the user selects "{country_1}" from the dropdown1')
def step_impl(context,country_1):
    wait = WebDriverWait(context.browser, 10)
    dropdown = wait.until(EC.element_to_be_clickable((By.NAME, 'country_code_1')))
    dropdown.click()
    # select = Select(dropdown)
    # select.select_by_visible_text(country_1)
    # Print all options for debugging purposes
    options = context.browser.find_elements(By.TAG_NAME, "option")
    for option in options:
        if(option.text==country_1):
            option.click()
            break
    
    # # Wait and click the specific option
    # option = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Aruba(ABW)')))
    # option.click()

@when(u'the user selects "{country_2}" from the dropdown2')
def step_impl(context,country_2):
    wait = WebDriverWait(context.browser, 10)
    dropdown = wait.until(EC.element_to_be_clickable((By.NAME, 'country_code_2')))
    dropdown.click()
    # select = Select(dropdown)
    # select.select_by_visible_text(country_2)
    # Print all options for debugging purposes
    options = context.browser.find_elements(By.TAG_NAME, "option")
    for option in options:
        if(option.text==country_2):
            option.click()
            break

@when(u'the user clicks the compare button')
def step_impl(context):
    submit_button = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
    )
    submit_button.click()


@then(u'the comparison for "{country_1}" and "{country_2}" should be displayed')
def step_impl(context,country_1,country_2):
    try:
        wait = WebDriverWait(context.browser, 10)
        # Check if at least one country is displayed
        country_locator = (By.ID, 'container')
        wait.until(EC.presence_of_element_located(country_locator))
        # You may also want to check for the presence of multiple countries, not just one
    except TimeoutException:
        raise AssertionError(f"Countries were not displayed after submitting the form.")