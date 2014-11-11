"""
Django settings for fitbucks project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from fitbucks.private import *
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['*']


'''-----------------------------------------------------------------------------
Applications 
-----------------------------------------------------------------------------'''
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registration',
    'crispy_forms',
    'django_email_changer',
    
    'fitbucks',
)

# django-registration
ACCOUNT_ACTIVATION_DAYS = 7
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# django_email_changer 
EMAIL_CHANGE_NOTIFICATION_SUBJECT = '[Email Update] - Please verify FitBucks email update'
EMAIL_CHANGE_NOTIFICATION_FROM = "FitBucks' Friendly Robot <fitbucks.team@gmail.com>"

'''-----------------------------------------------------------------------------
Middleware 
-----------------------------------------------------------------------------'''
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


'''-----------------------------------------------------------------------------
Static 
https://docs.djangoproject.com/en/1.7/howto/static-files/
-----------------------------------------------------------------------------'''
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = ( 
    os.path.join(BASE_DIR, 'static'),
)
STATICFILES_FINDERS = ( 
    'django.contrib.staticfiles.finders.FileSystemFinder', 
    'django.contrib.staticfiles.finders.AppDirectoriesFinder', 
) 


'''-----------------------------------------------------------------------------
FitBucks
-----------------------------------------------------------------------------'''
ROOT_URLCONF = 'fitbucks.urls'
WSGI_APPLICATION = 'fitbucks.wsgi.application'
DEFAULT_FROM_EMAIL = "FitBucks' Friendly Robot <fitbucks.team@gmail.com>"
LOGIN_URL = '/accounts/login/'


'''-----------------------------------------------------------------------------
Database 
https://docs.djangoproject.com/en/1.7/ref/settings/#databases
-----------------------------------------------------------------------------'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'fitbucks',
        'USER': 'fitbucks',
        'PASSWORD': 'fitbucks',
        'HOST': 'localhost',
        'PORT': '',
    }
}


'''-----------------------------------------------------------------------------
Template 
-----------------------------------------------------------------------------'''
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages'
)


'''-----------------------------------------------------------------------------
Internationalization
https://docs.djangoproject.com/en/1.6/topics/i18n/
-----------------------------------------------------------------------------'''
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True