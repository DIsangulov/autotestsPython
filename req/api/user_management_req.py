from req.helpers.base_req import BaseReq


class ReqUserManagement(BaseReq):
    def logged_on_user_list(self, csrf_token):
        headers = {
            "X-XSRF-TOKEN": csrf_token
        }
        resp = self.sess.get(f"{self.host}/aioc-rest-web/rest/user/getActiveSessionsOfUsers", headers=headers, verify=False)
        return resp
