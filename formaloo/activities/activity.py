import requests

from formaloo import constants, client


class Activity:

    def __init__(self, action, customer_data, activity_data={}, activity_date=None, tags=[]):
        self.client = client.Client()
        self.action = action
        self.customer_data = customer_data
        self.activity_data = activity_data
        self.activity_date = activity_date
        self.tags = tags

    def create(self):
        headers = self.client.get_headers()
        body = self.get_body()

        response = requests.post(
            constants.V_1_0_CREATE_ACTIVITY_ENDPOINT,
            headers=headers,
            data=body
        )

        return response

    def get_body(self):
        body = {
            'action': self.action,
            'custmer': self.customer_data,
            'activity_data': self.activity_data,
            'activity_date': self.activity_date,
            'tags': self.tags
        }

        return body
