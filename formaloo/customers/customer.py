from formaloo import constants, client
from formaloo.tags import Tag


class Customer:

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

    def get_body(self):
        tags_body = Tag.get_list_body(self.tags)

        body = {
            'customer_data': self.extra_customer_data,
            'tags': tags_body
        }
        body.update(self.base_customer_data)

        return body

    def get_list(self, **kwargs):
        params = kwargs

        response = self.client.get(
            constants.V_1_0_CUSTOMER_LIST_CREATE_ENDPOINT,
            params=params
        )

        return response.json()

    def create(self):
        body = self.get_body()

        response = self.client.post(
            constants.V_1_0_CUSTOMER_LIST_CREATE_ENDPOINT,
            body=body
        )

        return response.json()

    def get(self, code, **kwargs):
        params = kwargs

        response = self.client.get(
            constants.V_1_0_CUSTOMER_ITEM_ENDPOINT.format(code),
            params=params
        )

        return response.json()
