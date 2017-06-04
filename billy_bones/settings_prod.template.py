import os
from .settings import *

SECRET_KEY = '{{ django_secret_key }}'
DEBUG = False
ALLOWED_HOSTS = ['{{ django_host }}']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '{{ django_db.name }}',
        'HOST': '{{ django_db.host }}',
        'USER': '{{ django_db.user }}',
        'PASSWORD': '{{ django_db.password }}'
    }
}

MANIFEST_PATH = os.path.join(BASE_DIR, 'home', 'static', 'manifest.json')
STATIC_ROOT = '{{ django_staticroot }}'

for lgr in LOGGING['loggers'].values():
    lgr['handlers'] = ['file']
