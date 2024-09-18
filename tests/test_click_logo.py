import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import *
from Page_Objects.main_page import *
from Page_Objects.base_page import *
from conftest import *


@allure.suite("Тестирование хедера на главной странице")
@allure.feature("Проверка логотипов")
class TestHeaderButton:

    @allure.story("Переход на главную страницу Самоката")
    @allure.title('Проверка: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката»')
    @allure.step('Тест на клик по логотипу Самоката')
    def test_correct_go_to_scooter_button(self, driver):
        main_page = BasePageHeader(driver)
        main_page.upper_order_button_click()
        main_page.scooter_logo_click()
        current_url = main_page.get_current_url()
        title_is_displayed = main_page.check_order_title()

        with allure.step("Проверяем, что URL соответствует главной странице"):
            assert current_url == Urls.BASE_URL

        with allure.step("Проверяем, что заголовок отображается на главной странице"):
            assert title_is_displayed


    @allure.story("Переход на главную страницу Дзена")
    @allure.title('Проверка: если нажать на логотип Яндекса, в новом окне откроется главная страница Дзена')
    @allure.step('Тест на клик по логотипу Яндекса')
    def test_click_yandex_go_to_dzen(self, driver):
        main_page = BasePageHeader(driver)

        with allure.step("Клик по логотипу Яндекса"):
            main_page.yandex_logo_click()

        with allure.step("Переход на новую вкладку и проверка URL"):
            main_page.go_to_new_tab(Urls.DZEN_URL)
            assert main_page.get_current_url() == Urls.DZEN_URL
