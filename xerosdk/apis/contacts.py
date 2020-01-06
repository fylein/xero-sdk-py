from .api_base import ApiBase


class Contacts(ApiBase):

    GET_CONTACTS = "/api.xro/2.0/contacts"

    def get_all(self):
        return self._get_request(Contacts.GET_CONTACTS)
