import os

import allure

from pages.UI.Auth.auth_page import AuthPage

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

    @allure.title("Авторизация, позитивный кейс")
    def test_logout(self, browser):
        step = AuthPage(browser, link)
        with allure.step("Нажимаем на кнопку Выход"):
            step.log_out()
        with allure.step("Выход произведен успешно"):
            step.shold_log_out_be_successful()



