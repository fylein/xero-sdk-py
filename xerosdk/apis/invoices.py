from .api_base import ApiBase


class Invoices(ApiBase):

    GET_INVOICES = '/api.xro/2.0/invoices'
    GET_INVOICE_BY_ID = '/api.xro/2.0/invoices/{0}'
    POST_INVOICE = '/api.xro/2.0/invoices'

    def get_all(self):
        return self._get_request(Invoices.GET_INVOICES)

    def get_by_id(self, invoice_id):
        return self._get_request(Invoices.GET_INVOICE_BY_ID.format(invoice_id))

    def post(self, data):
        return self._post_request(data, Invoices.POST_INVOICE)
