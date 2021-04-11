from formaloo import constants, client


class Customer:

    def __init__(self, base_data={}, extra_data={}, tags=[], **kwargs):
        self.client = client.Client()
        self.base_customer_data = base_data
        self.extra_customer_data = extra_data
        self.tags = tags

        for key, value in kwargs.items():
            if key in constants.CUSTOMER_BASE_FIELDS:
                self.base_customer_data[key] = value
            else:
                self.extra_customer_data[key] = value

    def create(self):
        body = self.get_body()

        response = self.client.post(
            constants.V_1_0_CREATE_CUSTOMER_ENDPOINT,
            body=body
        )

        return response

    def get_body(self):
        body = {
            'customer_data': self.extra_customer_data,
            'tags': self.tags
        }
        body.update(self.base_customer_data)

        return body
