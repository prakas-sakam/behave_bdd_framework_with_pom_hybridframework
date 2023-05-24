from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from features.pages.home_page import Home_Page
from features.pages.search_page import Search_Page


@given(u'i am in home page')
def step_impl(context):
    expected_title = "Your Store"
    assert context.driver.title.__eq__(expected_title)


@when(u'entering valid product say "{product}" in search box field')
def step_impl(context,product):
   context.homepage = Home_Page(context.driver)
   context.homepage.search_box_element(product)

@when(u'clicking on search icon')
def step_impl(context):
    context.search_page = context.homepage.click_on_search_icon_element()

@then(u'valid product has to display')
def step_impl(context):
    assert context.search_page.displaying_result_for_known_element()

@when(u'entering invalid product say "{product}" in search box field')
def step_impl(context,product):
    context.homepage = Home_Page(context.driver)
    context.homepage.search_box_element(product)

@then(u'proper error message has to display')
def step_impl(context):
    assert context.search_page.displaying_error_message_for_unknown_product()

@when(u'no product in search box field')
def step_impl(context):
    context.homepage = Home_Page(context.driver)
    context.homepage.search_box_element("--")
