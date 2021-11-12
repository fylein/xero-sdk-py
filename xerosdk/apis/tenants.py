"""
Xero Tenants API
"""

from .api_base import ApiBase


class Tenants(ApiBase):
    """
    Class for Tenants
    """
    REVOKE_CONNECTION = '/connections/{}'

    def get_all(self):
        """
        Get all Tenants

        Returns:
            List of all Tenants
        """

        return self._get_tenant_ids()


    def remove_connection(self):
        """
        Revoke tenant connection
        """

        return self._delete_request(Tenants.REVOKE_CONNECTION.format(self.tenant_id))
