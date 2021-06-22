from formaloo import constants, client


class CustomerBatch:

    def __init__(self, customers=None):
        if not customers:
            customers = []

        self.client = client.client
        self.customers = customers

    def add_customer(self, customer):
        self.customers.append(customer)

    def create(self):
        body = self.get_body()

        response = self.client.post(
            constants.V_1_0_CUSTOMER_BATCH_ENDPOINT,
            body=body
        )

        return response.json()

    def get_body(self):
        body = {
            'customers_data': []
        }

        for customer in self.customers:
            body['customers_data'].append(
                customer.get_body()
            )

        return body
