import time

from behave import *

from selenium.webdriver.common.by import By

from features.pages.account_page import Account_Page
from features.pages.home_page import Home_Page
from features.pages.login_page import Login_Page
from features.utilities.timestamp import get_new_email_from_timestamp


@given(u'in login page')
def step_impl(context):
    context.homepage = Home_Page(context.driver)
    context.homepage.click_my_account_element()
    context.loginpage = context.homepage.click_on_login_element()

@when(u'entering email say "{email}" and password "{password}" in fields')
def step_impl(context, email, password):
    context.loginpage.enter_data_into_user_name_element(email)
    context.loginpage.enter_data_into_password_element(password)

@when(u'clicking on login button')
def step_impl(context):
    context.loginpage.click_on_login_button_element()


@then(u'account page has to open successfully')
def step_impl(context):
    context.accountpage = Account_Page(context.driver)
    assert context.accountpage.displaying_account_success_after_login_element()


@when(u'entering unknown email and "{password}" in fields')
def step_impl(context, password):
    invalid_email = get_new_email_from_timestamp()
    context.loginpage.enter_data_into_user_name_element(invalid_email)
    context.loginpage.enter_data_into_password_element(password)


@then(u'proper errorr message has to display')
def step_impl(context):
    assert context.loginpage.displaying_error_message_element_for_wrong_email_pass()


@when(u'din\'t entering email password in fields')
def step_impl(context):
    context.loginpage.enter_data_into_user_name_element(" ")
    context.loginpage.enter_data_into_password_element(" ")




