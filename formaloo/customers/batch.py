import requests

from formaloo import constants, client


class CustomerBatch:

    def __init__(self, customers=[]):
        self.client = client.Client()
        self.customers = customers

    def add_customer(self, customer):
        self.customers.append(customer)

    def create(self):
        headers = self.client.get_headers()
        body = self.get_body()

        response = requests.post(
            constants.V_1_0_CUSTOMER_BATCH_ENDPOINT,
            headers=headers,
            data=body
        )

        return response

    def get_body(self):
        body = []

        for customer in self.customers:
            body.append(
                customer.get_body()
            )

        return body
