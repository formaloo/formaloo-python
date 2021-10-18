

from typing import List, Dict

from formaloo import client


class RequestHandler:

    """
    actions example:
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
        }
    }
    """

    def __init__(self, **kwargs):
        self.client = client.Client()
        self.data = kwargs
        self.actions = {}

    def get_body(self):
        body = {}
        body.update(self.data)
        return body

    def validate(self, action, url_params):
        if action.get('has_url_params') and not url_params:
            raise ValueError(
                "`url_params` parameter is required."
            )

    @property
    def actions_list(self):
        return list(self.actions.keys())

    def __getattr__(self, attr):
        if attr not in self.actions_list:
            try:
                return getattr(self.__class__, attr)
            except Exception:
                raise AttributeError(
                    "{} has no attribute {}".format(
                            self.__class__.__name__,
                            attr
                        )
                    )
        self.received_action = attr
        return self._send_request

    def _send_request(
        self,
        url_params: List[str] = None,
        **kwargs
    ) -> Dict:
        """
        url_patrams: ["slug1", "slug2"]

        Example of using this method in projects:

        from formaloo.forms import Form
        form = Form()
        form.get_stats(
            url_params=['9fpTfgpR']
        )
        """

        action = self.actions.get(self.received_action)
        self.validate(action, url_params)

        url = action.get('url')
        request_data = {}

        if action['method'] in [
            self.client.get,
            self.client.delete
        ]:
            request_data['params'] = kwargs

        if action.get('body'):
            request_data['body'] = action.get('body')

        if action.get('has_url_params'):
            url = url.format(*url_params)

        response = action['method'](
            url,
            **request_data
        )

        # set some of response values as instance variables
        # set_from_response_data should set in action item
        if action.get('set_from_response_data'):
            for k, v in action.get('set_from_response_data').items():
                value = response.json()
                for key in v:
                    value = value.get(key)
                setattr(self, k, value)

        return response.json()
