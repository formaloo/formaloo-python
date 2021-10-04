from formaloo import constants, helper


class FormTemplate(helper.RequestHandler):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.actions = {
            "get_list": {
                "url": constants.V_1_0_FORM_TEMPLATE_LIST_ENDPOINT,
                "has_url_params": False,
                "body": None,
                "method": self.client.get
            }
        }
