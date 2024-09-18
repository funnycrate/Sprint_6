import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import *
from Page_Objects.base_page import BasePageHeader
from Page_Objects.order_page import *

@allure.suite("Тестирование заказов самокатов")
@allure.feature("Оформление заказа")
class TestOrder:

    @allure.title('Проверка всего флоу позитивного сценария с двумя наборами данных')
    @pytest.mark.parametrize("user_data",[UserData.user_1, UserData.user_2])
    def test_correct_order(self, driver, user_data):
        home_page = BasePageHeader(driver)
        order_page = OrderPage(driver)
        home_page.upper_order_button_click()
        order_page.send_first_name(user_data)
        order_page.send_last_name(user_data)
        order_page.send_address(user_data)
        order_page.send_metro(user_data)
        order_page.send_telephone(user_data)
        order_page.click_next_button()
        order_page.send_date(user_data)
        order_page.send_rental_period(user_data)
        order_page.send_color_scooter(user_data)
        order_page.send_comment(user_data)
        order_page.click_order_button()
        order_page.click_yes_button()
        assert order_page.show_status_text()