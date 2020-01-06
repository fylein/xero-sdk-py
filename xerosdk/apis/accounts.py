from .api_base import ApiBase


class Accounts(ApiBase):
    GET_ACCOUNTS = "/api.xro/2.0/accounts"

    def get_all(self):
        return self._get_request(Accounts.GET_ACCOUNTS)
