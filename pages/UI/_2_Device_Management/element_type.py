import time

from pages.Helpers.base_page import BasePage
from resources.locators import MainLocators, DeviceManagement, LoggingLocators


class ElementType(BasePage):

    def open_element_type(self):
        self.page.get_by_text("Управление устройствами").click()
        self.page.get_by_text("Типы элементов").click()

    def add_element_type(self, name):
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(
            "//label[contains(text(), 'ID типа элемента:')]/following::input[1]").fill(name)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(
            "//label[contains(text(), 'Название типа элемента:')]/following::input[1]").fill(name)
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Сохранить").click()

    def click_ok_button(self):
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.OK_BUTTON).click()

    def delete_element_type(self, name):
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Очистить").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(
            "//label[contains(text(), 'ID типа элемента:')]/following::input[1]").fill(name)
        time.sleep(2)
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Поиск").nth(0).click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("//div[contains(text(), '" + name +"')]/preceding::button[1]").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Удалить тип элемента").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.YES_BUTTON).click()

    def should_element_type_added(self, name):
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Очистить").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(
            "//label[contains(text(), 'ID типа элемента:')]/following::input[1]").fill(name)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.SEARCH_BUTTON).click()
        time.sleep(1)
        assert self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text(name).nth(0).is_visible()

