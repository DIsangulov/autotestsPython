from req.helpers.base_req import BaseReq


class ReqAuth(BaseReq):
    def user_login(self):
        data = {"username": "admin", "password": "1q2w3e4r5t"}
        resp = self.sess.post(f"{self.host}/aioc-rest-web/rest/jwt/login", json=data, verify=False)
        print(resp.text)
        return resp

    def user_logout(self, token):
        headers = {"Authorization": f"Bearer {token}"}
        resp = self.sess.post(f"{self.host}/aioc-rest-web/rest/logout", headers=headers, verify=False)
        return resp