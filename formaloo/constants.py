from .settings import V_1_0_API_BASE

# ENDPOINTS
V_1_0_AUTHORIZATION_TOKEN_ENDPOINT = '%soauth2/authorization-token/' % V_1_0_API_BASE

V_1_0_ACTIVITY_LIST_CREATE_ENDPOINT = '%sactivities/' % V_1_0_API_BASE
V_1_0_ACTIVITY_ITEM_ENDPOINT = '%sactivities/{}/' % V_1_0_API_BASE
V_1_0_ACTIVITY_BATCH_ENDPOINT = '%sactivities/batch/' % V_1_0_API_BASE

V_1_0_CUSTOMER_LIST_CREATE_ENDPOINT = '%scustomers/' % V_1_0_API_BASE
V_1_0_CUSTOMER_ITEM_ENDPOINT = '%scustomers/{}/' % V_1_0_API_BASE
V_1_0_CUSTOMER_BATCH_ENDPOINT = '%scustomers/batch/' % V_1_0_API_BASE

V_1_0_TAG_LIST_CREATE_ENDPOINT = '%stags/' % V_1_0_API_BASE
V_1_0_TAG_ITEM_ENDPOINT = '%stags/{}/' % V_1_0_API_BASE

V_1_0_CREATE_GAMIFICATION_CALCULATION_JOB = '%sgamification-calculation-jobs/' % V_1_0_API_BASE

V_1_0_FORM_LIST_CREATE_ENDPOINT = '%sforms/' % V_1_0_API_BASE
V_1_0_FORM_ITEM_ENDPOINT = '%sforms/{}/' % V_1_0_API_BASE
V_1_0_FORM_STATS_ENDPOINT = '%sforms/{}/stats/' % V_1_0_API_BASE
V_1_0_FORM_ROWS_LIST = '%sforms/{}/rows/' % V_1_0_API_BASE

V_1_0_FORM_DISPLAY_ADDRESS_ENDPOINT = '%sform-displays/address/{}/' % V_1_0_API_BASE
V_1_0_FORM_DISPLAY_SLUG_ENDPOINT = '%sform-displays/slug/{}/' % V_1_0_API_BASE
V_1_0_FORM_DISPLAY_SUBMIT_ENDPOINT = '%sform-displays/slug/{}/submit/' % V_1_0_API_BASE


V_1_0_FIELD_LIST_CREATE_ENDPOINT = '%sfields/' % V_1_0_API_BASE
V_1_0_FIELD_ITEM_ENDPOINT = '%sfields/{}/' % V_1_0_API_BASE


V_1_0_FORM_CATEGORY_LIST_CREATE_ENDPOINT = '%sforms/category/' % V_1_0_API_BASE
V_1_0_FORM_CATEGORY_ITEM_ENDPOINT = '%sforms/category/{}/' % V_1_0_API_BASE


V_1_0_FORM_TEMPLATE_LIST_ENDPOINT = '%sforms/templates/' % V_1_0_API_BASE
V_1_0_FORM_ROW_TAGS_LIST_CREATE_ENDPOINT = '%sforms/{}/row-tags/' % V_1_0_API_BASE
V_1_0_FORM_ROW_TAG_ITEM_ENDPOINT = '%sforms/{}/row-tags/{}/' % V_1_0_API_BASE


V_1_0_ROW_VOTE_LIST_CREATE_ENDPOINT = '%slive-dashboards/{}/rows/{}/votes/' % V_1_0_API_BASE
V_1_0_ROW_VOTE_ITEM_ENDPOINT = '%slive-dashboards/{}/rows/{}/votes/{}/' % V_1_0_API_BASE

V_1_0_PAYMENT_METHOD_LIST_CREATE_ENDPOINT = '%spayment-methods/' % V_1_0_API_BASE
V_1_0_PAYMENT_METHOD_ITEM_ENDPOINT = '%spayment-methods/{}/' % V_1_0_API_BASE


# HEADERS
APPLICATION_HEADER = 'x-api-key'
AUTHORIZATION_HEADER = 'Authorization'
AUTHORIZATION_BEARER = 'JWT'
CREDENTIAL_BEARER = 'Basic'
CREDENTIAL_GRAT_TYPE = 'client_credentials'

# Settings
AUTHORIZATION_TOKEN_TIMEOUT = 5*60

# Helpers
CUSTOMER_BASE_FIELDS = [
    'first_name',
    'last_name',
    'full_name',
    'email',
    'phone_number',
    'score',
    'city',
    'language',
    'created_at',
    'code',
    'username'
]
