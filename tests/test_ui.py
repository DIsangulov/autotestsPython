import os
import time

import allure
import pytest

from pages.UI._0_Auth.auth_page import AuthPage
from pages.UI._6_Policy_Control.session_policy import SessionPolicy
from pages.UI._8_User_Management.users_page import UserDefinition
from pages.UI._12_Logging.session_log import SessionLog
from pages.UI._2_Device_Management.device_groups import DeviceGroups

# ________ constants __________
# region
link = os.environ.get('TARGET_URL', "https://10.0.5.27")


# endregion
# ________ constants __________

@allure.suite("Проверка доступности веб-интерфейса")
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


@allure.suite("Настройка политик устройств")
class TestConfiguringDevicePolicies:
    @allure.title("Группы устройств - Создание группы устройств")
    def test_creating_device_group(self, browser):
        step = AuthPage(browser, link)
        with allure.step("Заходим на тестовый стенд"):
            step.open()
        with allure.step("Вводим корректные логин и пароль"):
            step.enter_as_user()
        with allure.step("Проверяем что авторизация прошла успешно"):
            step.should_enter_be_successful()
        step = DeviceGroups(browser, link)
        with allure.step("Переходим в Управление устройствами -> Группы устройств"):
            step.open_device_groups()
        try:
            with allure.step("Добавляем новую группу"):
                step.add_new_group("test1")
        except:
            with allure.step("Нажимаем Ok"):
                step.click_ok_button()
            print("Группа устройств уже существует")
        with allure.step("Кликаем ПКМ по созданной группе и нажимаем удалить"):
            step.delete_new_group("test1")

    @allure.title("Область групп устройств - Создание области")
    def test_creating_area(self, browser):
        step = AuthPage(browser, link)
        with allure.step("Заходим на тестовый стенд"):
            step.open()
        with allure.step("Вводим корректные логин и пароль"):
            step.enter_as_user()
        with allure.step("Проверяем что авторизация прошла успешно"):
            step.should_enter_be_successful()
        step = DeviceGroups(browser, link)
        with allure.step("Переходим в Управление устройствами -> Группы устройств"):
            step.open_device_groups()
        with allure.step("Переходим в Области групп устройств"):
            step.device_group_realms()
        with allure.step("Добавляем новую Область устройств"):
            step.add_new_area("test1")
        try:
            with allure.step("Нажимаем Ok"):
                step.click_ok_button()
            # with allure.step("Проверка что новая область добавлена"):
            #     step.should_new_area_added("test1")
        except:
            print("Область устройств устройств уже существует")
        try:
            with allure.step("Удаление добавленной области"):
                step.delete_new_area("test1")
        except:
            print("Удаление добавленной области не произошло")

    @allure.title("Ключ правил - Добавление ключа правил")
    def test_add_rules_key(self, browser):
        step = AuthPage(browser, link)
        with allure.step("Заходим на тестовый стенд"):
            step.open()
        with allure.step("Вводим корректные логин и пароль"):
            step.enter_as_user()
        with allure.step("Проверяем что авторизация прошла успешно"):
            step.should_enter_be_successful()
        step = SessionPolicy(browser, link)
        with allure.step("Переходим в Управление политиками -> Политики сессий"):
            step.open_session_policy()
        with allure.step("Добавляем новый ключ политики"):
            step.add_new_policy_key(".*")
        with allure.step("Удаляем новый ключ политики"):
            step.delete_new_policy_key(".*")
