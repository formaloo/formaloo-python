from environs import Env

env = Env()
env.read_env()

try:
    from django.conf import settings

    V_1_0_API_BASE = getattr(settings, "FORMALOO_API_BASE", None)
    CLIENT_KEY = getattr(settings, 'FORMALOO_CLIENT_KEY', None)
    CLIENT_SECRET = getattr(settings, 'FORMALOO_CLIENT_SECRET', None)

except ModuleNotFoundError:
    V_1_0_API_BASE = None
    CLIENT_KEY = None
    CLIENT_SECRET = None


if V_1_0_API_BASE == None:
    V_1_0_API_BASE = env("FORMALOO_API_BASE", 'https://api.formaloo.net/v1.0/')

if CLIENT_KEY == None:
    CLIENT_KEY = env('FORMALOO_CLIENT_KEY')

if CLIENT_SECRET == None:
    CLIENT_SECRET = env('FORMALOO_CLIENT_SECRET', None)
