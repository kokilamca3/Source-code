import time

from allure_commons.types import AttachmentType

from test.subtask import Base
from test.loginpage import Login_page
from test.searchhotel import Searchhotel_page
from test.selecthotelpage import Select_hotelpae
from test.bookhotelpage import Bookhotel
from test.bookorderpage import Book_order
import pytest
import allure


class TestEmployee:

    @pytest.fixture()

    def setup(self):
        s1 = Base()
        self.d = s1.browser_launch()
        s1.url_launch("http://adactin.com/HotelApp/")
        s1.max_window()
        yield
        print("test completed")
        s1.quit_browser()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self, setup):
        s1 = Base()
        l1 = Login_page(self.d)
        s1.set_text(l1.get_txt_username(), "Koku123ve")
        s1.set_text(l1.get_txt_password(), "Koku123ve")
        s1.btn_click(l1.get_btn_id())


        l2 = Searchhotel_page(self.d)
        s1.drop_down1(l2.get_txt_location_id(), "Sydney")
        s1.drop_down1(l2.get_txt_hotel_id1(), "Hotel Creek")
        s1.drop_down1(l2.get_txt_roomtype_id(), "Double")
        s1.drop_down1(l2.get_txt_roomnos(), "3")
        s1.set_text(l2.get_txt_date(), "01/06/2021")
        s1.set_text(l2.get_date_out_id(), "10/06/2021")
        s1.drop_down1(l2.get_adult_id(), "2")
        s1.drop_down1(l2.get_child_id(), "1")
        s1.btn_click(l2.get_serch_btn_id())
        l3 = Select_hotelpae(self.d)
        s1.btn_click(l3.get_sele())
        s1.btn_click(l3.get_continue_btn())
        l4 = Bookhotel(self.d)
        s1.set_text(l4.get_first_name(), "koko")
        s1.set_text(l4.get_lname(), "veeve")
        s1.set_text(l4.get_card_no(), "1234567890123467")
        s1.drop_down1(l4.get_card_type(), "AMEX")
        s1.drop_down1(l4.get_month_ex(), "2")
        s1.drop_down1(l4.get_ex_year(), "2022")
        s1.set_text(l4.get_cc_num(), "12345")
        s1.set_text(l4.get_address(), "elim nagar, 2nd cross street, chennai")
        s1.btn_click(l4.get_book_txt())
        time.sleep(10)
        # Print Book order pag
        l5 = Book_order(self.d)
        s1.getatt(l5.get_order_no())
        allure.attach(self.d.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.png)


t = TestEmployee()
