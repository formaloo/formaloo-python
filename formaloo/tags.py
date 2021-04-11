from formaloo import constants, client


class Tag:
    def __init__(self, title, description=None, slug=None):
        self.client = client.Client()
        self.title = title
        self.description = description
        self.slug = slug

    def create(self):
        body = self.get_body()

        response = self.client.post(
            constants.V_1_0_CREATE_TAGS_ENDPOINT,
            body=body
        )

        return response

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
