import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from utilities import ConfigReader

def before_scenario(context,driver):

    browser_name = "chrome" #ConfigReader.config_reader("basic info","browser")

    if browser_name.__eq__("chrome"):
        context.driver = webdriver.Chrome()
    elif browser_name.__eq__("edge"):
        context.driver = webdriver.Edge()

    context.driver.get("https://tutorialsninja.com/demo/")
    context.driver.maximize_window()
    #context.driver.get(configReader.config_reader("basic info","url"))


def after_scenario(context,driver):
    context.driver.quit()

def after_step(context,step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(),name='failed_screensot.png',attachment_type=AttachmentType.PNG)

