import os
import time

import allure
import pytest

from pages.UI._0_Auth.auth_page import AuthPage
from pages.UI._13_SAPM_Management.sapm_management import SapmManagement
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


@allure.suite("Базовая настройка Инфраскоп")
class TestBasicConfiguration:

    @allure.title("Подключение по ssh для создания SAPM аккаунта")
    def test_ssh_send_command(self, ssh):
        ssh.ssh_send_command('sudo -s')
        ssh.ssh_send_command('adduser sapm')
        ssh.ssh_send_command('passwd sapm')

    @allure.title("Создание SAPM аккаунта")
    def test_create_sapm_account(self, browser):

        step = AuthPage(browser, link)
        with allure.step("Заходим на тестовый стенд"):
            step.open()
        with allure.step("Вводим корректные логин и пароль"):
            step.enter_as_user()
        step = SapmManagement(browser, link)
        with allure.step("Переходим на страницу Управление SAPM -> SAPM"):
            step.open_sapm_management()
        time.sleep(3)
