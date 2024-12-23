class BaseReq:
    def __init__(self, sess, host):
        self.sess = sess
        self.host = host

    def auth(self, username="admin", password="1q2w3e4r5t"):
        jsn = {"username": username, "password": password}
        resp = self.sess.post(f"{self.host}/aioc-rest-web/rest/jwt/login", json=jsn, verify=False)
        token = resp.json().get("access_token")
        return token








