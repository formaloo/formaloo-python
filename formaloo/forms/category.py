from formaloo import constants, helper


class FormCategory(helper.RequestHandler):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.actions = {
            "get_list": {
                "url": constants.V_1_0_FORM_CATEGORY_LIST_CREATE_ENDPOINT,
                "has_url_params": False,
                "body": None,
                "accept_query_params": True,
                "method": self.client.get
            },
            "create": {
                "url": constants.V_1_0_FORM_CATEGORY_LIST_CREATE_ENDPOINT,
                "has_url_params": False,
                "body": self.get_body(),
                "accept_query_params": False,
                "method": self.client.post
            },
            "get": {
                "url": constants.V_1_0_FORM_CATEGORY_ITEM_ENDPOINT,
                "has_url_params": True,
                "body": None,
                "accept_query_params": True,
                "method": self.client.get
            },
            "patch": {
                "url": constants.V_1_0_FORM_CATEGORY_ITEM_ENDPOINT,
                "has_url_params": True,
                "body": self.get_body(),
                "accept_query_params": False,
                "method": self.client.patch
            },
            "delete": {
                "url": constants.V_1_0_FORM_CATEGORY_ITEM_ENDPOINT,
                "has_url_params": True,
                "body": None,
                "accept_query_params": True,
                "method": self.client.delete
            }
        }
