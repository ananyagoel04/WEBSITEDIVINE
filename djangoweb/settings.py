"""
Django settings for djangoweb project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
from pathlib import Path
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


cloudinary.config(
    cloud_name="dzimskwuu",
    api_key="855474131666424",
    api_secret="FfG87alFoOawh1tZVd6FHWP0MR0",
)
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dzimskwuu',
    'API_KEY': '855474131666424',
    'API_SECRET': 'FfG87alFoOawh1tZVd6FHWP0MR0',
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.environ.get("SECRET_KEY","django-insecure-%(nl+y6lqvagxcj2qsgfl&1e%#xtrgrp8%vik*^am9j65g)l!1")#comment collectstatic

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", "False").lower() == "false" # comment collectstatic

if 'ALLOWED_HOSTS' in os.environ:
    ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(" ") #comment collectstatic
else:
    ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gallery',
    'tinymce',
    'about',
    'cloudinary',
    'cloudinary_storage',
    'TC',
    'djongo',
    'Parents',
]




TINYMCE_DEFAULT_CONFIG = {
    'plugins': 'link image code',
    'toolbar': 'undo redo | formatselect | bold italic backcolor | link image | code',
    'menubar': 'file edit view insert format tools table help',
    'toolbar_mode': 'floating',
}




MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

]

ROOT_URLCONF = 'djangoweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR,"templates"],
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

WSGI_APPLICATION = 'djangoweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'DWSDB',
#         'USER': 'ADMINDWS',
#         'PASSWORD': 'Divine2011',
#         'HOST': 'dwsdb.c7i6qkocud3x.ap-south-1.rds.amazonaws.com',
#         'PORT': '5432',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'DWSWEBCLUSTER',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'mongodb+srv://ananyagoel:hUAgixIgEEEPPiTJ@dwswebcluster.uyuegnq.mongodb.net/',
            'appName': 'DWSWEBCLUSTER'
        }
    }
}



# if 'DATABASE_URL' in os.environ:
#     # Production configuration using dj_database_url
#     database_url = os.environ.get("DATABASE_URL")#comment collectstatic
#     DATABASES["default"] = dj_database_url.parse(database_url) #comment collectstatic
# else:
#     # Local development configuration
#     DATABASES["default"] = dj_database_url.parse("postgres://database_a13g_user:tottQTAeLag5oyeePRdUTdciEkOlu8mt@dpg-cn06k5ed3nmc7389khf0-a.oregon-postgres.render.com/database_a13g")

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
(os.path.join(BASE_DIR, "static")),
]

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"



# settings.py

# Email settings for Gmail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtppro.zoho.in'
EMAIL_PORT = 587  # Use 465 if you are using SSL
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'info@divinewisdomschool.in'
EMAIL_HOST_PASSWORD = 'sg6ZRmnLjTNR'

# Default "from" address for email messages sent by Django
# DEFAULT_FROM_EMAIL = 'infoananya20@gmail.com'
# "From" address for error messages sent to the site administrators
# SERVER_EMAIL = 'infoananya20@gmail.com'
