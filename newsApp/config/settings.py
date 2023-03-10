"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from imaplib import _Authenticator
from optparse import SUPPRESS_USAGE
from pathlib import Path
from urllib import request

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-s#p1jkdsb0%*!du4+u=7=_h16si(8j=0&+d-y9p0u5bw%^cmqr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
2
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms', #new
    'accounts', #new
    'pages',#new
    'articles', #new
]

TIME_ZONE = 'Africa/Casablanca'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
        'DIRS':[str(BASE_DIR.joinpath('templates'))], #NEW
    },
]

WSGI_APPLICATION = 'config.wsgi.application'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
        'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'your db',  
        'USER': 'django',  
        'PASSWORD': 'your code',  
        'HOST': 'localhost',  
        'PORT': '3306',  
        'OPTIONS': {  
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
                }
        }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [str(BASE_DIR.joinpath('static'))]
STATIC_ROOT = STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

AUTH_USER_MODEL =  'accounts.CustomUser' #new
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# send reset password email 


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'your email' 
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True

