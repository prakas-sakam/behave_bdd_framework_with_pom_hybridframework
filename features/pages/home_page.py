from selenium.webdriver.common.by import By

from features.pages.base_page import Base_Page
from features.pages.login_page import Login_Page
from features.pages.register_page import Register_Page
from features.pages.search_page import Search_Page


class Home_Page(Base_Page):
    def __init__(self,driver):
        super().__init__(driver)
    search_box_xpath = "//input[@placeholder='Search']"
    search_icon_xpath = "//button[@class='btn btn-default btn-lg']"
    contactus_icon_xpath = "//i[@class='fa fa-phone']"
    my_account_xpath = "//i[@class='fa fa-user']"
    login_icon_xpath = "//a[normalize-space()='Login']"
    register_icon_xpath = "//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Register']"
    def search_box_element(self,data):
        self.enter_data_into_element("search_box_xpath", self.search_box_xpath, data)
        #self.driver.find_element(By.XPATH,self.search_box_xpath).send_keys(data)

    def click_on_search_icon_element(self):
        self.click_on_element("search_icon_xpath", self.search_icon_xpath)
        #self.driver.find_element(By.XPATH,self.search_icon_xpath).click()
        return Search_Page(self.driver)

    def click_contact_us_icon_element(self):
        self.click_on_element("contactus_icon_xpath", self.contactus_icon_xpath)
        #self.driver.find_element(By.XPATH,self.contactus_icon_xpath).click()

    def click_my_account_element(self):
        self.click_on_element("my_account_xpath", self.my_account_xpath)
        #self.driver.find_element(By.XPATH,self.my_account_xpath).click()

    def click_on_login_element(self):
        self.click_on_element("login_icon_xpath", self.login_icon_xpath)
        #self.driver.find_element(By.XPATH,self.login_icon_xpath).click()
        return Login_Page(self.driver)
    def click_on_register_element(self):
        self.click_on_element("self.register_icon_xpath", self.register_icon_xpath)
        #self.driver.find_element(By.XPATH,self.register_icon_xpath).click()
        return Register_Page(self.driver)
