from formaloo import constants, client, helper
from formaloo.tags import Tag


class Activity(helper.RequestHandler):

    def __init__(
        self, customer_data=None,
        activity_data=None, tags=None,
        **kwargs
    ):
        if not activity_data:
            activity_data = {}

        if not tags:
            tags = []

        if not customer_data:
            customer_data = {}

        self.client = client.client
        self.customer_data = customer_data
        self.activity_data = activity_data
        self.action = kwargs.get('action', None)
        self.activity_date = kwargs.get('activity_date', None)
        self.relations = kwargs.get('relations', None)
        self.monetary_value = kwargs.get('monetary_value', None)
        self.currency = kwargs.get('currency', None)
        self.tags = tags
        self.actions = {
            "get_list": {
                "url": constants.V_1_0_ACTIVITY_LIST_CREATE_ENDPOINT,
                "has_url_params": False,
                "body": None,
                "method": self.client.get
            },
            "get": {
                "url": constants.V_1_0_ACTIVITY_ITEM_ENDPOINT,
                "has_url_params": True,
                "body": None,
                "method": self.client.get
            },
            "create": {
                "url": constants.V_1_0_ACTIVITY_LIST_CREATE_ENDPOINT,
                "has_url_params": False,
                "body": self.get_body(),
                "method": self.client.post
            }
        }

    def get_body(self):
        tags_body = Tag.get_list_body(self.tags)

        body = {
            'action': self.action,
            'customer': self.customer_data,
            'activity_data': self.activity_data,
            'activity_date': self.activity_date,
            'relations': self.relations,
            'monetary_value': self.monetary_value,
            'currency': self.currency,
            'tags': tags_body
        }

        return body
