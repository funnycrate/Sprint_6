import pytest
import allure
from selenium import webdriver
from Page_Objects.main_page import MainPageBody
from locators.main_page_locators import MainPageLocators
from data import *


@allure.suite("Тестирование блока главной страницы 'Вопросы о важном'")
@allure.feature("Проверка текста ответов на вопросы")
class TestQuestionAnswers:

    @allure.title('Проверяем текст ответов в разделе "Вопросы о важном"')
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('https://qa-scooter.praktikum-services.ru/')
        cls.main_page = MainPageBody(cls.driver)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @pytest.mark.parametrize("question_locator, answer_locator, expected_answer", [
        (MainPageLocators.question_0_locator, MainPageLocators.answer_0_locator, Answers.expected_answers[0]),
        (MainPageLocators.question_1_locator, MainPageLocators.answer_1_locator, Answers.expected_answers[1]),
        (MainPageLocators.question_2_locator, MainPageLocators.answer_2_locator, Answers.expected_answers[2]),
        (MainPageLocators.question_3_locator, MainPageLocators.answer_3_locator, Answers.expected_answers[3]),
        (MainPageLocators.question_4_locator, MainPageLocators.answer_4_locator, Answers.expected_answers[4]),
        (MainPageLocators.question_5_locator, MainPageLocators.answer_5_locator, Answers.expected_answers[5]),
        (MainPageLocators.question_6_locator, MainPageLocators.answer_6_locator, Answers.expected_answers[6]),
        (MainPageLocators.question_7_locator, MainPageLocators.answer_7_locator, Answers.expected_answers[7]),
    ])
    @allure.title("Проверяем текст ответа")
    def test_question_answer(self, question_locator, answer_locator, expected_answer):
        with allure.step('Прокручиваем к секции с вопросами'):
            self.main_page.scroll_to_questions_place()

        with allure.step(f'Получаем текст ответа для вопроса с локатором {question_locator}'):
            actual_answer = self.main_page.get_text_question(question_locator, answer_locator)

        with allure.step(f'Проверяем, что текст ответа соответствует ожидаемому'):
            assert actual_answer == expected_answer, f"Ожидаемый ответ: {expected_answer}, но был получен: {actual_answer}"

