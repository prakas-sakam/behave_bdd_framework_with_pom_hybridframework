from selenium.webdriver.common.by import By

from features.pages.account_page import Account_Page
from features.pages.base_page import Base_Page


class Register_Page(Base_Page):
    def __init__(self,driver):
        super().__init__(driver)


    first_name_xpath = "//input[@id='input-firstname']"
    last_name_xpath = "//input[@id='input-lastname']"
    email_xpath = "//input[@id='input-email']"
    telephone_xpath = "//input[@id='input-telephone']"
    password_xpath = "//input[@id='input-password']"
    confirm_password_xpath = "//input[@id='input-confirm']"
    subscribe_yes_xpath = "//label[normalize-space()='Yes']//input[@name='newsletter']"
    subscribe_no_xpath = "//input[@value='0']"
    privacy_policy_xpath = "//input[@name='agree']"
    continue_button_xpath = "//input[@value='Continue']"
    error_for_invalid_email_xpath = "//div[contains(text(),'E-Mail Address does not appear to be valid!')]"
    error_for_email_already_register_xpath = "//div[@class='alert alert-danger alert-dismissible']"
    def enter_first_name_element(self,firstname):
        self.enter_data_into_element("first_name_xpath", self.first_name_xpath, firstname)
        #self.driver.find_element(By.XPATH,self.first_name_xpath).send_keys(firstname)
    def enter_last_name_element(self,lastname):
        self.enter_data_into_element("last_name_xpath",self.last_name_xpath, lastname)
        #self.driver.find_element(By.XPATH,self.last_name_xpath).send_keys(lastname)
    def enter_email_element(self,email):
        self.enter_data_into_element("email_xpath", self.email_xpath, email)
        #self.driver.find_element(By.XPATH, self.email_xpath).send_keys(email)
    def enter_telephone_element(self,telephone):
        self.enter_data_into_element("telephone_xpath", self.telephone_xpath, telephone)
        #self.driver.find_element(By.XPATH, self.telephone_xpath).send_keys(telephone)
    def enter_password_element(self,password):
        self.enter_data_into_element("password_xpath", self.password_xpath, password)
#        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)
    def enter_confirm_password_element(self,con_password):
        self.enter_data_into_element("confirm_password_xpath", self.confirm_password_xpath, con_password)
        #self.driver.find_element(By.XPATH, self.confirm_password_xpath).send_keys(con_password)
    def click_on_privacy_policy_element(self):
        self.click_on_element("privacy_policy_xpath", self.privacy_policy_xpath)
        #self.driver.find_element(By.XPATH, self.privacy_policy_xpath).click()
    def click_on_continue_element(self):
        self.click_on_element("continue_button_xpath", self.continue_button_xpath)
        #self.driver.find_element(By.XPATH, self.continue_button_xpath).click()
        return Account_Page(self.driver)
    def displaying_error_message_for_nodata_element(self):
        return self.display_status_success_or_error("error_for_invalid_email_xpath", self.error_for_invalid_email_xpath)
        # result = self.driver.find_element(By.XPATH,self.error_for_invalid_email_xpath).is_displayed()
        # return result
    def displaying_error_for_email_already_register(self):
        return self.display_status_success_or_error("error_for_email_already_register_xpath", self.error_for_email_already_register_xpath)
        # result = self.driver.find_element(By.XPATH,self.error_for_email_already_register).is_displayed()
        # return result