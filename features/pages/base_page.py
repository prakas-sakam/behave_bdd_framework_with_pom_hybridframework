from selenium.webdriver.common.by import By


class Base_Page:
    def __init__(self, driver):
        self.driver = driver

    element = None

    def click_on_element(self,locater_type ,locater_value):

        if locater_type.endswith("xpath"):
            element = self.driver.find_element(By.XPATH,locater_value)
            element.click()
        elif locater_type.endswith("id"):
            element = self.driver.find_element(By.ID, locater_value)
            element.click()
        elif locater_type.endswith("name"):
            element = self.driver.find_element(By.NAME, locater_value)
            element.click()
        elif locater_type.endswith("link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locater_value)
            element.click()
        elif locater_type.endswith("tag_name"):
            element = self.driver.find_element(By.TAG_NAME, locater_value)
            element.click()
        elif locater_type.endswith("css_selector"):
            element = self.driver.find_element(By.CSS_SELECTOR, locater_value)
            element.click()


    def enter_data_into_element(self,locater_type,locater_value,data):

        if locater_type.endswith("xpath"):
            element = self.driver.find_element(By.XPATH, locater_value)
            element.click()
            element.clear()
            element.send_keys(data)
        elif locater_type.endswith("id"):
            element = self.driver.find_element(By.ID, locater_value)
            element.click()
            element.clear()
            element.send_keys(data)
        elif locater_type.endswith("name"):
            element = self.driver.find_element(By.NAME, locater_value)
            element.click()
            element.clear()
            element.send_keys(data)
        elif locater_type.endswith("link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locater_value)
            element.click()
            element.clear()
            element.send_keys(data)
        elif locater_type.endswith("tag_name"):
            element = self.driver.find_element(By.TAG_NAME, locater_value)
            element.click()
            element.clear()
            element.send_keys(data)
        elif locater_type.endswith("css_selector"):
            element = self.driver.find_element(By.CSS_SELECTOR, locater_value)
            element.click()
            element.clear()
            element.send_keys(data)
    def display_status_success_or_error(self,locater_type,locater_value):
        if locater_type.endswith("xpath"):
            element = self.driver.find_element(By.XPATH, locater_value).is_displayed()
            return element
        elif locater_type.endswith("id"):
            element = self.driver.find_element(By.ID, locater_value).is_displayed()
            return element
        elif locater_type.endswith("name"):
            element = self.driver.find_element(By.NAME, locater_value).is_displayed()
            return element
        elif locater_type.endswith("link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locater_value).is_displayed()
            return element