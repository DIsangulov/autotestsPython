import time

from playwright.sync_api import Frame

from pages.Helpers.base_page import BasePage
from resources.locators import MainLocators


class SessionPolicy(BasePage):
    def open_session_policy(self):
        self.page.get_by_text("Управление политиками").click()
        self.page.get_by_text("Политики сессий").click()

    def click_ok_button(self):
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.OK_BUTTON).click()

    def add_new_policy_key(self, key_name):
        self.input_text_field("Ключ политики:", key_name)
        self.input_text_field("Описание", key_name)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("#x-auto-157-input").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("разрешенная команда").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Linux Server").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.SHIFT_RIGHT_BUTTON).click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Windows").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.SHIFT_RIGHT_BUTTON).click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("HTTP").nth(1).click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.SHIFT_RIGHT_BUTTON).click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.SAVE_BUTTON).click()

    def delete_new_policy_key(self, key_name):
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("#x-auto-183-input").fill(key_name)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.SEARCH_BUTTON).click()
        time.sleep(3)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("(//button[@class='x-btn-text'])[5]").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.YES_BUTTON).click()

    def open_politic_group(self):
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Группа политик").click()

    def open_politic_area(self):
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Область политики").click()

    def add_policy_group_properties(self, policy_name):
        self.input_text_field("Имя политики:", policy_name)
        self.input_text_field("Описание:", policy_name)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("#x-auto-236-input").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("OPERATION").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text(".* - разрешенная команда").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("#x-auto-249").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("#x-auto-258").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Generate Error").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.SAVE_BUTTON).click()

    def delete_policy_group_properties(self, policy_name):
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Очистить").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("#x-auto-234-input").fill(policy_name)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.SEARCH_BUTTON).click()
        time.sleep(3)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("(//button[@class='x-btn-text'])[3]").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Удалить").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.YES_BUTTON).click()

    def add_policy_area(self, area_name):
        self.input_text_field("Имя области:", area_name)
        self.input_text_field("Описание:", area_name)
        self.input_text_field("Область(и) устройств:", "all")
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("all").nth(0).click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("#x-auto-265").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.SAVE_BUTTON).click()

    def delete_policy_area(self, area_name):
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Очистить").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("#x-auto-234-input").fill(area_name)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.SEARCH_BUTTON).click()
        time.sleep(3)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("//span[contains(text(), '"+area_name+"')]/preceding::button[1]").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.YES_BUTTON).click()

    def should_policy_key_added(self, key_name, element_type):  # здесь подставляем ключ и тип необходимого элемента для проверки
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Очистить").click()
        self.input_text_field("Ключ политики:", key_name)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.SEARCH_BUTTON).click()
        time.sleep(1)
        assert self.page.frame_locator(MainLocators.MAIN_FRAME).locator("(//span[contains(text(), '"+key_name+"')]/following::span[contains(text(), '"+element_type+"')])[1]").is_visible()











