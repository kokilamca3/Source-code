from selenium import webdriver
from selenium.webdriver.support.select import Select
import openpyxl
class Base:
    def browser_launch(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Airtel\PycharmProjects\python day9\task\chromedriver.exe")
        return self.driver
    def url_launch(self, url):
        self.driver.get(url)
    def max_window(self):
        self.driver.maximize_window()
    def set_text(self, element, in_data):
        element.send_keys(in_data)
    def btn_click(self, element2):
        element2.click()
    def drop_down1(self, dd_element, value):
        s = Select(dd_element)
        s.select_by_value(value)
    def getatt(self, element22):
        p = element22.get_attribute('value')
        print(p)
    def get_data_from_excel(self,excel_loc,row_value,cell_value):
        w=openpyxl.load_workbook(excel_loc)
        sheet=w.active
        c=sheet.cell(row_value,cell_value)
        data=c.value
        return data
