import time

from pages.Helpers.base_page import BasePage
from resources.locators import MainLocators


class ActiveSessions(BasePage):

    def open_active_sessions(self):
        self.page.get_by_text("Управление политиками").click()
        self.page.locator("(//*[text()='Активные сессии'])[1]").click()

    def viewing_information_about_active_SSH_session(self):
        self.page.frame_locator(MainLocators.MAIN_FRAME).nth(2).get_by_text("Поиск").nth(1).click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).nth(2).locator("(//div[contains(text(), 'SSH')]/preceding::button[1])[2]").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).nth(2).get_by_text("Показать детали").click()
        time.sleep(2)
        assert self.page.frame_locator(MainLocators.MAIN_FRAME).nth(2).locator("//*[text()='pwd']").is_visible()

    def play_active_SSH_session(self):
        self.page.frame_locator(MainLocators.MAIN_FRAME).nth(2).get_by_text("Поиск").nth(1).click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).nth(2).locator("(//div[contains(text(), 'SSH')]/preceding::button[1])[2]").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).nth(2).get_by_text("Воспроизвести сессию").click()
        time.sleep(5)
        with self.page.context.expect_page() as window:
            new_window = window.value
            assert new_window.locator("#terminal-container").is_visible()

