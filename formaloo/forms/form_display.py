from formaloo import constants, client


class FormDisplay:

    def __init__(self, **kwargs):
        self.client = client.Client()

    def get_body(self):
        body = {
        }

        return body

    def get_by_address(self, address, **kwargs):
        params = kwargs

        response = self.client.get(
            constants.V_1_0_FORM_DISPLAY_ADDRESS_ENDPOINT.format(address),
            params=params
        )

        return response.json()

    def get_by_slug(self, slug, **kwargs):
        params = kwargs

        response = self.client.get(
            constants.V_1_0_FORM_DISPLAY_SLUG_ENDPOINT.format(slug),
            params=params
        )

        return response.json()

    def submit(self, slug):
        body = self.get_body()

        response = self.client.post(
            constants.V_1_0_FORM_DISPLAY_SLUG_ENDPOINT.format(slug),
            body=body
        )

        return response.json()
