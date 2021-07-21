from task.Employee.Subtask import Base1
from task.Employee.Firstpage import First_page
from task.Employee.Secondpage import Second_page


class Amazon:
    def login(self):
        b1 = Base1()
        d = b1.browser_launch()
        b1.url_launch("https://www.amazon.com/")
        b1.max_window()
        f1 = First_page(d)
        b1.user_input(f1.get_userin_txt(), "iphones X")
        b1.btn_click(f1.get_btn_id())
        s1 = Second_page(d)
        first_phn = s1.get_first_phn()

        first_phn_txt = first_phn.text
        b1.get_data_excel(1, 1, first_phn_txt)

        second_phn = s1.get_second_phn()
        second_phn_txt = second_phn.text
        b1.get_data_excel(2, 1, second_phn_txt)
        third_phn = s1.get_third_phn()
        third_phn_txt = third_phn.text
        b1.get_data_excel(3, 1, third_phn_txt)
        fourth_ph = s1.get_fourth_phn()
        fourth_ph_txt = fourth_ph.text
        b1.get_data_excel(4, 1, fourth_ph_txt)
        fifth_phn = s1.get_fifth_phn()
        fifth_phn_txt = fifth_phn.text
        b1.get_data_excel(5, 1, fifth_phn_txt)


e = Amazon()
e.login()
