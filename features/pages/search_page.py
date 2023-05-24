from selenium.webdriver.common.by import By

from features.pages.base_page import Base_Page


class Search_Page(Base_Page):
    def __init__(self,driver):
        super().__init__(driver)

    hp_product_xpath = "//a[normalize-space()='HP LP3065']"
    no_product_xpath = "//p[contains(text(),'There is no product that matches the search criter')]"
    def displaying_result_for_known_element(self):
        return self.display_status_success_or_error("hp_product_xpath", self.hp_product_xpath)
       #return self.driver.find_element(By.XPATH, self.hp_product_xpath).is_displayed()
    def displaying_error_message_for_unknown_product(self):
        return self.display_status_success_or_error("no_product_xpath", self.no_product_xpath)
        # result = self.driver.find_element(By.XPATH,self.no_product_xpath).is_displayed()
        # return result

