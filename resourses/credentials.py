import os

TARGET_URL = os.environ.get('TARGET_URL', "https://10.130.7.15/idm/api")


class TestUsers:
    # /login  #  auth_data

    MchQa = {
        "login": os.environ.get('TARGET_API_USER', "admin"),
        "password": os.environ.get('TARGET_API_PASSWORD', "Admin123")
    }

