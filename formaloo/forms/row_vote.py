from formaloo import constants, helper


class RowVote(helper.RequestHandler):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.actions = {
            "get_list": {
                "url": constants.V_1_0_ROW_VOTE_LIST_CREATE_ENDPOINT,
                "has_url_params": True,
                "body": None,
                "method": self.client.get
            },
            "create": {
                "url": constants.V_1_0_ROW_VOTE_LIST_CREATE_ENDPOINT,
                "has_url_params": True,
                "body": self.get_body(),
                "method": self.client.post
            },
            "patch": {
                "url": constants.V_1_0_ROW_VOTE_ITEM_ENDPOINT,
                "has_url_params": True,
                "body": self.get_body(),
                "method": self.client.patch
            },
            "delete": {
                "url": constants.V_1_0_ROW_VOTE_ITEM_ENDPOINT,
                "has_url_params": True,
                "body": None,
                "method": self.client.delete
            }
        }
