from selenium.webdriver.common.by import By
from task.Employee import Locators2


class Second_page:
    def __init__(self, d):
        self.first_phn_xpath_txt = d.find_element(By.XPATH, Locators2.first_phn_Xpath)
        self.second_phn_txt = d.find_element(By.XPATH, Locators2.second_phn_xpath)
        self.third_phn_txt = d.find_element(By.XPATH, Locators2.third_phn_xpath)
        self.fourth_phn_txt = d.find_element(By.XPATH, Locators2.first_phn_Xpath)
        self.fifth_phn_txt = d.find_element(By.XPATH, Locators2.fifth_phn_xpath)

    def get_first_phn(self):
        return self.first_phn_xpath_txt

    def get_second_phn(self):
        return self.second_phn_txt

    def get_third_phn(self):
        return self.third_phn_txt

    def get_fourth_phn(self):
        return self.fourth_phn_txt

    def get_fifth_phn(self):
        return self.fifth_phn_txt
