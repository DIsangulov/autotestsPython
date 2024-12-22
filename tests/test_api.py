import allure
import requests
from faker import Faker
from playwright.sync_api import expect

from req.api.auth_req import ReqAuth
from req.api.user_management_req import ReqUserManagement
from req.helpers.base_req import BaseReq
from resourses.global_hosts import HOST


# ________ constants __________
sess = requests.Session()
host = HOST
fake = Faker()
# ________ constants __________


@allure.feature("API - Авторизация")
class TestAuthentication:

    @allure.story("Авторизоваться в системе")
    def test_login(self):
        sess = requests.Session()  # Используем одну сессию
        req_auth = ReqAuth(sess, host)
        resp = req_auth.user_login()
        assert resp.status_code == 200, f"Ошибка входа пользователя, код {resp.status_code}, {resp.text}"

    @allure.story("Выйти из системы")
    def test_logout(self):
        req = BaseReq(sess, host)
        csrf_token = get_csrf_token()
        print(csrf_token)
        req = ReqAuth(sess, host)
        resp = req.user_logout(csrf_token)
        assert resp.status_code == 200, f"Ошибка входа пользователя, код {resp.status_code}, {resp.text}"

@allure.feature("API - Управление пользователями")
class TestUserManagement:
    @allure.story("Запрос списка залогированных пользователей")
    def test_logged_on_user_list(self, get_and_set_csrf):
        req = BaseReq(sess, host)
        csrf_token = get_csrf_token()
        req = ReqUserManagement(sess, host)
        resp = req.logged_on_user_list(csrf_token)
        assert resp.status_code == 200, f"Ошибка вывода списка залогированных пользователей, код {resp.status_code}, {resp.text}"
        print(resp.status_code)