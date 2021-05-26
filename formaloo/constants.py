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
