from formaloo import constants, client, helper
from formaloo.tags import Tag


class Customer(helper.RequestHandler):

    def __init__(self, base_data=None, extra_data=None, tags=None, **kwargs):
        if not base_data:
            base_data = {}

        if not extra_data:
            extra_data = {}

        if not tags:
            tags = []

        self.client = client.client
        self.base_customer_data = base_data
        self.extra_customer_data = extra_data
        self.tags = tags

        for key, value in kwargs.items():
            if key in constants.CUSTOMER_BASE_FIELDS:
                self.base_customer_data[key] = value
            else:
                self.extra_customer_data[key] = value

        self.actions = {
            "get_list": {
                "url": constants.V_1_0_CUSTOMER_LIST_CREATE_ENDPOINT,
                "has_url_params": False,
                "body": None,
                "method": self.client.get
            },
            "get": {
                "url": constants.V_1_0_CUSTOMER_ITEM_ENDPOINT,
                "has_url_params": True,
                "body": None,
                "method": self.client.get
            },
            "create": {
                "url": constants.V_1_0_CUSTOMER_LIST_CREATE_ENDPOINT,
                "has_url_params": False,
                "body": self.get_body(),
                "method": self.client.post
            }
        }

    def get_body(self):
        tags_body = Tag.get_list_body(self.tags)

        body = {
            'customer_data': self.extra_customer_data,
            'tags': tags_body
        }
        body.update(self.base_customer_data)

        return body
