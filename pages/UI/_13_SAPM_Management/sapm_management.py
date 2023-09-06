from pages.Helpers.base_page import BasePage
from resources.locators import MainLocators


class SapmManagement(BasePage):

    def open_sapm_management(self):
        self.page.get_by_text("Управление SAPM").click()
        self.page.locator("(//*[text()='SAPM'])[1]").click()
