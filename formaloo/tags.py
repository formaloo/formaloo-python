from formaloo import constants, client, helper


class Tag(helper.RequestHandler):

    def __init__(self, title=None, description=None, slug=None):
        self.client = client.client
        self.title = title
        self.description = description
        self.slug = slug
        self.actions = {
            "get_list": {
                "url": constants.V_1_0_TAG_LIST_CREATE_ENDPOINT,
                "has_url_params": False,
                "body": None,
                "method": self.client.get
            },
            "create": {
                "url": constants.V_1_0_TAG_LIST_CREATE_ENDPOINT,
                "has_url_params": False,
                "body": self.get_body(),
                "method": self.client.post
            },
            "get": {
                "url": constants.V_1_0_TAG_ITEM_ENDPOINT,
                "has_url_params": True,
                "body": None,
                "method": self.client.get
            }
        }

    def get_body(self):
        body = {
            'title': self.title
        }

        if self.description:
            body['description'] = self.description

        if self.slug:
            body['slug'] = self.slug

        return body

    @staticmethod
    def get_list_body(tags):
        body = []

        for tag in tags:
            body.append(
                tag.get_body()
            )

        return body
