"""
Django settings for UNRCE project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os 
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*4#w1xtd7#hfw_kyd$(4pwlv&@uv9xbzgxg8!e1d-g9dp!r@p7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['3.24.216.179','.localhost', '127.0.0.1', '[::1]']


# Application definition

INSTALLED_APPS = [
    "UNRCE_APP",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'captcha',
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

ROOT_URLCONF = 'UNRCE.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'UNRCE.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'dbmaster',
#         'USER': 'dbmasteruser',
#         'PASSWORD': ',Yy8N0jC<&7.,7m*kUH)TKsU_(I!j`]D',
#         'HOST': 'ls-99842c38855ffa2f97fb191db94cd898aae44b20.c5c4ycagorbe.ap-southeast-2.rds.amazonaws.com',  # or the hostname where your MySQL server is running
#         'PORT': '3306',      # or the port on which your MySQL server is listening
#         'OPTIONS': {
#             'init_command': 'SET sql_mode="STRICT_ALL_TABLES"',
#         },
#     }
# }



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / "db.sqlite3"),
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

LANGUAGE_CODE = 'en-au'

TIME_ZONE = 'AWST'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'UNRCE_APP/static/'	
STATICFILES_DIRS = [os.path.join(BASE_DIR, "UNRCE_APP/static"),]
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MEDIA_ROOT = BASE_DIR / "images"
MEDIA_URL = "/media/"
LOGIN_REDIRECT_URL = 'UNRCE_APP:index'

#Point django to new user model 
AUTH_USER_MODEL = 'UNRCE_APP.CustomUser'

#Point django to new authentication backend
AUTHENTICATION_BACKENDS = ['UNRCE_APP.backends.EmailBackend']











