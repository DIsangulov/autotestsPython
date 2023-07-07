import time

from pages.Helpers.base_page import BasePage
from resources.locators import MainLocators


class SystemConfigMan(BasePage):
    def open_system_config_man(self):
        self.page.get_by_text("Администрирование").click()
        self.page.get_by_text("Конфигур. системы").click()

    def add_system_parameter_otp_rest_url(self):
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("#x-auto-79-input").fill("otp.rest.url")
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("#x-auto-80-input").fill("http://127.0.0.1")
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.SAVE_BUTTON).click()

    def add_system_parameter_netright_auth_ldap(self):
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("#x-auto-79-input").fill("netright.auth.ldap")
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("#x-auto-80-input").fill("true")
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.SAVE_BUTTON).click()

    def add_system_parameter_sc_portal_otp_enabled(self):
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("#x-auto-79-input").fill("sc.portal.otp.enabled")
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("#x-auto-80-input").fill("false")
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.SAVE_BUTTON).click()
