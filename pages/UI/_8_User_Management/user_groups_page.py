import time

from pages.Helpers.base_page import BasePage
from resources.locators import UserGroupsLocators, MainLocators


class UserGroupDefinition(BasePage):
    def open_user_group_definition(self):
        self.page.get_by_text("Управление пользователями").click()
        self.page.get_by_text("Пользователи").click()
        self.page.frame_locator("//iframe[@class='gwt-Frame x-component']").get_by_text(
            "Определение группы пользователей").click()

    def enter_user_group(self, namegroup, username, description):
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(UserGroupsLocators.NAME_GROUP_INPUT).fill(namegroup)
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text(username).nth(0).click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("//div[@id='x-auto-183']").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(UserGroupsLocators.DESCRIPTION_INPUT).fill(description)
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text(username).nth(1).click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("//div[@id='x-auto-209']").click()

    def edit_user_group(self, editname):
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(UserGroupsLocators.OPTION_BUT).click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Редактировать").click()
        time.sleep(2)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(UserGroupsLocators.NAME_GROUP_INPUT).fill(editname)

    def click_save(self):
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.SAVE_BUTTON).click()

    def click_confirm(self):
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(UserGroupsLocators.CONFIRM_BUT).click()

    def search_user_group(self, namegroup):
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(UserGroupsLocators.NAME_GROUP_INPUT).fill(namegroup)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(UserGroupsLocators.SEARCH_BUT).click()

    def should_create_user_group_be_successful(self, namegroup):
        try:
            assert self.page.get_by_text(namegroup).is_visible()
        except:
            print("Данная группа пользователей найдена")

    def should_edit_user_group_be_successful(self, editname):
        try:
            assert self.page.get_by_text(editname).is_visible()
        except:
            print("Данная группа пользователей отредактирована")