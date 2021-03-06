"""
Django settings for django_thecodebase project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

def load_config(path):
    import json
    with open(path) as f_obj:
        return json.load(f_obj)


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONFIG_FILE = os.path.join(BASE_DIR, 'config.json')
if os.path.isfile(CONFIG_FILE):
    CONFIG_DICT = load_config(CONFIG_FILE)
else:
    CONFIG_DICT = {}


CELERY_BROKER_URL = 'amqp://localhost//'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = CONFIG_DICT.get('SECRET_KEY') or 'secret_key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = not bool(CONFIG_DICT)

if not DEBUG:
    # Production settings only
    ALLOWED_HOSTS = CONFIG_DICT['ALLOWED_HOSTS']
    # https://docs.djangoproject.com/en/2.2/ref/middleware/#http-strict-transport-security
    SECURE_HSTS_SECONDS = 600
    # https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-SECURE_CONTENT_TYPE_NOSNIFF
    SECURE_CONTENT_TYPE_NOSNIFF = True
    # https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-SECURE_BROWSER_XSS_FILTER
    SECURE_BROWSER_XSS_FILTER = True
    # https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-SECURE_SSL_REDIRECT
    SECURE_SSL_REDIRECT = True
    # https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-SESSION_COOKIE_SECURE
    SESSION_COOKIE_SECURE = True
    # https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-CSRF_COOKIE_SECURE
    CSRF_COOKIE_SECURE = True
    # https://docs.djangoproject.com/en/2.2/ref/clickjacking/
    X_FRAME_OPTIONS = 'DENY'
    # https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-SECURE_HSTS_PRELOAD
    SECURE_HSTS_PRELOAD = True
    # https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-SECURE_HSTS_INCLUDE_SUBDOMAINS
    # WARNING: Setting this incorrectly can irreversibly (for the value of SECURE_HSTS_SECONDS) break your site.
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True

    # https://docs.djangoproject.com/en/3.0/ref/middleware/#referrer-policy
    SECURE_REFERRER_POLICY = 'same-origin'


    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
            },
        },
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': CONFIG_DICT['LOG_FILE'],
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file'],
                'level': 'DEBUG',
                'propagate': True,
                'formatter': 'verbose',
            },
        },
    }


else:
    # Development settings
    ALLOWED_HOSTS = [
        '127.0.0.1',
        'localhost',
    ]
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'level': 'INFO',
                'propagate': True,
            },
        },
    }


# Application definition

INSTALLED_APPS = [
    'main',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_thecodebase.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'main', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'main.context_processors.default_context',
                'main.context_processors.topics',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_thecodebase.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


DEFAULT_DB_CONF = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'thecodebase',
}

if CONFIG_DICT.get('POSTGRESQL'):
    DEFAULT_DB_CONF.update(CONFIG_DICT.get('POSTGRESQL'))

DATABASES = {
    'default': DEFAULT_DB_CONF
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'STATIC')

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'main', "static"),
]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

LOGIN_REDIRECT_URL = 'main/home'
LOGOUT_REDIRECT_URL = 'main/home'
