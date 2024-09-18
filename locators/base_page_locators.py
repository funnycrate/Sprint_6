from selenium.webdriver.common.by import By

class BasePageLocators:
    logo_samokat = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')  # Используем кортеж, а не список
    logo_yandex = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
    order_button_upper = (By.CLASS_NAME, 'Button_Button__ra12g')  # Исправлена точка на запятую
    header_page_title = (By.XPATH, ".//div[text() = 'Учебный тренажер']")