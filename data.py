from locators.base_page_locators import *
from locators.order_page_locators import *
from locators.main_page_locators import *

class Urls:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/'
    DZEN_URL = 'https://dzen.ru/?yredirect=true'
    ORDER_URL = 'https://qa-scooter.praktikum-services.ru/order'


class UserData:
    user_1 = {
        'button': BasePageLocators.order_button_upper,
        'first_name': 'Иван',
        'last_name': 'Иванов',
        'address': 'Москва, ул. Льва Толстого, д. 16',
        'metro': 'Преображенская площадь',
        'telephone': '89000000001',
        'calendar': '15.09.2024',
        'rental': OrderPageLocators.four_day_rental,
        'color': OrderPageLocators.black_color_checkbox,
        'comment': 'Комментарий user_1'
    }

    user_2 = {
        'button': MainPageLocators.button_order_middle,
        'first_name': 'Петр',
        'last_name': 'Андреев',
        'address': 'Москва, ул. Арбат, д. 26',
        'metro': 'Преображенская площадь',
        'telephone': '89000000002',
        'calendar': '14.09.2024',
        'rental': OrderPageLocators.one_day_rental,
        'color': OrderPageLocators.grey_color_checkbox,
        'comment': 'Комментарий user_2'
    }

class Answers:
    expected_answers = {
            0: "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
            1: "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
            2: "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
            3: "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
            4: "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
            5: "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
            6: "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
            7: "Да, обязательно. Всем самокатов! И Москве, и Московской области."
        }