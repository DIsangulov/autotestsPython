import os
import time

import allure
import pytest

from pages.UI._0_Auth.auth_page import AuthPage
from pages.UI._12_Logging.session_log import SessionLog

# ________ constants __________
# region
link = os.environ.get('TARGET_URL', "https://10.0.5.27")


# endregion
# ________ constants __________

@allure.suite("Страница авторизации")
class TestAuth:
    @allure.title("Авторизация, позитивный кейс")
    def test_valid_auth(self, browser):
        step = AuthPage(browser, link)
        with allure.step("Заходим на тестовый стенд"):
            step.open()
        with allure.step("Вводим корректные логин и пароль"):
            step.enter_as_user()
        with allure.step("Проверяем что авторизация прошла успешно"):
            step.should_enter_be_successful()

    @allure.title("Выход из системы")
    def test_logout(self, browser):
        step = AuthPage(browser, link)
        with allure.step("Заходим на тестовый стенд"):
            step.open()
        with allure.step("Вводим корректные логин и пароль"):
            step.enter_as_user()
        with allure.step("Проверяем что авторизация прошла успешно"):
            step.should_enter_be_successful()
        with allure.step("Нажимаем на кнопку Выход"):
            step.log_out()
        with allure.step("Выход произведен успешно"):
            step.shold_log_out_be_successful()


@allure.suite("Сценарные проверки по ПиМИ")
class TestScenariosPimi:
    @allure.title("Проверка показа деталей")
    def test_checking_details(self, browser):
        step = AuthPage(browser, link)
        with allure.step("Заходим на тестовый стенд"):
            step.open()
        with allure.step("Вводим корректные логин и пароль"):
            step.enter_as_user()
        step = SessionLog(browser, link)
        with allure.step("Переходим в Логирование -> Лог сессии"):
            step.open_session_log()
        with allure.step("Вводим дату начала поиска 01.01.2023"):
            step.enter_date_data("01.01.2023")
        with allure.step("Нажимаем на кнопку Поиск"):
            step.click_search()
        with allure.step("Нажимаем на Опции -> Показать детали"):
            step.click_sessions_details()
        with allure.step("Проверяем что Детали команды содержат информацию"):
            step.should_session_log_be_successful()

    @allure.title("Проверка воспроизведения сесии")
    def test_play_session(self, browser):
        step = AuthPage(browser, link)
        with allure.step("Заходим на тестовый стенд"):
            step.open()
        with allure.step("Вводим корректные логин и пароль"):
            step.enter_as_user()
        step = SessionLog(browser, link)
        with allure.step("Переходим в Логирование -> Лог сессии"):
            step.open_session_log()
        with allure.step("Вводим дату начала поиска 01.01.2023"):
            step.enter_date_data("01.01.2023")
        with allure.step("Нажимаем на кнопку Поиск"):
            step.click_search()
        with allure.step("Нажимаем на Опции -> Воспроизвести сессию"):
            step.click_play_session()
        with allure.step("Проверка что вопроизведение сессии запущенно"):
            step.should_play_session_run()
