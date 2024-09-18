from selenium.webdriver.common.by import By

class MainPageLocators:
    button_order_middle = (By.CSS_SELECTOR, '.Button_Button__ra12g.Button_UltraBig__UU3Lp')

    # Локатор для первого вопроса
    question_0_locator = (By.ID, 'accordion__heading-0')
    # Локатор для ответа на первый вопрос
    answer_0_locator = (By.ID, 'accordion__panel-0')

    question_1_locator = (By.ID, 'accordion__heading-1')
    answer_1_locator = (By.ID, 'accordion__panel-1')

    question_2_locator = (By.ID, 'accordion__heading-2')
    answer_2_locator = (By.ID, 'accordion__panel-2')

    question_3_locator = (By.ID, 'accordion__heading-3')
    answer_3_locator = (By.ID, 'accordion__panel-3')

    question_4_locator = (By.ID, 'accordion__heading-4')
    answer_4_locator = (By.ID, 'accordion__panel-4')

    question_5_locator = (By.ID, 'accordion__heading-5')
    answer_5_locator = (By.ID, 'accordion__panel-5')

    question_6_locator = (By.ID, 'accordion__heading-6')
    answer_6_locator = (By.ID, 'accordion__panel-6')

    question_7_locator = (By.ID, 'accordion__heading-7')
    answer_7_locator = (By.ID, 'accordion__panel-7')