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
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Очистить").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("#x-auto-54-input").fill(area_name)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.SEARCH_BUTTON).click()
        time.sleep(2)
        assert self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text(area_name).nth(2).is_visible()

    def delete_new_area(self, area_name):
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Очистить").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("#x-auto-54-input").fill(area_name)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.SEARCH_BUTTON).click()
        time.sleep(2)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(
            "(//button[@class='x-btn-text' and @type='button'])[6]").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.YES_BUTTON).click()

    def go_to_function_group_definition_tab(self):
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Определение группы функций").click()

    def add_new_function_group_definition(self, group_name):
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("#x-auto-206-input").fill(group_name)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("#x-auto-207-input").fill(group_name)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("#x-auto-216").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.SAVE_BUTTON).click()

    def should_new_function_group_definition_added(self, group_name):
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Очистить").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("#x-auto-206-input").fill(group_name)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.SEARCH_BUTTON).click()
        time.sleep(3)
        assert self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text(group_name).nth(0).is_visible()

    def delete_new_function_group_definition_added(self, group_name):
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Очистить").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("#x-auto-195-input").fill(group_name)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.SEARCH_BUTTON).click()
        time.sleep(3)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("//div[contains(text(), 'test1')]/preceding::button[1]").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.YES_BUTTON).click()





