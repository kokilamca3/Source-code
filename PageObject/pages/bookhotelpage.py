from selenium.webdriver.common.by import By
from PageObject import locators


class Bookhotel:
    def __init__(self, d):
        self.txt_first_name = d.find_element(By.ID, locators.firstname_id)
        self.txt_lname_id = d.find_element(By.ID, locators.laname_id)
        self.txt_card_no = d.find_element(By.ID, locators.card_no_id)
        self.txt_card_type = d.find_element(By.ID, locators.card_type_id)
        self.txt_month_ex = d.find_element(By.ID, locators.month_ex_id)
        self.txt_ex_year = d.find_element(By.ID, locators.ex_year_id)
        self.txt_cc_num = d.find_element(By.ID, locators.cc_num_id)
        self.txt_address = d.find_element(By.ID, locators.add_id_id)
        self.txt_book = d.find_element(By.ID, locators.book_id_id)

    def get_first_name(self):
        return self.txt_first_name

    def get_lname(self):
        return self.txt_lname_id

    def get_card_no(self):
        return self.txt_card_no

    def get_card_type(self):
        return self.txt_card_type

    def get_month_ex(self):
        return self.txt_month_ex

    def get_ex_year(self):
        return self.txt_ex_year

    def get_cc_num(self):
        return self.txt_cc_num

    def get_address(self):
        return self.txt_address

    def get_book_txt(self):
        return self.txt_book
