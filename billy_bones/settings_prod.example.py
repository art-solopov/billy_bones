import os
from .settings import *

# Fill the blanks!

SECRET_KEY = '{}'
DEBUG = False
ALLOWED_HOSTS = ['{}']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '{}',
        'HOST': '{}',
        'USER': '{}',
        'PASSWORD': '{}'
    }
}

for lgr in LOGGING['loggers'].values():
    lgr['handlers'] = ['file']
