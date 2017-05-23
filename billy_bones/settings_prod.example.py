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

MANIFEST_PATH = os.path.join(BASE_DIR, 'home', 'static', 'manifest.json')
STATIC_ROOT = os.path.join(BASE_DIR, '__static')

for lgr in LOGGING['loggers'].values():
    lgr['handlers'] = ['file']
