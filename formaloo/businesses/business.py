from formaloo import constants, client


class Business:

    def __init__(self, **kwargs):
        self.client = client.Client()

    def get_list(self, **kwargs):
        params = kwargs

        response = self.client.get(
            constants.V_1_0_BUSINESS_LIST_ENDPOINT,
            params=params
        )

        return response.status_code, response.json()
