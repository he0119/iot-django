""" Test settings
"""
import os

SECRET_KEY = os.getenv('SECRET_KEY') or 'This is a very strong key'
DEBUG = False
ALLOWED_HOSTS = '*'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'timescaledb',
        'PORT': '5432',
    }
}
