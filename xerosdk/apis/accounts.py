"""
Xero Accounts API
"""

from .api_base import ApiBase


class Accounts(ApiBase):
    """
    Class for Accounts API
    """

    GET_ACCOUNTS = '/api.xro/2.0/Accounts'

    def get_all(self):
        """
        Get all accounts

        Returns:
            List of all accounts
        """

        return self._get_request(Accounts.GET_ACCOUNTS)

    def post(self, data):
        return self._post_request(data, Accounts.GET_ACCOUNTS)
