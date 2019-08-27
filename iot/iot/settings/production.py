""" Production settings
"""
import os

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = '*'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'iot',
        'USER': 'postgres',
        'PASSWORD': os.getenv('POSTGRESQL_PASSWORD'),
        'HOST': 'timescaledb',
        'PORT': '5432',
    }
}
