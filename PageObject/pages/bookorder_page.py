from selenium.webdriver.common.by import By
from PageObject import locators


class Book_order:
    def __init__(self, d):
        self.txt_book_id = d.find_element(By.ID, locators.order_no_id)

    def get_order_no(self):
        return self.txt_book_id
