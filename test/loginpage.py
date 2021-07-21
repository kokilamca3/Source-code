from selenium.webdriver.common.by import By
from test import locators


class Login_page:
    def __init__(self, d):
        self.txt_username = d.find_element(By.ID, locators.user_name_id)
        self.txt_password = d.find_element(By.ID, locators.pwd_id_id)
        self.txt_btn_login = d.find_element(By.ID, locators.btn_id)

    def get_txt_username(self):
        return self.txt_username

    def get_txt_password(self):
        return self.txt_password

    def get_btn_id(self):
        return self.txt_btn_login
