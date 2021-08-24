"""
Xero Items API
"""

from .api_base import ApiBase


class Items(ApiBase):
    """
    Class for Items API
    """

    GET_ITEMS = '/api.xro/2.0/Items'

    def get_all(self):
        """
        Get all Items

        Returns:
            List of all Items
        """

        return list(self._get_all(Items.GET_ITEMS, 'Items'))
