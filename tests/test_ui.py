# ________ constants __________
# region
import time

from pages.UI.Auth.auth_page import AuthPage

link = "https://10.0.5.27"


# endregion
# ________ constants __________

class TestAuth:

    def test_valid_auth(self, browser):
        page = AuthPage(browser, link)
        page.open()
        page.enter_as_user()
        page.should_enter_be_successful()

