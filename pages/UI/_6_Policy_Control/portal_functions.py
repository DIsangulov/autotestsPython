import time

from pages.Helpers.base_page import BasePage
from resources.locators import MainLocators


class PortalFunctions(BasePage):
    def open_portal_functions(self):
        self.page.get_by_text("Управление политиками").click()
        self.page.get_by_text("Функции портала").click()

    def add_new_area(self, area_name):
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("#x-auto-54-input").fill(area_name)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("#x-auto-74-input").fill(area_name)
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Administration").nth(0).click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("#x-auto-64").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Policy Control").nth(0).click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("#x-auto-64").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Device Management").nth(0).click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("#x-auto-64").click()
        self.delay_input(MainLocators.MAIN_FRAME, "#x-auto-75-input", "test_group")
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(
            "(//button[@class='x-btn-text' and @type='button'])[2]").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.SAVE_BUTTON).click()

    def should_new_area_added(self, area_name):
        assert self.page.get_by_text(area_name).is_visible()

    def delete_new_area(self, area_name):
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Очистить").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("#x-auto-54-input").fill(area_name)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.SEARCH_BUTTON).click()
        time.sleep(2)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(
            "(//button[@class='x-btn-text' and @type='button'])[6]").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.YES_BUTTON).click()
