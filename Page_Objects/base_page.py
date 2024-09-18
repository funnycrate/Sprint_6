from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = BasePageLocators

    @allure.step('Получение текущего URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Ожидание видимости элемента {locator}')
    def wait_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step('Клик по элементу {locator}')
    def click_to_element(self, locator):
        element = self.wait_element(locator)
        element.click()

    @allure.step('Ввод текста "{text}" в элемент {locator}')
    def input_text(self, locator, text):
        element = self.wait_element(locator)
        element.send_keys(text)

    @allure.step('Прокрутка до элемента {locator}')
    def scroll_to_element(self, locator):
        element = self.wait_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Получение текста из элемента {locator}')
    def get_text_locator(self, locator):
        element = self.wait_element(locator)
        return element.text

    @allure.step('Переход на новую вкладку с URL {url}')
    def go_to_new_tab(self, url):
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(EC.url_to_be(url))


class BasePageHeader(BasePage):

    @allure.step('Клик на лого Яндекса')
    def yandex_logo_click(self):
        self.click_to_element(self.locators.logo_yandex)

    @allure.step('Клик на лого Самоката')
    def scooter_logo_click(self):
        self.click_to_element(self.locators.logo_samokat)

    @allure.step('Клик на верхнюю кнопку "Заказать"')
    def upper_order_button_click(self):
        self.click_to_element(self.locators.order_button_upper)

    @allure.step('Проверка отображения заголовка "Учебный проект"')
    def check_order_title(self):
        return self.wait_element(self.locators.header_page_title).is_displayed()
