import os

import allure

from pages.UI.Auth.auth_page import AuthPage
from pages.UI._8_User_Management.User_Defition_page import UserDefinition

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
        with allure.step("Нажимаем на кнопку Выход"):
            step.log_out()
        with allure.step("Выход произведен успешно"):
            step.shold_log_out_be_successful()


@allure.suite("Страница 'Определение пользователя'")
class TestUser:
    @allure.title("Создание пользователя, позитивный кейс")
    def test_create_user(self, browser):
        step = AuthPage(browser, link)
        with allure.step("Заходим на тестовый стенд"):
            step.open()
        with allure.step("Вводим корректные логин и пароль"):
            step.enter_as_user()
        step = UserDefinition(browser, link)
        with allure.step("Переходим на страницу 'Определение пользователя'"):
            step.open_user_definition()
        with allure.step("Вводим корректные данные"):
            step.enter_user("autotest_user", "1", "qwerty", "qwerty", "autotest", "autotest", "autotest@test.com",
                        "89999999999")
        with allure.step("Нажимаем сохранить"):
            step.click_save()
        with allure.step("Поиск созданного пользователя"):
            step.search_user("autotest_user")
        with allure.step("Проверяем, что пользователь создан успешно"):
            step.should_create_user_be_successful("autotest_user")

