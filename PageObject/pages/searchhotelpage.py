from selenium.webdriver.common.by import By
from PageObject import locators


class Searchhotel_page:
    def __init__(self, d):
        self.txt_location_id = d.find_element(By.ID, locators.loc_id_id)
        self.txt_hotel_id = d.find_element(By.ID, locators.hotel_id_id)
        self.txt_roomtype_id_id=d.find_element(By.ID,locators.room_type_id)
        self.txt_roomnos_id_id=d.find_element(By.ID,locators.room_nos_id)
        self.txt_date_id_id=d.find_element(By.ID,locators.date_id_id)
        self.txt_date_out_id_id=d.find_element(By.ID,locators.date_out_id)
        self.txt_adult_id=d.find_element(By.ID,locators.adult_room_id)
        self.txt_child_id=d.find_element(By.ID,locators.child_room_id)
        self.txt_serch_btn_id=d.find_element(By.ID,locators.search_btn_id)
    def get_txt_location_id(self):
        return self.txt_location_id

    def get_txt_hotel_id1(self):
        return self.txt_hotel_id
    def get_txt_roomtype_id(self):
        return self.txt_roomtype_id_id
    def get_txt_roomnos(self):
        return self.txt_roomnos_id_id
    def get_txt_date(self):
        return self.txt_date_id_id
    def get_date_out_id(self):
        return self.txt_date_out_id_id
    def get_adult_id(self):
        return self.txt_adult_id
    def get_child_id(self):
        return self.txt_child_id
    def get_serch_btn_id(self):
        return self.txt_serch_btn_id
