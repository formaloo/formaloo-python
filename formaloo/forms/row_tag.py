from formaloo import constants, helper


class RowTag(helper.RequestHandler):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.actions = {
            "get_list": {
                "url": constants.V_1_0_FORM_ROW_TAGS_LIST_CREATE_ENDPOINT,
                "has_url_params": True,
                "body": None,
                "method": self.client.get
            },
            "create": {
                "url": constants.V_1_0_FORM_ROW_TAGS_LIST_CREATE_ENDPOINT,
                "has_url_params": True,
                "body": self.get_body(),
                "method": self.client.post
            },
            "get": {
                "url": constants.V_1_0_FORM_ROW_TAG_ITEM_ENDPOINT,
                "has_url_params": True,
                "body": None,
                "method": self.client.get
            },
            "patch": {
                "url": constants.V_1_0_FORM_ROW_TAG_ITEM_ENDPOINT,
                "has_url_params": True,
                "body": self.get_body(),
                "method": self.client.patch
            },
            "delete": {
                "url": constants.V_1_0_FORM_ROW_TAG_ITEM_ENDPOINT,
                "has_url_params": True,
                "body": None,
                "method": self.client.delete
            }
        }
