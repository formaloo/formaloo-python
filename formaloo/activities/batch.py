from formaloo import constants, client


class ActivityBatch:

    def __init__(self, activities=[]):
        self.client = client.client
        self.activities = activities

    def add_activity(self, activity):
        self.activities.append(activity)

    def create(self):
        body = self.get_body()

        response = self.client.post(
            constants.V_1_0_ACTIVITY_BATCH_ENDPOINT,
            body=body
        )

        return response.json()

    def get_body(self):
        body = {
            'activities_data': []
        }

        for activity in self.activities:
            body['activities_data'].append(
                activity.get_body()
            )

        return body
