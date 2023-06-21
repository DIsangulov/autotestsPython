import time

from pages.Helpers.base_page import BasePage
from resources.locators import MainLocators, DeviceManagement


class DeviceGroups(BasePage):

    def open_device_groups(self):
        self.page.get_by_text("Управление устройствами").click()
        self.page.get_by_text("Группы устройств").click()

    def add_new_group(self, group_name):
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(DeviceManagement.GROUP_NAME).fill(group_name)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.SAVE_BUTTON).click()
        time.sleep(1)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.REFRESH_PAGE).click()

    def delete_new_group(self, group_name):
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text(group_name).nth(0).click(button='right')
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Удалить группу устройств").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.YES_BUTTON).click()

