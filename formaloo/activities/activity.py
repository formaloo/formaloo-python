from formaloo import constants, client
from formaloo.tags import Tag


class Activity:

    def __init__(self, action=None, customer_data=None, activity_data=None, activity_date=None, tags=None):
        if not activity_data:
            activity_data = {}

        if not tags:
            tags = []

        if not customer_data:
            customer_data = {}

        self.client = client.client
        self.action = action
        self.customer_data = customer_data
        self.activity_data = activity_data
        self.activity_date = activity_date
        self.tags = tags

    def get_body(self):
        tags_body = Tag.get_list_body(self.tags)

        body = {
            'action': self.action,
            'customer': self.customer_data,
            'activity_data': self.activity_data,
            'activity_date': self.activity_date,
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
