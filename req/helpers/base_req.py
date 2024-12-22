import requests

URL = "https://10.130.6.29/aioc-rest-web/rest/login"




class BaseReq:
    def __init__(self, sess, host): # , sess
        self.sess = sess
        self.host = host

    def get_csrf_token(self):
        # Здесь вы можете сделать запрос, чтобы получить токен
        resp = self.sess.get(f"{self.host}/aioc-rest-web/rest/get-csrf-token", verify=False)
        csrf_token = resp.cookies.get('XSRF-TOKEN')
        print(f"CSRF Token obtained: {csrf_token}")
        return csrf_token








