import time

from pages.Helpers.base_page import BasePage
from resources.locators import MainLocators, DeviceManagement, LoggingLocators


class Devices(BasePage):

    def open_devices(self):
        self.page.get_by_text("Управление устройствами").click()
        self.page.get_by_text("Устройства").click()

