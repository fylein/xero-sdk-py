"""
Xero TrackingCategories API
"""

from .api_base import ApiBase


class TrackingCategories(ApiBase):
    """
    Class for Tracking Categories API
    """

    GET_TRACKING_CATEGORIES = '/api.xro/2.0/trackingcategories'

    def get_all(self):
        """
        Get all tracking categories

        Returns:
            List of all tracking categories
        """

        return list(self._get_all(TrackingCategories.GET_TRACKING_CATEGORIES, 'TrackingCategories'))
