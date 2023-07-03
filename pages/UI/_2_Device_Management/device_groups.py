import time

from pages.Helpers.base_page import BasePage
from resources.locators import MainLocators, DeviceManagement, LoggingLocators


class DeviceGroups(BasePage):

    def open_device_groups(self):
        self.page.get_by_text("Управление устройствами").click()
        self.page.get_by_text("Группы устройств").click()

    def add_new_group(self, group_name):
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(DeviceManagement.GROUP_NAME).fill(group_name)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.SAVE_BUTTON).click()
        time.sleep(1)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.REFRESH_PAGE).click()

    def click_ok_button(self):
        # self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Ok").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("//button[@class='x-btn-text ' and text()='Ok']").click()

    def delete_new_group(self, group_name):
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text(group_name).nth(0).click(button='right')
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Удалить группу устройств").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.YES_BUTTON).click()

    def device_group_realms(self):
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Области групп устройств").click()

    def add_new_area(self, area_name):
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(DeviceManagement.NAME_AREA_DEVICES).fill(area_name)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(DeviceManagement.DESCRIPTION_AREA_DEVICES).fill("description")
        self.delay_input(MainLocators.MAIN_FRAME, DeviceManagement.CHOICE_GROUP_DEVICES, "RDP")
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("//*[text()='RDP']").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(DeviceManagement.ADD_GROUP_DEVICES_BUTTON).click()
        self.delay_input(MainLocators.MAIN_FRAME, DeviceManagement.CHOICE_GROUP_DEVICES, "SSH")
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("//*[text()='SSH']").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(DeviceManagement.ADD_GROUP_DEVICES_BUTTON).click()
        self.delay_input(MainLocators.MAIN_FRAME, DeviceManagement.CHOICE_GROUP_DEVICES, "HTTP")
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("//*[text()='HTTP']").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(DeviceManagement.ADD_GROUP_DEVICES_BUTTON).click()
        self.delay_input(MainLocators.MAIN_FRAME, DeviceManagement.CHOICE_GROUP_USERS, "test_group")
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(DeviceManagement.ADD_GROUP_USERS_BUTTON).click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.SAVE_BUTTON).click()


    def should_new_area_added(self, area_name):
        assert self.page.frame_locator(MainLocators.MAIN_FRAME).locator("//*[text()='"+area_name+"']"), "Новая добавленная область не появилась"

    def delete_new_area(self, area_name):
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.CLEAR_BUTTON).click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(DeviceManagement.NAME_AREA_DEVICES).fill(area_name)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.SEARCH_BUTTON).click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(LoggingLocators.SESSION_OPTIONS).click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Удалить").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.YES_BUTTON).click()




