import json

import requests

from req.helpers.base_req import BaseReq


class ReqAuth(BaseReq):
    def user_login(self):
        csrf_token = self.get_csrf_token()
        headers = {
            "Content-Type": "application/json",
            "X-XSRF-TOKEN": csrf_token
        }
        data = {"username": "admin", "password": "1q2w3e4r5t"}
        print(f"Sending login request with data: {data} and headers: {headers}")

        # Отправляем запрос на вход
        resp = self.sess.post(f"{self.host}/aioc-rest-web/rest/login", json=data, headers=headers, verify=False)
        print(f"Login response: {resp.status_code}, {resp.text}")

        if resp.status_code == 200:
            csrf_token = resp.cookies.get('XSRF-TOKEN')
            if csrf_token:
                print(f"Updated CSRF Token after login: {csrf_token}")

        return resp

    def user_logout(self, csrf_token):
        headers = {
            "X-XSRF-TOKEN": csrf_token
        }
        resp = self.sess.post(f"{self.host}/aioc-rest-web/rest/logout", headers=headers, verify=False)
        return resp