from formaloo import constants, client, helper


class ActivityBatch(helper.RequestHandler):

    def __init__(self, activities=[]):
        self.client = client.client
        self.activities = activities
        self.actions = {
            "create": {
                "url": constants.V_1_0_ACTIVITY_BATCH_ENDPOINT,
                "has_url_params": False,
                "body": self.get_body(),
                "method": self.client.post
            }
        }

    def add_activity(self, activity):
        self.activities.append(activity)

    def get_body(self):
        body = {
            'activities_data': []
        }

        for activity in self.activities:
            body['activities_data'].append(
                activity.get_body()
            )

        return body
