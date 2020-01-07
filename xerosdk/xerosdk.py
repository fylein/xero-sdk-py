import requests
import json
import base64

from .apis import *


class XeroSDK:
    """
    Creates connection with Xero APIs using OAuth2 authentication

    Parameters:
        base_url (str): Base URL for Xero API
        client_id (str): Client ID for Xero API
        client_secret (str): Client Secret for Xero API
        refresh_token (str): Refresh token for Xero API
    """

    TOKEN_URL = "https://identity.xero.com/connect/token"
    AUTHORIZE_URL = "https://login.xero.com/identity/connect/authorize"

    def __init__(self, base_url, client_id, client_secret, refresh_token):
        # Store the input parameters
        self.__base_url = base_url
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__refresh_token = refresh_token

        # Create an object for each API
        self.Invoices = Invoices()
        self.Accounts = Accounts()
        self.Contacts = Contacts()
        self.TrackingCategories = TrackingCategories()

        # Set the server url
        self.set_server_url()

        # Refresh access token
        self.refresh_access_token()

    def set_server_url(self):
        """
        Set server URL for all API objects
        """

        base_url = self.__base_url

        self.Invoices.set_server_url(base_url)
        self.Accounts.set_server_url(base_url)
        self.Contacts.set_server_url(base_url)
        self.TrackingCategories.set_server_url(base_url)

    def refresh_access_token(self):
        """
        Refresh access token for each API objects
        """

        access_token = self.__get_access_token()

        self.Invoices.change_access_token(access_token)
        self.Accounts.change_access_token(access_token)
        self.Contacts.change_access_token(access_token)
        self.TrackingCategories.change_access_token(access_token)

    def __get_access_token(self):
        """
        Get access token from Xero TOKEN_URL

        Returns:
            A new access token
        """

        api_headers = {
            "authorization": "Basic " + str(
                base64.b64encode(
                    (self.__client_id + ":" + self.__client_secret).encode("utf-8")
                ), "utf-8"
            ),
        }
        api_data = {
            "grant_type": "refresh_token",
            "refresh_token": self.__refresh_token
        }
        response = requests.post(XeroSDK.TOKEN_URL, headers=api_headers, data=api_data)

        if response.status_code == 200:
            token = json.loads(response.text)
            return token["access_token"]
