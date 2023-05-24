import time

from behave import *
from selenium.webdriver.common.by import By

from features.pages.account_page import Account_Page
from features.pages.home_page import Home_Page
from features.pages.register_page import Register_Page
from features.utilities.timestamp import get_new_email_from_timestamp


@given(u'i am at register page')
def step_impl(context):
    context.homepage = Home_Page(context.driver)
    context.homepage.click_my_account_element()
    context.registerpage = context.homepage.click_on_register_element()


@when(u'entering all below details for to register')
def step_impl(context):
    for row in context.table:
        email_register = get_new_email_from_timestamp()
        context.registerpage.enter_first_name_element(row["f_name"])
        context.registerpage.enter_last_name_element(row["l_name"])
        context.registerpage.enter_email_element(email_register)
        context.registerpage.enter_telephone_element(row["phone"])
        context.registerpage.enter_password_element(row["password"])
        context.registerpage.enter_confirm_password_element(row["confirm_pass"])
        context.registerpage.click_on_privacy_policy_element()

@when(u'clicking on register button')
def step_impl(context):
    context.accountpage = context.registerpage.click_on_continue_element()
@then(u'registration has to be succesfully')
def step_impl(context):
    #context.accountpage = Account_Page(context.driver)
    assert context.accountpage.displaying_account_created_after_register_element()

@when(u'entering all below same email details for to register')
def step_impl(context):
    for row in context.table:
        context.registerpage = Register_Page(context.driver)
        context.registerpage.enter_first_name_element(row["f_name"])
        context.registerpage.enter_last_name_element(row["l_name"])
        context.registerpage.enter_email_element(row["email"])
        context.registerpage.enter_telephone_element(row["phone"])
        context.registerpage.enter_password_element(row["password"])
        context.registerpage.enter_confirm_password_element(row["confirm_pass"])
        context.registerpage.click_on_privacy_policy_element()

@when(u'entering nodetails register')
def step_impl(context):
    context.registerpage = Register_Page(context.driver)
    context.registerpage.enter_first_name_element(" ")
    context.registerpage.enter_last_name_element(" ")
    context.registerpage.enter_email_element(" ")
    context.registerpage.enter_telephone_element(" ")
    context.registerpage.enter_password_element(" ")
    context.registerpage.enter_confirm_password_element(" ")
    context.registerpage.click_on_privacy_policy_element()

@then(u'proper eerror message has to display')
def step_impl(context):
    assert context.registerpage.displaying_error_message_for_nodata_element()

@then(u'proper er message has to display')
def step_impl(context):
    assert context.registerpage.displaying_error_for_email_already_register()
