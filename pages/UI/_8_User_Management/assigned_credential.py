import time

from pages.Helpers.base_page import BasePage
from resources.locators import MainLocators


class AssignedCredential(BasePage):

    def open_assigned_credential(self):
        self.page.get_by_text("Управление пользователями").click()
        self.page.get_by_text("Назначенные аккаунты").click()

    def assigning_user_rights(self, user_name):
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("//label[contains(text(), 'Выбор пользователя:')]/following::input[1]").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("//*[text()='User']").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("//label[contains(text(), 'Источник назначения:')]/following::input[1]").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("//div[@title='SAPM']").click()
        self.delay_input(MainLocators.MAIN_FRAME, "//label[contains(text(), 'Имя пользователя:')]/following::input[1]", "admin")
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("//p[contains(text(), 'Username: admin')]").click()
        self.delay_input(MainLocators.MAIN_FRAME, "//label[contains(text(), 'Имя пользователя SAPM:')]/following::input[1]", user_name)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("//p[contains(text(), '"+str(user_name)+"')]").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("//*[text()='Сохранить']").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("//*[text()='Да']").click()





