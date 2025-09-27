import os
from pathlib import Path
from datetime import timedelta
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'change-me')
DEBUG = os.environ.get('DEBUG', '1') == '1'
ALLOWED_HOSTS = ['*']
AUTH_USER_MODEL = 'users.User'
INSTALLED_APPS = [

    'django.contrib.admin','django.contrib.auth','django.contrib.contenttypes',
    'django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles',
    'rest_framework', "corsheaders",'users','billing','mikrotik','sms','packages', 
]
MIDDLEWARE = [ "corsheaders.middleware.CorsMiddleware",'django.middleware.security.SecurityMiddleware','django.contrib.sessions.middleware.SessionMiddleware',
'django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware',
'django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware',]
ROOT_URLCONF = 'core.urls'
TEMPLATES = [{'BACKEND': 'django.template.backends.django.DjangoTemplates','DIRS': [],'APP_DIRS': True,'OPTIONS': {'context_processors': ['django.template.context_processors.debug','django.template.context_processors.request','django.contrib.auth.context_processors.auth','django.contrib.messages.context_processors.messages'],},}]
WSGI_APPLICATION = 'core.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'isp-billing',    
        'USER': 'postgres',        
        'PASSWORD': 'password', 
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:4200",
]


AUTH_PASSWORD_VALIDATORS = []
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
STATIC_URL = '/static/'
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
from datetime import timedelta
SIMPLE_JWT = {'ACCESS_TOKEN_LIFETIME': timedelta(days=7)}
