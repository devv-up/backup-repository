import json

from .base import *

with open(os.path.join(BASE_DIR, 'secrets.json')) as file:
    SECRETES = json.loads(file.read())

SECRET_KEY = SECRETES['SECRET_KEY']

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': SECRETES['MYSQL_HOST'],
        'NAME': SECRETES['MYSQL_NAME'],
        'USER': SECRETES['MYSQL_USER'],
        'PASSWORD': SECRETES['MYSQL_PASSWORD'],
    }
}