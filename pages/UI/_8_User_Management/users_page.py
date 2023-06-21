from pages.Helpers.base_page import BasePage
from resources.locators import UserDefinitionLocators, MainLocators


class UserDefinition(BasePage):
    def open_user_definition(self):
        self.page.get_by_text("Управление пользователями").click()
        self.page.get_by_text("Пользователи").click()
        self.page.frame_locator("//iframe[@class='gwt-Frame x-component']").get_by_text(
            "Определение пользователя").click()

    def enter_user(self, username, personal_no, password, confirm_pass, name, surname, email, phone):
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(UserDefinitionLocators.USERNAME_INPUT).fill(username)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(UserDefinitionLocators.PERSON_NO_INPUT).fill(personal_no)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(UserDefinitionLocators.PASS_INPUT).fill(password)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(UserDefinitionLocators.CONFIRM_PASS_INPUT).fill(confirm_pass)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(UserDefinitionLocators.FIRST_NAME_INPUT).fill(name)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(UserDefinitionLocators.SURNAME_INPUT).fill(surname)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(UserDefinitionLocators.EMAIL_INPUT).fill(email)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(UserDefinitionLocators.PHONE_INPUT).fill(phone)

    def click_save(self):
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(UserDefinitionLocators.SAVE_BUT).click()

    def search_user(self, username):
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(UserDefinitionLocators.USERNAME_INPUT).fill(username)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(UserDefinitionLocators.SEARCH_BUT).click()

    def should_create_user_be_successful(self, username):
        try:
            assert self.page.get_by_text(username).is_visible()
        except:
            print("Данный пользователь найден")
