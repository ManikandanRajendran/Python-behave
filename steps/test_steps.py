import sys

from behave import *
from locators.login_page import login_page_locators


@given('user opens the homepage')
def open_homepage(context):
    context.driver.get(context.base_url)
    context.driver.implicitly_wait(10)


@when('user enters {user} and {pwd}')
def step_impl(context, user, pwd):
    context.driver.find_element_by_id(login_page_locators.username_textbox_id).clear()
    context.driver.find_element_by_id(login_page_locators.username_textbox_id).send_keys(user)
    context.driver.find_element_by_id(login_page_locators.password_textbox_id).clear()
    context.driver.find_element_by_id(login_page_locators.password_textbox_id).send_keys(pwd)
    context.driver.implicitly_wait(10)


@when('user clicks login button')
def step_impl(context):
    context.driver.find_element_by_id(login_page_locators.login_button_id).click()
    context.driver.implicitly_wait(15)


@then('user should see the dashboard page')
def step_impl(context):
    try:
        context.driver.implicitly_wait(10)
        title = context.driver.find_element_by_class_name(login_page_locators.title_class).text
        assert title == "Dashboard", f"Title is not same. Actual {title}"
    except:
        assert False, f'exception : {sys.exc_info()[0]}'
