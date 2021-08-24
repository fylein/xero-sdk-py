"""
Xero Accounts API
"""

from .api_base import ApiBase


class Accounts(ApiBase):
    """
    Class for Accounts API
    """

    GET_ACCOUNTS = '/api.xro/2.0/accounts'

    def get_all(self):
        """
        Get all accounts

        Returns:
            List of all accounts
        """

        return self._get_all(Accounts.GET_ACCOUNTS, 'Accounts')

    def post(self, data):
        return self._post_request(data, Accounts.GET_ACCOUNTS)
