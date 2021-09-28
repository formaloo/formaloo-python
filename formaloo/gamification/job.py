from formaloo import constants, helper


class GamificationCalculationJob(helper.RequestHandler):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.actions = {
            "create": {
                "url": constants.V_1_0_CREATE_GAMIFICATION_CALCULATION_JOB,
                "has_url_params": False,
                "body": self.get_body(),
                "method": self.client.post
            }
        }
