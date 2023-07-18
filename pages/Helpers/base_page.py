import datetime
import time

import allure
from playwright.sync_api import Playwright, Page

from resources.locators import MainLocators


class BasePage:
    def __init__(self, page: Page, url: str, timeout: int = 10):
        self.page = page
        self.url = url
        self.page.set_default_timeout(timeout * 1000)

    def open(self):
        self.page.goto(self.url)

    def open_new_tab(self, link):
        self.page.click(f'text={link}')
        self.page.wait_for_selector(f'//a[@href="{link}"]', timeout=3000)
        self.page.click(f'xpath=//a[@href="{link}"]')
        self.page.wait_for_selector(f':not([href="{link}"])')

    def is_element_present(self, selector: str):
        return self.page.query_selector(selector)

    def switch(self, handle_number: int):
        handles = self.page.context.pages
        self.page = handles[handle_number]

    def close_handle(self, handle_num: int):
        self.switch(handle_num)
        self.page.close()

    def clear_input(self, selector: str):
        input_field = self.page.query_selector(selector)
        input_field.fill('')
        self.page.keyboard.press('Tab')

    def browser_close(self):
        self.page.close()

    def delay_input(self, frame_loc: str, elem_loc: str, input_str: str):
        d = self.page.frame_locator(frame_loc).locator(elem_loc)
        for char in input_str:
            d.type(char, delay=100)
            time.sleep(0.5)

    def input_text_field(self, elem_name: str, input_text):
        self.page.frame_locator(MainLocators.MAIN_FRAME).locator("//label[contains(text(), '"+elem_name+"')]/following::input[1]").fill(input_text)


