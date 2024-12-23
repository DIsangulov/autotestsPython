import json
from http.cookies import SimpleCookie

import allure
import pytest
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


@allure.feature("API - ")
class TestUserManagement:

    def setup_method(self):
        self.sess = requests.Session()  # Создаем сессию на уровне экземпляра

    @allure.story("Авторизоваться в системе")
    def test_login(self):
        req_auth = ReqAuth(self.sess, host)
        resp = req_auth.user_login()
        assert resp.status_code == 200, f"Ошибка входа пользователя, код {resp.status_code}, {resp.text}"


    @allure.story("Запрос списка залогированных пользователей")
    def test_logged_on_user_list(self, auth_api):
        req = ReqUserManagement(self.sess, host)
        token = auth_api.auth()
        resp = req.logged_on_user_list(token)
        print(resp.text)
        response_data = json.loads(resp.text)
        global user_id
        user_id = response_data[0]["userId"]
        assert resp.status_code == 200, f"Ошибка вывода списка залогированных пользователей, код {resp.status_code}, {resp.text}"

    @allure.story("Получение данных о пользователе по userId")
    def test_get_user_details_by_id(self, auth_api):
        req = ReqUserManagement(self.sess, host)
        token = auth_api.auth()
        resp = req.get_user_details_by_id(token, user_id)
        print(resp.text)
        assert resp.status_code == 200, f"Ошибка получения данных о пользователе, код {resp.status_code}, {resp.text}"

    @allure.story("Получение данных о сессии пользователя")
    def test_get_current_session_user(self, auth_api):
        req = ReqUserManagement(self.sess, host)
        token = auth_api.auth()
        resp = req.get_user_details_by_id(token, user_id)
        print(resp.text)
        assert resp.status_code == 200, f"Ошибка получения данных о сессии пользователя, код {resp.status_code}, {resp.text}"



    @pytest.mark.skip
    @allure.story("Выход из аккаунта пользователя")
    def test_logout(self, auth_api):
        req = ReqAuth(self.sess, host)
        token = auth_api.auth()
        resp = req.user_logout(token)
        print(resp.text)
        assert resp.status_code == 200, f"Ошибка выхода из аккаунта пользователя, код {resp.status_code}, {resp.text}"



