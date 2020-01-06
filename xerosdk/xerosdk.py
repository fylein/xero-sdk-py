import requests
import json
import base64

from .apis import *


class XeroSDK:
    TOKEN_URL = "https://identity.xero.com/connect/token"
    AUTHORIZE_URL = "https://login.xero.com/identity/connect/authorize"

    def __init__(self, base_url, client_id, client_secret, refresh_token):
        self.__base_url = base_url
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__refresh_token = refresh_token

        self.Invoices = Invoices()

        self.set_server_url()
        self.refresh_access_token()

    def set_server_url(self):
        base_url = self.__base_url

        self.Invoices.set_server_url(base_url)

    def refresh_access_token(self):
        access_token = self.__get_access_token()

        self.Invoices.change_access_token(access_token)

    def __get_access_token(self):
        authorization_header = f"{self.__client_id}:{self.__client_secret}"
        api_headers = {
            "authorization": f"Basic {str(base64.b64encode(authorization_header.encode()))}"
        }
        api_data = {
            "grant_type": "authorization_code",
            "refresh_token": self.__refresh_token
        }
        response = requests.post(XeroSDK.TOKEN_URL, headers=api_headers, data=api_data)

        if response.status_code == 200:
            access_token = json.loads(response.text)
            return access_token
