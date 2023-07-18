import os
import time

import allure
import pytest

from pages.UI._0_Auth.auth_page import AuthPage
from pages.UI._3_Administration.system_config_man import SystemConfigMan
from pages.UI._6_Policy_Control.portal_functions import PortalFunctions
from pages.UI._6_Policy_Control.session_policy import SessionPolicy
from pages.UI._8_User_Management.users_page import UserDefinition
from pages.UI._8_User_Management.user_groups_page import UserGroupDefinition

# ________ constants __________
# region
link = os.environ.get('TARGET_URL', "https://10.0.5.27")


# endregion
# ________ constants __________
@allure.suite("Страница 'Определение группы пользователей'")
class TestUserGroup:
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
            step.edit_user_group("_edit")
        with allure.step("Нажимаем сохранить"):
            step.click_save()
        with allure.step("Нажимаем подтвердить"):
            step.click_confirm()
        with allure.step("Поиск отредактированной группы"):
            step.search_user_group("_edit")
        with allure.step("Проверяем, что группа отредактирована успешно"):
            step.should_edit_user_group_be_successful("_edit")
