from selenium.webdriver.common.by import By
from test import locators


class Select_hotelpae:
    def __init__(self, d):
        self.txt_sele_id_id = d.find_element(By.ID, locators.sele_id_id)
        self.txt_continue_btn_id = d.find_element(By.ID, locators.continue_btn_id)

    def get_sele(self):
            return self.txt_sele_id_id

    def get_continue_btn(self):
        return self.txt_continue_btn_id
