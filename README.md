# Sprint 6
## Описание

Этот проект предназначен для автоматизации тестирования веб-приложения. Он использует Selenium WebDriver для выполнения тестов и Allure для генерации отчетов о тестировании.

## Структура проекта

Проект имеет следующую структуру:


- **Locators/**: Папка содержит файлы с локаторами элементов на страницах.
  - `base_page_locators.py`: Локаторы для общих элементов на страницах.
  - `main_page_locators.py`: Локаторы для элементов главной страницы.
  - `order_page_locators.py`: Локаторы для элементов страницы с заказами.

- **Page_Object/**: Папка содержит файлы с Page Object моделями для взаимодействия с элементами страниц.
  - `base_page.py`: Методы для работы с элементами, общие для других страниц.
  - `main_page.py`: Методы для работы с элементами главной страницы.
  - `order_page.py`: Методы для работы с элементами страницы с заказами.

- **tests/**: Папка содержит тесты для различных функциональных областей.
  - `test_click_logo.py`: Тест для проверки перехода по логотипам Яндекс и Самокат.
  - `test_answers_main_page.py`: Тест для проверки текста ответов на вопросы в блоке "Вопросы о важном".
  - `test_order_scooter.py`: Тестирование функционала заказа самоката.

- **conftest.py**: Файл с фикстурами для настройки и очистки тестов.

- **data/**: Папка содержит файлы с данными для тестов.
  - `data.py`: Данные для тестов, такие как URL и ожидаемые ответы.

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone <URL вашего репозитория>
   cd <название репозитория>
2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Windows используйте venv\Scripts\activate
3. Установите необходимые зависимости:
    ```bash
   pip install -r requirements.txt

## Запуск тестов

Для запуска тестов используйте команду:

```bash
pytest --alluredir=allure-results
allure serve allure-results
    