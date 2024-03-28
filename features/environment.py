from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import django
from django.conf import settings
import os

def before_all(context):
    # Ensure Django settings are correctly loaded
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
    django.setup()

    # Initialize WebDriver options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Headless mode, browser interface won't be displayed
    chrome_options.add_argument("--no-sandbox")  # Necessary when running in Docker or CI systems
    chrome_options.add_argument("--disable-dev-shm-usage")  # To avoid resource constraint issues
    chrome_options.add_argument("--window-size=1920,1080")  # Set window size

    # Initialize WebDriver
    # Please adjust according to the path of your ChromeDriver
    context.browser = webdriver.Chrome(options=chrome_options)

    # Set implicit wait time
    context.browser.implicitly_wait(5)
    context.home_page_url = "https://repairolivia-nylonsincere-8000.codio-box.uk/"

def after_all(context):
    # Close the browser after the tests are finished
    if hasattr(context, 'browser'):  # Check if the context object has a 'browser' attribute
        context.browser.quit()

def before_scenario(context, scenario):
    # Operations that can be performed before each scenario starts (if necessary)
    pass

def after_scenario(context, scenario):
    # Operations that can be performed after each scenario ends (if necessary), for example, cleaning up test data
    pass
