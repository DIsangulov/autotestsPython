import contextlib
import datetime
import logging
import os
from http.client import HTTPConnection

import allure
import paramiko
import pytest
import requests
from playwright.sync_api import sync_playwright

from req.helpers.base_req import BaseReq
from ssh_draft.ssh import SSH

host = os.environ.get('TARGET_URL', "https://10.130.6.29")
sess = requests.Session()


@pytest.fixture(scope='function')
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel="chrome", headless=False)
        context = browser.new_context(ignore_https_errors=True, viewport={"width": 1920, "height": 1080})
        page = context.new_page()
        yield page
        take_screenshot(page)
        page.close()
        browser.close()

@pytest.fixture(scope='class')
def auth_api():
    req = BaseReq(sess, host)
    req.auth()
    yield req


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
    ssh = SSH(host=link)
    ssh.connect()
    yield ssh
    ssh.close_connection()



def debug_requests_on():
    """Switches on logging of the requests module."""
    HTTPConnection.debuglevel = 1

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True


def debug_requests_off():
    """Switches off logging of the requests module, might be some side-effects"""
    HTTPConnection.debuglevel = 0

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.WARNING)
    root_logger.handlers = []
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.WARNING)
    requests_log.propagate = False


@contextlib.contextmanager
def debug_requests():
    """Use with 'with'!"""
    debug_requests_on()
    yield
    debug_requests_off()


@pytest.fixture(autouse=True)
def enable_debug_requests():
    """Фикстура для включения логирования запросов для каждого теста."""
    with debug_requests():
        yield