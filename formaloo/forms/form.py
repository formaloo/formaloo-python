from formaloo import constants, helper


class Form(helper.RequestHandler):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.actions = {
            "get_list": {
                "url": constants.V_1_0_FORM_LIST_CREATE_ENDPOINT,
                "has_url_params": False,
                "body": None,
                "method": self.client.get
            },
            "create": {
                "url": constants.V_1_0_FORM_LIST_CREATE_ENDPOINT,
                "has_url_params": False,
                "body": self.get_body(),
                "method": self.client.post,
                "set_from_response_data": {
                    # set slug and address as
                    # instance variables from response data
                    'slug': ('data', 'form', 'slug'),
                    'address': ('data', 'form', 'address')
                }
            },
            "get": {
                "url": constants.V_1_0_FORM_ITEM_ENDPOINT,
                "has_url_params": True,
                "body": None,
                "method": self.client.get
            },
            "rows_list": {
                "url": constants.V_1_0_FORM_ROWS_LIST,
                "has_url_params": True,
                "body": None,
                "method": self.client.get
            },
            "get_stats": {
                "url": constants.V_1_0_FORM_LIST_CREATE_ENDPOINT,
                "has_url_params": True,
                "body": None,
                "method": self.client.get
            },
            "patch": {
                "url": constants.V_1_0_FORM_ITEM_ENDPOINT,
                "has_url_params": True,
                "body": self.get_body(),
                "method": self.client.patch
            },
            "delete": {
                "url": constants.V_1_0_FORM_ITEM_ENDPOINT,
                "has_url_params": True,
                "body": None,
                "method": self.client.delete
            }
        }
