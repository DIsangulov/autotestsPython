import time

from pages.Helpers.base_page import BasePage
from resources.locators import MainLocators


class Devices(BasePage):

    def open_devices(self):
        self.page.get_by_text("Управление устройствами").click()
        self.page.get_by_text("Устройства").nth(1).click()

    def open_new_device_discovery_tab(self):
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Обнаружить новое устройство").click()

    def detect_and_add_new_device(self, name):
        self.input_text_field("IP-адреса или домен устройства:", "1.1.1.1")
        self.input_text_field("Имя устройства:", name)
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Протокол доступа:").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("SSHv2").click()
        self.input_text_field("Номер порта:", "22")
        self.delay_input(MainLocators.MAIN_FRAME,
                         "//label[contains(text(), 'Тип элемента:')]/following::input[1]", "Linux Server")
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Linux Server").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Имя интерфейса:").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("None").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Site коннектор:").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("None").click()
        self.delay_input(MainLocators.MAIN_FRAME, "//label[contains(text(), 'Выбор Группы устройств:')]/following::input[1]", "test1")
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("test1").nth(1).click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("(//button[@class='x-btn-text' and @type='button'])[2]").click()
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Обнаружить и добавить").click()
        try:
            self.page.frame_locator(MainLocators.MAIN_FRAME).locator(MainLocators.OK_BUTTON).click()
        except:
            pass

    def should_device_detected_and_added(self, name):
        try:
            self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Cancel").click()
        except:
            pass
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text(name).click(click_count=2)
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator(
            "//span[contains(text(), 'test1')]/following::span[2]").click(button='right')
        self.page.frame_locator(MainLocators.MAIN_FRAME).get_by_text("Открыть терминал").click()
        time.sleep(2)
        with self.page.context.expect_page() as p:
            assert p.value.locator("//div[@class='col-md-4 logo']").is_visible()






