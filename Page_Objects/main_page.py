from selenium.webdriver.common.by import By
from locators.main_page_locators import  MainPageLocators
from locators.base_page_locators import BasePageLocators
from Page_Objects.base_page import BasePage
import allure


class MainPageBody(BasePage):

    @allure.step('Скролл и клик до нижней кнопки Заказать')
    def middle_order_button_click(self):
        self.scroll_to_element(MainPageLocators.button_order_middle)
        self.click_to_element(MainPageLocators.button_order_middle)

    @allure.step('Переход к вопросам')
    def scroll_to_questions_place(self):
        self.scroll_to_element(MainPageLocators.question_0_locator)

    @allure.step('Клик на вопрос')
    def click_question_button(self, question_button_locator):
        self.scroll_to_questions_place()
        self.click_to_element(question_button_locator)

    @allure.step('Получение текста вопроса')
    def get_text_question(self, question_button_locator, question_text_locator):
        self.click_question_button(question_button_locator)
        return self.get_text_locator(question_text_locator)