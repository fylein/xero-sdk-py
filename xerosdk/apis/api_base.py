import requests
import json


class ApiBase:

    def __init__(self):
        self.__access_token = None
        self.__server_url = None

    def change_access_token(self, access_token):
        self.__access_token = access_token

    def set_server_url(self, server_url):
        self.__server_url = server_url

    def _get_request(self, api_url):
        api_headers = {'Authorization': f'Bearer {self.__access_token}'}

        response = requests.get(
            f'{self.__server_url}{api_url}',
            headers=api_headers
        )

        if response.status_code == 200:
            result = json.loads(response.text)
            return result

    def _post_request(self, data, api_url):
        api_headers = {'Authorization': f'Bearer {self.__access_token}'}

        response = requests.post(
            f'{self.__server_url}{api_url}',
            headers=api_headers,
            data=data
        )

        if response.status_code == 200:
            result = json.loads(response.text)
            return result
