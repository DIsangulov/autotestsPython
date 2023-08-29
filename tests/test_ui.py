import os
import time

import allure
import pytest

from pages.UI._0_Auth.auth_page import AuthPage
from pages.UI._2_Device_Management.devices import Devices
from pages.UI._2_Device_Management.element_type import ElementType
from pages.UI._3_Administration.system_config_man import SystemConfigMan
from pages.UI._6_Policy_Control.active_sessions import ActiveSessions
from pages.UI._6_Policy_Control.portal_functions import PortalFunctions
from pages.UI._6_Policy_Control.session_policy import SessionPolicy
from pages.UI._8_User_Management.users_page import UserDefinition
from pages.UI._8_User_Management.user_groups_page import UserGroupDefinition
from pages.UI._12_Logging.session_log import SessionLog
from pages.UI._2_Device_Management.device_groups import DeviceGroups

# ________ constants __________
# region
link = os.environ.get('TARGET_URL', "https://10.0.5.27")


# endregion
# ________ constants __________

@pytest.mark.skip
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


@pytest.mark.skip
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


@pytest.mark.skip
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


@pytest.mark.skip
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


@pytest.mark.skip
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
            step.click_play_session()  # тут надо конкретезировать что воспроизводить только определенные сессии
        with allure.step("Проверка что вопроизведение сессии запущенно"):
            step.should_play_session_run()


@pytest.mark.skip
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

    @allure.title("Группа правил - Добавление группы правил")
    def test_add_rules_group(self, browser):
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
        with allure.step("Переходим в Группы политик"):
            step.open_politic_group()
        with allure.step("Добавляем новое свойство группы политик"):
            step.add_policy_group_properties("test1")
        with allure.step("Удаляем новое свойство группы политик"):
            step.delete_policy_group_properties("test1")

    @allure.title("Область политики - Добавление области политики")
    def test_add_policy_area(self, browser):
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
        with allure.step("Переходим в Область политики"):
            step.open_politic_area()
        with allure.step("Добавляем новую область политики"):
            step.add_policy_area("test1")
        with allure.step("Удаляем новую область политики"):
            step.delete_policy_area("test1")

    @allure.title("Область политики - Добавление области политики")
    def test_add_policy_area(self, browser):
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
        with allure.step("Переходим в Область политики"):
            step.open_politic_area()
        with allure.step("Добавляем новую область политики"):
            step.add_policy_area("test1")
        with allure.step("Удаляем новую область политики"):
            step.delete_policy_area("test1")


@allure.suite("Базовая настройка Инфраскоп")
class TestBasicConfiguration:
    @allure.title("Авторизация, позитивный кейс")
    def test_valid_auth(self, browser):
        step = AuthPage(browser, link)
        with allure.step("Заходим на тестовый стенд"):
            step.open()
        with allure.step("Вводим корректные логин и пароль"):
            step.enter_as_user()
        with allure.step("Проверяем что авторизация прошла успешно"):
            step.should_enter_be_successful()

    @allure.title("Определение функциональной группы - Добавление функциональной группы")
    def test_defining_functional_group_adding_functional_group(self, browser):
        step = AuthPage(browser, link)
        with allure.step("Заходим на тестовый стенд"):
            step.open()
        with allure.step("Вводим корректные логин и пароль"):
            step.enter_as_user()
        step = PortalFunctions(browser, link)
        with allure.step("Переходим в Управление политиками -> Функции портала"):
            step.open_portal_functions()
        with allure.step("Переходим во вкладку Определение группы функций"):
            step.go_to_function_group_definition_tab()
        with allure.step("Добавляем новую функциональную группу"):
            step.add_new_function_group_definition("test1")
        with allure.step("Проверяем что группа добавлена"):
            step.should_new_function_group_definition_added("test1")
        # with allure.step("Удаляем созданную группу"):
        #     step.delete_new_function_group_definition_added("test1")

    @allure.title("Проверка создания области определения и разделения функции")
    def test_creating_scope_for_defining_and_separating_function(self, browser):
        step = AuthPage(browser, link)
        with allure.step("Заходим на тестовый стенд"):
            step.open()
        with allure.step("Вводим корректные логин и пароль"):
            step.enter_as_user()
        step = PortalFunctions(browser, link)
        with allure.step("Переходим в Управление политиками -> Функции портала"):
            step.open_portal_functions()
        with allure.step("Добавляем новую области определения и разделения функции"):
            step.add_new_area("test1")
        with allure.step("Проверяем что новая область добавлена"):
            step.should_new_area_added("test1")
        # with allure.step("Удаляем новую области определения и разделения функции"):
        #     step.delete_new_area("test1")

    # @pytest.mark.skip
    # @allure.title("Настройки системы - Создание менеджера конфигурации системы")
    # def test_creating_system_configuration_manager(self, browser):
    #     step = AuthPage(browser, link)
    #     with allure.step("Заходим на тестовый стенд"):
    #         step.open()
    #     with allure.step("Вводим корректные логин и пароль"):
    #         step.enter_as_user()
    #     step = SystemConfigMan(browser, link)
    #     with allure.step("Переходим в Администрирование -> Конфигурация системы"):
    #         step.open_system_config_man()
    #     with allure.step("Добавляем параметр otp.rest.url/http://127.0.0.1"):
    #         step.add_system_parameter_otp_rest_url()
    #     with allure.step("Добавляем параметр netright.auth.ldap/true"):
    #         step.add_system_parameter_netright_auth_ldap()
    #     with allure.step("Добавляем параметр sc.portal.otp.enabled/false"):
    #         step.add_system_parameter_sc_portal_otp_enabled()

    @allure.title("Редактирование группы пользователей, позитивный кейс")
    def test_edit_user_group(self, browser):
        step = AuthPage(browser, link)
        with allure.step("Заходим на тестовый стенд"):
            step.open()
        with allure.step("Вводим корректные логин и пароль"):
            step.enter_as_user()
        step = UserGroupDefinition(browser, link)
        with allure.step("Переходим на страницу 'Определение группы пользователей'"):
            step.open_user_group_definition()
        with allure.step("Поиск группы пользователей"):
            step.search_user_group("at_gp")
        with allure.step("Редактируем группу"):
            step.edit_user_group("at_gp", "_edit")
        with allure.step("Нажимаем сохранить"):
            step.click_save()
        with allure.step("Нажимаем подтвердить"):
            step.click_confirm()
        with allure.step("Поиск отредактированной группы"):
            step.search_user_group("_edit")
        with allure.step("Проверяем, что группа отредактирована успешно"):
            step.should_edit_user_group_be_successful("_edit")
        with allure.step("Поиск группы пользователей"):
            step.search_user_group("_edit")
        with allure.step("Редактируем группу в первоначальный вид"):
            step.edit_user_group("_edit", "at_gp")
        with allure.step("Нажимаем сохранить"):
            step.click_save()
        with allure.step("Нажимаем подтвердить"):
            step.click_confirm()

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
        # with allure.step("Кликаем ПКМ по созданной группе и нажимаем удалить"):
        #     step.delete_new_group("test1")

    @allure.title("Группы устройств - Добавление свойств")
    def test_device_group_add_property(self, browser):
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
        with allure.step("Клик ПКМ на название Группы устройств, открываем свойства"):
            step.open_device_properties('test1')
        with allure.step("Добавляем первое свойство"):
            step.add_properties_to_device_group('addAssignedCredentialToUserSelection', 'true')
        with allure.step("Добавляем второе свойство"):
            step.add_properties_to_device_group('addManualLoginToUserSelection', 'true')
        with allure.step("Проверяем что свойства добавлены"):
            step.should_device_group_properties_added('addAssignedCredentialToUserSelection',
                                                      'addManualLoginToUserSelection')

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

    @allure.title("Типы элементов - Добавление типа элемента")
    def test_add_device_types(self, browser):
        step = AuthPage(browser, link)
        with allure.step("Заходим на тестовый стенд"):
            step.open()
        with allure.step("Вводим корректные логин и пароль"):
            step.enter_as_user()
        step = ElementType(browser, link)
        with allure.step("Переходим в Управление устройствами -> Типы элементов"):
            step.open_element_type()
        with allure.step("Добавляем новый тип элемента"):
            step.add_element_type("test1")
        try:
            with allure.step("Нажимаем на Ок, если такой тип элементов уже существует"):
                step.click_ok_button()
                print("Данный тип элементов уже сужествует")
        except:
            pass
        with allure.step("Проверяем, что новый тип элемента добавлен"):
            step.should_element_type_added("test1")
        # with allure.step("Удаляем новый тип элемента"):
        #     step.delete_element_type("test1")

    @allure.title("Список устройств - Создание устройства")
    def test_creating_device(self, browser):
        step = AuthPage(browser, link)
        with allure.step("Заходим на тестовый стенд"):
            step.open()
        with allure.step("Вводим корректные логин и пароль"):
            step.enter_as_user()
        step = Devices(browser, link)
        with allure.step("Переходим в Управление устройствами -> Устройства"):
            step.open_devices(1)
        with allure.step("Переходим на вкладку 'Обнаружить новое устройство'"):
            step.open_new_device_discovery_tab()
        with allure.step("Вводим данные в область 'Обнаружить и добавить новое устройство' и сохраняем"):
            step.detect_and_add_new_device("test1")
        with allure.step("Проверяем подключение на новое устройство"):
            step.should_device_detected_and_added("test1")

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

    @allure.title("Группа правил - Добавление группы правил")
    def test_add_rules_group(self, browser):
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
        with allure.step("Переходим в Группы политик"):
            step.open_politic_group()
        with allure.step("Добавляем новое свойство группы политик"):
            step.add_policy_group_properties("test1")
        with allure.step("Удаляем новое свойство группы политик"):
            step.delete_policy_group_properties("test1")

    @allure.title("Область политики - Добавление области политики")
    def test_add_policy_area(self, browser):
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
        with allure.step("Переходим в Область политики"):
            step.open_politic_area()
        with allure.step("Добавляем новую область политики"):
            step.add_policy_area("test1")
        with allure.step("Удаляем новую область политики"):
            step.delete_policy_area("test1")

    @allure.title("Список устройств - Подключение к устройству SSH")
    def test_connect_to_SSH_device(self, browser):
        step = AuthPage(browser, link)
        with allure.step("Заходим на тестовый стенд"):
            step.open()
        with allure.step("Вводим корректные логин и пароль"):
            step.enter_as_user()
        step = SessionPolicy(browser, link)
        with allure.step("Переходим на страницу Управление политиками -> Политики сессий"):
            step.open_session_policy()
        with allure.step("Выполняем проверку что нужный ключ политики существует"):
            step.should_policy_key_added(".*", "Linux Server")
        step = Devices(browser, link)
        with allure.step("Переходим на страницу Управление устройствами -> Устройства"):
            step.open_devices(2)
        with allure.step("Раскрываем каталог SSH"):
            step.open_device_folder_by_name("SSH")
        with allure.step("Подключаемся к выбранному SSH устройству"):
            step.connect_to_device_ssh("SSH-10.0.5.42")

    @allure.title("Список устройств - Подключение к устройству RDP")
    def test_connect_to_RDP_device(self, browser):
        step = AuthPage(browser, link)
        with allure.step("Заходим на тестовый стенд"):
            step.open()
        with allure.step("Вводим корректные логин и пароль"):
            step.enter_as_user()
        step = SessionPolicy(browser, link)
        with allure.step("Переходим на страницу Управление политиками -> Политики сессий"):
            step.open_session_policy()
        with allure.step("Выполняем проверку что нужный ключ политики существует"):
            step.should_policy_key_added(".*", "Linux Server")
        step = Devices(browser, link)
        with allure.step("Переходим на страницу Управление устройствами -> Устройства"):
            step.open_devices(2)
        with allure.step("Раскрываем каталог RDP"):
            step.open_device_folder_by_name("RDP")
        with allure.step("Подключаемся к выбранному RDP устройству"):
            step.connect_to_device_rdp("TestRDP-10.0.5.188")

    @allure.title("Показ деталей при активной сессии")
    def test_showing_details_during_active_session(self, browser):
        step = AuthPage(browser, link)
        with allure.step("Заходим на тестовый стенд"):
            step.open()
        with allure.step("Вводим корректные логин и пароль"):
            step.enter_as_user()
        step = SessionPolicy(browser, link)
        with allure.step("Переходим на страницу Управление политиками -> Политики сессий"):
            step.open_session_policy()
        with allure.step("Выполняем проверку что нужный ключ политики существует"):
            step.should_policy_key_added(".*", "Linux Server")
        step = Devices(browser, link)
        with allure.step("Переходим на страницу Управление устройствами -> Устройства"):
            step.open_devices(2)
        with allure.step("Раскрываем каталог SSH"):
            step.open_device_folder_by_name("SSH")
        with allure.step("Подключаемся к выбранному SSH устройству и выполняем команнду pwd"):
            step.connect_to_device_ssh_for_check_active_session("SSH-10.0.5.42")
        step = ActiveSessions(browser, link)
        with allure.step("Переходим в Управление политиками -> Активные сессии"):
            step.open_active_sessions()
        with allure.step("Выполняем поиск и открываем детали активной SSH сессии и проверяем, что есть запись о выполненной команде pwd"):
            step.viewing_information_about_active_SSH_session()

    @allure.title("Воспроизведение активной сессии")
    def test_showing_session_during_active_session(self, browser):
        step = AuthPage(browser, link)
        with allure.step("Заходим на тестовый стенд"):
            step.open()
        with allure.step("Вводим корректные логин и пароль"):
            step.enter_as_user()
        step = SessionPolicy(browser, link)
        with allure.step("Переходим на страницу Управление политиками -> Политики сессий"):
            step.open_session_policy()
        with allure.step("Выполняем проверку что нужный ключ политики существует"):
            step.should_policy_key_added(".*", "Linux Server")
        step = Devices(browser, link)
        with allure.step("Переходим на страницу Управление устройствами -> Устройства"):
            step.open_devices(2)
        with allure.step("Раскрываем каталог SSH"):
            step.open_device_folder_by_name("SSH")
        with allure.step("Подключаемся к выбранному SSH устройству и выполняем команнду pwd"):
            step.connect_to_device_ssh_for_check_active_session("SSH-10.0.5.42")
        step = ActiveSessions(browser, link)
        with allure.step("Переходим в Управление политиками -> Активные сессии"):
            step.open_active_sessions()
        with allure.step("Воспроизводим сессию и убеждаемся что окно воспроизведения терминала открыто"):
            step.play_active_SSH_session()

    @allure.title("Подключение к активной сессии")
    def test_showing_session_during_active_session(self, browser):
        step = AuthPage(browser, link)
        with allure.step("Заходим на тестовый стенд"):
            step.open()
        with allure.step("Вводим корректные логин и пароль"):
            step.enter_as_user()
        step = SessionPolicy(browser, link)
        with allure.step("Переходим на страницу Управление политиками -> Политики сессий"):
            step.open_session_policy()
        with allure.step("Выполняем проверку что нужный ключ политики существует"):
            step.should_policy_key_added(".*", "Linux Server")
        step = Devices(browser, link)
        with allure.step("Переходим на страницу Управление устройствами -> Устройства"):
            step.open_devices(2)
        with allure.step("Раскрываем каталог SSH"):
            step.open_device_folder_by_name("SSH")
        with allure.step("Подключаемся к выбранному SSH устройству и выполняем команнду pwd"):
            step.connect_to_device_ssh_for_check_active_session("SSH-10.0.5.42")
        step = ActiveSessions(browser, link)
        with allure.step("Переходим в Управление политиками -> Активные сессии"):
            step.open_active_sessions()
        with allure.step("Подключаемся к активной сессии и передаем в терминал команду pwd"):
            step.connect_to_active_SSH_session()

    @allure.title("Отправка сообщения в активную сессию")
    def test_showing_session_during_active_session(self, browser):
        step = AuthPage(browser, link)
        with allure.step("Заходим на тестовый стенд"):
            step.open()
        with allure.step("Вводим корректные логин и пароль"):
            step.enter_as_user()
        step = SessionPolicy(browser, link)
        with allure.step("Переходим на страницу Управление политиками -> Политики сессий"):
            step.open_session_policy()
        with allure.step("Выполняем проверку что нужный ключ политики существует"):
            step.should_policy_key_added(".*", "Linux Server")
        step = Devices(browser, link)
        with allure.step("Переходим на страницу Управление устройствами -> Устройства"):
            step.open_devices(2)
        with allure.step("Раскрываем каталог SSH"):
            step.open_device_folder_by_name("SSH")
        with allure.step("Подключаемся к выбранному SSH устройству и выполняем команнду pwd"):
            step.connect_to_device_ssh_for_check_active_session("SSH-10.0.5.42")
        step = ActiveSessions(browser, link)
        with allure.step("Переходим в Управление политиками -> Активные сессии"):
            step.open_active_sessions()
        with allure.step("Выбираем активную сессию и отправляем в нее сообщение и проверяем что сообщение успешно отправлено"):
            step.send_message_to_active_SSH_session()

    @allure.title("Завершение активной сессии")
    def test_showing_session_during_active_session(self, browser):
        step = AuthPage(browser, link)
        with allure.step("Заходим на тестовый стенд"):
            step.open()
        with allure.step("Вводим корректные логин и пароль"):
            step.enter_as_user()
        step = SessionPolicy(browser, link)
        with allure.step("Переходим на страницу Управление политиками -> Политики сессий"):
            step.open_session_policy()
        with allure.step("Выполняем проверку что нужный ключ политики существует"):
            step.should_policy_key_added(".*", "Linux Server")
        step = Devices(browser, link)
        with allure.step("Переходим на страницу Управление устройствами -> Устройства"):
            step.open_devices(2)
        with allure.step("Раскрываем каталог SSH"):
            step.open_device_folder_by_name("SSH")
        with allure.step("Подключаемся к выбранному SSH устройству и выполняем команнду pwd"):
            step.connect_to_device_ssh_for_check_active_session("SSH-10.0.5.42")
        step = ActiveSessions(browser, link)
        with allure.step("Переходим в Управление политиками -> Активные сессии"):
            step.open_active_sessions()
        with allure.step("Выбираем активную сессию и завершаем ее"):
            step.close_active_SSH_session()