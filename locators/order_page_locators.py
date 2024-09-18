from selenium.webdriver.common.by import By


class OrderPageLocators:
    """Страница заказа, первая часть"""
    first_name_place = [By.XPATH, "//input[@placeholder='* Имя']"]
    second_name_place = (By.XPATH, "//input[@placeholder='* Фамилия']")
    address_place = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    metro_place = (By.XPATH, "//input[@placeholder='* Станция метро']")
    metro_wtf = (By.XPATH, ".//div[text() = 'Преображенская площадь']")
    telephone_place = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    next_button = (By.XPATH, "//button[text()='Далее']")

    """Страница заказа, вторая часть"""
    when_to_bring_place = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    rental_period_place = (By.XPATH, ".//span[@class='Dropdown-arrow']")
    one_day_rental = (By.XPATH, "//div[text()='сутки']")
    two_day_rental = (By.XPATH, "//div[@class='Dropdown-option' and text()='двое суток']")
    three_day_rental = (By.XPATH, "//div[@class='Dropdown-option' and text()='трое суток']")
    four_day_rental = (By.XPATH, "//div[@class='Dropdown-option' and text()='четверо суток']")
    five_day_rental = (By.XPATH, "//div[@class='Dropdown-option' and text()='пятеро суток']")
    six_day_rental = (By.XPATH, "//div[@class='Dropdown-option' and text()='шестеро суток']")
    seven_day_rental = (By.XPATH, "//div[@class='Dropdown-option' and text()='семеро суток']")
    black_color_checkbox = (By.XPATH, "//input[@id='black']")
    grey_color_checkbox = (By.XPATH, "//input[@id='grey']")
    comment_place = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    backspace_button = (By.XPATH, "//button[text()='Назад']")
    order_button = (By.XPATH, "(//button[contains(@class, 'Button_') and text()='Заказать'])[2]")
    no_button = (By.XPATH, "//button[text()='Нет']")
    yes_button = (By.XPATH, "//button[text()='Да']")
    show_status_button = (By.XPATH, "//button[text()='Посмотреть статус']")
    show_status_text = (By.XPATH, "(//div[contains(@class, 'Order_ModalHeader_') and text()='Заказ оформлен'])")