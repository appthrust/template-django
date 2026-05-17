import os
SECRET_KEY = os.getenv('SECRET_KEY', 'appthrust-dev-secret')
DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'
ALLOWED_HOSTS = ['*']
ROOT_URLCONF = 'app.urls'
MIDDLEWARE = []
INSTALLED_APPS = []
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': ':memory:'}}
