from formaloo import constants, client


class Tag:

    def __init__(self, title=None, description=None, slug=None):
        self.client = client.client
        self.title = title
        self.description = description
        self.slug = slug

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

    def get_list(self, **kwargs):
        params = kwargs

        response = self.client.get(
            constants.V_1_0_TAG_LIST_CREATE_ENDPOINT,
            params=params
        )

        return response.json()

    def create(self):
        if not self.title:
            raise ValueError("`title` is required to create a tag!")

        body = self.get_body()

        response = self.client.post(
            constants.V_1_0_TAG_LIST_CREATE_ENDPOINT,
            body=body
        )

        return response.json()

    def get(self, slug, **kwargs):
        params = kwargs

        response = self.client.get(
            constants.V_1_0_TAG_ITEM_ENDPOINT.format(slug),
            params=params
        )

        return response.json()
