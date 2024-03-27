import urllib
from urllib.parse import urljoin
from behave import given, when, then

@when(u'we click the Home button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we click the Home button')


@then(u'it load home page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then it load home page')