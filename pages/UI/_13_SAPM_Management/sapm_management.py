import time

from pages.Helpers.base_page import BasePage
from resources.locators import MainLocators
from ssh_draft.ssh import SSH


class SapmManagement(BasePage, SSH):

    def open_sapm_management(self):
        self.page.get_by_text("Управление SAPM").click()
        self.page.locator("(//*[text()='SAPM'])[1]").click()

    def create_sapm_account(self, user_name):
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("//label[contains(text(), 'Тип:')]/following::input[1]").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Static").click()
        self.delay_input(MainLocators.MAIN_FRAME, "//label[contains(text(), 'Конфигурация:')]/following::input[1]", "Linux")
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("//*[text()='Name: Linux']").press("Enter")
        self.input_text_field("Имя пользователя:", user_name)
        self.input_text_field("Пароль:", user_name)
        self.input_text_field("Имя аккаунта", "SAPM")
        self.delay_input(MainLocators.MAIN_FRAME, "//label[contains(text(), 'Хост (IP/Название):')]/following::input[1]", "local")
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("//*[text()='Name: local']").press("Enter")
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("//*[text()='Сохранить']").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("//*[text()='Да']").click()





