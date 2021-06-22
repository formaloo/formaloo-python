from formaloo import constants, client
from formaloo.tags import Tag


class Activity:

    def __init__(self, customer_data=None, activity_data=None, tags=None, **kwargs):
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

    def get_body(self):
        tags_body = Tag.get_list_body(self.tags)

        body = {
            'action': self.action,
            'customer': self.customer_data,
            'monetary_value': self.monetary_value,
            'activity_data': self.activity_data,
            'activity_date': self.activity_date,
            'relations': self.relations,
            'monetary_value': self.monetary_value,
            'currency': self.currency,
            'tags': tags_body
        }

        return body

    def get_list(self, **kwargs):
        params = kwargs

        response = self.client.get(
            constants.V_1_0_ACTIVITY_LIST_CREATE_ENDPOINT,
            params=params
        )

        return response.json()

    def create(self):
        if not self.action:
            raise ValueError("`action` is required to create a tag!")

        body = self.get_body()

        response = self.client.post(
            constants.V_1_0_ACTIVITY_LIST_CREATE_ENDPOINT,
            body=body
        )

        return response.json()

    def get(self, slug, **kwargs):
        params = kwargs

        response = self.client.get(
            constants.V_1_0_ACTIVITY_ITEM_ENDPOINT,
            params=params
        )

        return response.json()
