from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@given(u'the user is on the home page')
def step_impl(context):
    context.browser.get(context.home_page_url)
    actual_title = context.browser.title
    print(f"Actual page title: '{actual_title}'")  # This will print the actual title to the console.
    assert "Countries" in actual_title

@when(u'the user selects an "{income_group}" group from the dropdown')
def step_impl(context, income_group):
    # Wait for the dropdown to be clickable and select the income group
    wait = WebDriverWait(context.browser, 10)
    dropdown = wait.until(EC.element_to_be_clickable((By.ID, 'income_group_id')))
    
    # Click the dropdown and select the income group
    dropdown.click()
    option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//option[text()='{income_group}']")))
    option.click()

@when(u'the user clicks the submit button')
def step_impl(context):
    submit_button = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
    )
    submit_button.click()

@then(u'the countries for the "{income_group}" group should be displayed')
def step_impl(context, income_group):
    # This step assumes that the income group will be displayed in a specific column in the table rows
    try:
        wait = WebDriverWait(context.browser, 10)
        # Check if at least one country with the selected income group is displayed
        income_group_locator = (By.XPATH, f"//td[text()='{income_group}']")
        wait.until(EC.presence_of_element_located(income_group_locator))
        # You may also want to check for the presence of multiple countries, not just one
    except TimeoutException:
        raise AssertionError(f"Countries for the income group {income_group} were not displayed after submitting the form.")
