from req.helpers.base_req import BaseReq


class ReqUserManagement(BaseReq):
    def logged_on_user_list(self, token):
        headers = {"Authorization": f"Bearer {token}"}
        resp = self.sess.get(f"{self.host}/aioc-rest-web/rest/user/getActiveSessionsOfUsers", headers=headers, verify=False)
        return resp

    def get_user_details_by_id(self, token, user_id):
        headers = {"Authorization": f"Bearer {token}"}
        resp = self.sess.get(f"{self.host}/aioc-rest-web/rest/user/detail/{user_id}", headers=headers, verify=False)
        return resp

    def get_current_session_user(self, token, user_id):
        headers = {"Authorization": f"Bearer {token}"}
        resp = self.sess.get(f"{self.host}/aioc-rest-web/rest/user/{user_id}", headers=headers, verify=False)
        return resp

