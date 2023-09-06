import datetime

import allure
import paramiko
import pytest
from playwright.sync_api import sync_playwright
from ssh_draft.ssh import SSH

# @pytest.fixture(scope='function')
# def browser():
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(channel="chrome", headless=False)
#         context = browser.new_context(ignore_https_errors=True, viewport={"width": 1920, "height": 1080})
#         page = context.new_page()
#         yield page
#         page.close()
#         browser.close()


@pytest.fixture(scope='function')
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel="chrome", headless=True)
        context = browser.new_context(ignore_https_errors=True, viewport={"width": 1920, "height": 1080})
        page = context.new_page()
        yield page
        take_screenshot(page)
        page.close()
        browser.close()


def take_screenshot(page):
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot = page.screenshot()
    screenshot_path = f"screenshots/screenshot_{current_datetime}.png"
    with open(screenshot_path, 'wb') as file:
        file.write(screenshot)
    allure.attach.file(screenshot_path, name=f"screenshot_{current_datetime}",
                       attachment_type=allure.attachment_type.PNG)


@pytest.fixture(scope='function')
def ssh():
    ssh = SSH(host='10.0.5.27')
    ssh.connect()
    yield ssh
    ssh.close_connection()
