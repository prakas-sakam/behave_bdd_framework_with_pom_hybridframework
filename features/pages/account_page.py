from selenium.webdriver.common.by import By

from features.pages.base_page import Base_Page


class Account_Page(Base_Page):
    def __init__(self,driver):
        super().__init__(driver)

    account_success_aftr_login_xpath = "//h2[normalize-space()='My Account']"
    account_success_afetr_regi_xpath = "//h1[normalize-space()='Your Account Has Been Created!']"
    def displaying_account_success_after_login_element(self):
        return self.display_status_success_or_error("account_success_aftr_login_xpath", self.account_success_aftr_login_xpath)
        #result = self.driver.find_element(By.XPATH,self.account_success_aftr_login_xpath).is_displayed()
        #return result
    def displaying_account_created_after_register_element(self):
        return self.display_status_success_or_error("account_success_afetr_regi_xpath",self.account_success_afetr_regi_xpath)
        # result = self.driver.find_element(By.XPATH,self.account_success_afetr_regi_xpath).is_displayed()
        # return result