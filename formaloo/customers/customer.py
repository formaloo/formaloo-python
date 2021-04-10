import requests

from formaloo import constants, client


class Customer:

    def __init__(self, base_data, extra_data={}, tags=[]):
        self.client = client.Client()
        self.base_customer_data = base_data
        self.extra_customer_data = extra_data
        self.tags = tags

    def create(self):
        headers = self.client.get_headers()
        body = self.get_body()

        response = requests.post(
            constants.V_1_0_CREATE_CUSTOMER_ENDPOINT,
            headers=headers,
            data=body
        )

        return response

    def get_body(self):
        body = {
            'customer_data': self.extra_customer_data,
            'tags': self.tags
        }
        body.update(self.base_customer_data)

        return body
