"""
Django settings for clothstore project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2&c8mudy$4y#s07b)#@gt9b*t8&difmn@5iuq8r%!cj)o%=c^i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
DEFAULT_TAX_RATE = 0.08 # 8%

DEFAULT_FROM_EMAIL = "Chimauche Njoku <njokuchimauche@gmail.com>"
try:
    from .email_settings import host, user, password
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_HOST_USER = "njokuchimauche@gmail.com"
    EMAIL_HOST_PASSWORD = "password"
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    # Application definition
except:
    pass    
    
SITE_URL = "https://codelumen.com"    
if DEBUG:
    SITE_URL = "http://127.0.0.1:8000"

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products',
    'carts',
    'orders',
    'accounts.apps.AccountsConfig',
    'marketing',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'marketing.middleware.DisplayMarketing',

]

ROOT_URLCONF = 'clothstore.urls'

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

WSGI_APPLICATION = 'clothstore.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''
DATABASES = {
    'default': {
        'ENGINE':  'django.db.backends.postgresql',
        'NAME': 'clothstore',
        'USER': 'postgres',
        'PASSWORD': 'roygbiv7',
        'HOST': '127.0.0.1',
        'PORT': ''
    }

}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "static", "media")

'''
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "media")
#MEDIA_ROOL = '/Users/ASUS/Documents/django/clothstore/static/media/'

STATIC_ROOT =  os.path.join(os.path.dirname(BASE_DIR), "static", "static_files"),

STATICFILES_DIR = [
     os.path.join(os.path.dirname(BASE_DIR), "static", "static_files"),
]
'''
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets', 'static_files')

STRIPE_SECRET_KEY = "sk_test_51HEDiTHehoWvxEUUTw0SHiZHoQVRFytNyIaySRUYkVXwHbcYv2Kn0UyQISmABI0LQ4Wlt2954shaMQ09BM0yaV0k000LDfXvgC"
STRIPE_PUBLISHABLE_KEY = "pk_test_51HEDiTHehoWvxEUUu82q7RCmNX50ABhIWAdBHx0HXLFYl8lr4pQr3RdX9jtUiWeMwrdlYwiWkrjenDdo9ge3VkoM00sG8PEStE"