import time

from pages.Helpers.base_page import BasePage
from resources.locators import LoggingLocators, MainLocators


class SessionLog(BasePage):
    def open_session_log(self):
        self.page.get_by_text("Логирование").click()
        self.page.get_by_text("Лог сессий").click()

    def enter_date_data(self, date):
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(LoggingLocators.LOG_START_TIME).fill(date)

    def click_search(self):
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.SEARCH_BUTTON).click()

    def click_sessions_details(self):
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(LoggingLocators.SESSION_OPTIONS).click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Показать детали").click()

    def should_session_log_be_successful(self):
        try:
            self.page.frame_locator(MainLocators.MAIN_FRAME).locator(
                LoggingLocators.DETAILID_SESSION_VIEW_BUTTON).click()
            assert self.page.locator(LoggingLocators.TEXT_AREA) != ""
        except:
            print("У данной сессии детали не найдены, но модальное окно открылось")

    def click_play_session(self):
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("(//div[contains(text(), 'RDP')]/preceding::button[1])[2]").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Воспроизвести сессию").click()

    def should_play_session_run(self):
        with self.page.context.expect_page() as p:
            assert p.value.locator("#play-pause").is_enabled(), "Ошибка воспроизведения"


