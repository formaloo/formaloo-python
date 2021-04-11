from formaloo import constants, client
from formaloo.tags import Tag


class Activity:

    def __init__(self, action, customer_data, activity_data=None, activity_date=None, tags=None):
        if not activity_data:
            activity_data = {}

        if not tags:
            tags = []

        self.client = client.Client()
        self.action = action
        self.customer_data = customer_data
        self.activity_data = activity_data
        self.activity_date = activity_date
        self.tags = tags

    def create(self):
        body = self.get_body()

        response = self.client.post(
            constants.V_1_0_CREATE_ACTIVITY_ENDPOINT,
            body=body
        )

        return response

    def get_body(self):
        tags_body = Tag.get_list_body(self.tags)

        body = {
            'action': self.action,
            'custmer': self.customer_data,
            'activity_data': self.activity_data,
            'activity_date': self.activity_date,
            'tags': tags_body
        }

        return body
