from selenium.webdriver.common.by import By
from task.Employee import Locators2
class First_page:
    def __init__(self,d):
        self.userin_id_txt=d.find_element(By.ID,Locators2.userin_id)
        self.btn_txt=d.find_element(By.ID,Locators2.btn_id)
    def get_userin_txt(self):
        return self.userin_id_txt
    def get_btn_id(self):
        return self.btn_txt
    

