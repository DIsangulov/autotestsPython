import time

from pages.Helpers.base_page import BasePage
from resources.locators import AuthLocators, MainLocators

login = 'admin'
password = '1q2w3e4r5t'


class AuthPage(BasePage):

    def enter_as_user(self):
        self.page.fill(AuthLocators.LOGIN_INPUT, login)
        self.page.fill(AuthLocators.PAS_INPUT, password)
        self.page.click(AuthLocators.ENTER_BUT)
        self.page.click(MainLocators.RUS_BUTTON)

    def should_enter_be_successful(self):
        assert self.page.wait_for_selector(MainLocators.LOGO_LEFT).is_visible()

    def log_out(self):
        self.page.click(AuthLocators.LOGOUT)

    def shold_log_out_be_successful(self):
        assert self.page.wait_for_selector(MainLocators.LOGO_ON_AYTH_PAGE).is_visible()


