from selenium.webdriver.common.by import By

from features.pages.account_page import Account_Page
from features.pages.base_page import Base_Page


class Login_Page(Base_Page):
    def __init__(self,driver):
        super().__init__(driver)


    user_name_field_xpath = "//input[@id='input-email']"
    password_field_xpath = "//input[@id='input-password']"
    login_button_xpath = "//input[@value='Login']"
    forgot_password_xpath = "//div[@class='form-group']//a[normalize-space()='Forgotten Password']"
    error_message_for_wrong_email_password_xpath = "//div[@class='alert alert-danger alert-dismissible']"
    def enter_data_into_user_name_element(self,data):
        self.enter_data_into_element("user_name_field_xpath", self.user_name_field_xpath, data)
        #self.driver.find_element(By.XPATH,self.user_name_field_xpath).send_keys(data)

    def enter_data_into_password_element(self,data):
        self.enter_data_into_element("password_field_xpath", self.password_field_xpath, data)
        #self.driver.find_element(By.XPATH,self.password_field_xpath).send_keys(data)

    def click_on_forgot_password_element(self):
        self.click_on_element("forgot_password__xpath",self.forgot_password_xpath)
        #self.driver.find_element(By.XPATH,self.forgot_password_xpath).click()

    def click_on_login_button_element(self):
        self.click_on_element("login_button_xpath", self.login_button_xpath)
        #self.driver.find_element(By.XPATH,self.login_button_xpath).click()
        return Account_Page(self.driver)

    def displaying_error_message_element_for_wrong_email_pass(self):
        return self.display_status_success_or_error("error_message_for_wrong_email_password_xpath", self.error_message_for_wrong_email_password_xpath)
        #return self.driver.find_element(By.XPATH,self.error_message_for_wrong_email_password_xpath).is_displayed()