import time

from pages.Helpers.base_page import BasePage
from resources.locators import LoggingLocators, MainLocators


class SessionPolicy(BasePage):
    def open_session_policy(self):
        self.page.get_by_text("Управление политиками").click()
        self.page.get_by_text("Политики сессий").click()

    def add_new_policy_key(self, key_name):
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("#x-auto-183-input").fill(key_name)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("#x-auto-156-input").fill("description")
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



