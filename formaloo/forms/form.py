from formaloo import constants, client


class Form:

    def __init__(self, **kwargs):
        self.client = client.Client()

        self.data = kwargs

    def get_body(self):
        body = {
        }

        body.update(self.data)

        return body

    def get_list(self, **kwargs):
        params = kwargs

        response = self.client.get(
            constants.V_1_0_FORM_LIST_CREATE_ENDPOINT,
            params=params
        )

        return response.json()

    def create(self):
        body = self.get_body()

        response = self.client.post(
            constants.V_1_0_FORM_LIST_CREATE_ENDPOINT,
            body=body
        )

        return response.json()

    def get(self, slug, **kwargs):
        params = kwargs

        response = self.client.get(
            constants.V_1_0_FORM_ITEM_ENDPOINT.format(slug),
            params=params
        )

        return response.json()

    def patch(self, slug, **kwargs):
        params = kwargs

        response = self.client.patch(
            constants.V_1_0_FORM_ITEM_ENDPOINT.format(slug),
            params=params
        )

        return response.json()

    def delete(self, slug, **kwargs):
        params = kwargs

        response = self.client.patch(
            constants.V_1_0_FORM_ITEM_ENDPOINT.format(slug),
            params=params
        )

        return response.json()
