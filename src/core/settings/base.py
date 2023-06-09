# Imports
import os
from pathlib import Path
from decouple import config as env
from decouple import Csv as csv

# BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")

# Production
PRODUCTION = env("PRODUCTION", default=False, cast=bool)


# Application definition

# LOCAL_APPS
LOCAL_APPS = [
    "common",
    "backend",
    "frontend",
]

THIRD_PARTY_APPS = [
    "rest_framework",
]

THEME_APPS = [
    "jazzmin",
]

INSTALLED_APPS = [
    *THEME_APPS,
    "django.contrib.auth",
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    *THIRD_PARTY_APPS,
    *LOCAL_APPS,
]

# MIDDLEWARE
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

LANGUAGE_CODE = "ru-RU"

TIME_ZONE = "Asia/Bishkek"

DATE_FORMAT = "%Y-%m-%d"
USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files
STATIC_URL = "/back_static/"
STATIC_ROOT = os.path.join(BASE_DIR, "back_static")

# Media files
MEDIA_URL = "/back_media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "back_media")
X_FRAME_OPTIONS = "SAMEORIGIN"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

EXTRA_SMALL_THUMBNAIL_SIZE = 100, 100
SMALL_THUMBNAIL_SIZE = 512, 512
MEDIUM_THUMBNAIL_SIZE = 1024, 1024
BIG_THUMBNAIL_SIZE = 1400, 1400

# Celery settings
CELERY_BROKER_URL = env("CELERY_BROKER")
CELERY_RESULT_BACKEND = env("CELERY_BACKEND")
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_SERIALIZER = "json"


REST_FRAMEWORK = {
    "PAGE_SIZE": 13,
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
}

# ALLOWED_HOSTS
ALLOWED_HOSTS = env("ALLOWED_HOSTS", cast=csv())

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT", cast=int),
    }
}

from .themes import *
from .cors import *

# if not PRODUCTION:
#     from .local import *
# else:
#     from .production import *


# REDIS_URL = "redis://redis:6370"
