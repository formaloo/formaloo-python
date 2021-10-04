from environs import Env

try:
    from django.conf import settings

    V_1_0_API_BASE = getattr(settings, "FORMALOO_API_BASE", None)
    CLIENT_KEY = getattr(settings, 'FORMALOO_CLIENT_KEY', None)
    CLIENT_SECRET = getattr(settings, 'FORMALOO_CLIENT_SECRET', None)

except ModuleNotFoundError:
    env = Env()
    env.read_env()
    V_1_0_API_BASE = env("FORMALOO_API_BASE", 'https://api.formaloo.net/v1.0/')
    CLIENT_KEY = env('FORMALOO_CLIENT_KEY')
    CLIENT_SECRET = env('FORMALOO_CLIENT_SECRET', None)
