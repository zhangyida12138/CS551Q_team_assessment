import urllib
from urllib.parse import urljoin
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@when(u'we click the Home button')
def step_impl(context):
    # Assuming the Home button can be identified by its link text
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'Home'))
    )
    home_button = context.browser.find_element(By.LINK_TEXT, 'Home')
    home_button.click()


@then(u'it load home page')
def step_impl(context):
    expected_url = context.browser.current_url
    assert 'countries' in expected_url