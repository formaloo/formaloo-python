from formaloo import constants, client, helper


class CustomerBatch(helper.RequestHandler):

    def __init__(self, customers=None):
        if not customers:
            customers = []

        self.client = client.client
        self.customers = customers
        self.actions = {
            "create": {
                "url": constants.V_1_0_CUSTOMER_BATCH_ENDPOINT,
                "has_url_params": False,
                "body": self.get_body(),
                "method": self.client.post
            }
        }

    def add_customer(self, customer):
        self.customers.append(customer)

    def get_body(self):
        body = {
            'customers_data': []
        }

        for customer in self.customers:
            body['customers_data'].append(
                customer.get_body()
            )

        return body
