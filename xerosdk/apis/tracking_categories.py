from .api_base import ApiBase


class TrackingCategories(ApiBase):

    GET_TRACKING_CATEGORIES = "/api.xro/2.0/trackingcategories"

    def get_all(self):
        return self._get_request(TrackingCategories.GET_TRACKING_CATEGORIES)
