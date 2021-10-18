from formaloo import constants, helper


class Field(helper.RequestHandler):

    def __init__(self, type, **kwargs):
        super().__init__(**kwargs)
        self.type = type
        self.actions = {
            "get_list": {
                "url": constants.V_1_0_FIELD_LIST_CREATE_ENDPOINT,
                "has_url_params": False,
                "body": None,
                "method": self.client.get
            },
            "create": {
                "url": constants.V_1_0_FIELD_LIST_CREATE_ENDPOINT,
                "has_url_params": False,
                "body": self.get_body(),
                "method": self.client.post,
                "set_from_response_data": {
                    # set slug as instance variable from response data
                    'slug': ('data', 'field', 'slug'),
                }
            },
            "get": {
                "url": constants.V_1_0_FIELD_ITEM_ENDPOINT,
                "has_url_params": True,
                "body": None,
                "method": self.client.get
            },
            "patch": {
                "url": constants.V_1_0_FIELD_ITEM_ENDPOINT,
                "has_url_params": True,
                "body": self.get_body(),
                "method": self.client.patch
            },
            "delete": {
                "url": constants.V_1_0_FIELD_ITEM_ENDPOINT,
                "has_url_params": True,
                "body": None,
                "method": self.client.delete
            }
        }

    def get_body(self):
        body = {
            'type': self.type
        }

        body.update(self.data)

        return body
