import os
import time

import allure
import pytest

from pages.UI._0_Auth.auth_page import AuthPage
from pages.UI._8_User_Management.users_page import UserDefinition
from pages.UI._8_User_Management.user_groups_page import UserGroupDefinition

# ________ constants __________
# region
link = os.environ.get('TARGET_URL', "https://10.0.5.27")


# endregion
# ________ constants __________

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


@allure.suite("Страница 'Определение группы пользователей'")
class TestUserGroup:
    @allure.title("Создание группы пользователей, позитивный кейс")
    def test_create_user_group(self, browser):
        step = AuthPage(browser, link)
        with allure.step("Заходим на тестовый стенд"):
            step.open()
        with allure.step("Вводим корректные логин и пароль"):
            step.enter_as_user()
        step = UserGroupDefinition(browser, link)
        with allure.step("Переходим на страницу 'Определение группы пользователей'"):
            step.open_user_group_definition()
        with allure.step("Вводим корректные данные"):
            step.enter_user_group("at_gp", "autotest_user", "at")
        with allure.step("Нажимаем сохранить"):
            step.click_save()
        with allure.step("Нажимаем подтвердить"):
            step.click_confirm()
        with allure.step("Поиск созданной группы"):
            step.search_user_group("at_gp")
        with allure.step("Проверяем, что группа создана успешно"):
            step.should_create_user_group_be_successful("at_gp")


@allure.suite("Страница 'Определение пользователя'")
class TestDeleteUser:
    @allure.title("Удаление пользователя, позитивный кейс")
    def test_delete_user(self, browser):
        step = AuthPage(browser, link)
        with allure.step("Заходим на тестовый стенд"):
            step.open()
        with allure.step("Вводим корректные логин и пароль"):
            step.enter_as_user()
        step = UserDefinition(browser, link)
        with allure.step("Переходим на страницу 'Определение пользователя'"):
            step.open_user_definition()
        with allure.step("Поиск пользователя"):
            step.search_user("autotest_user")
        with allure.step("Удаляем пользователя"):
            step.delete_user()
        with allure.step("Проверяем, что пользователь удален"):
            step.should_delete_user_be_successful("autotest_user")


