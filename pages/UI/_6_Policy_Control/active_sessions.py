import time

from pages.Helpers.base_page import BasePage
from resources.locators import MainLocators


class ActiveSessions(BasePage):

    def open_active_sessions(self):
        self.page.get_by_text("Управление политиками").click()
        self.page.get_by_text("Активные сессии").click()