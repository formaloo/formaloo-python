from formaloo import constants, helper


class FormDisplay(helper.RequestHandler):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.actions = {
            "get_by_address": {
                "url": constants.V_1_0_FORM_DISPLAY_ADDRESS_ENDPOINT,
                "has_url_params": True,
                "body": None,
                "method": self.client.get
            },
            "get_by_slug": {
                "url": constants.V_1_0_FORM_DISPLAY_SLUG_ENDPOINT,
                "has_url_params": True,
                "body": None,
                "method": self.client.get
            },
            "submit": {
                "url": constants.V_1_0_FORM_DISPLAY_SUBMIT_ENDPOINT,
                "has_url_params": True,
                "body": self.get_body(),
                "method": self.client.post
            }
        }
