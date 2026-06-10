from decouple import config
import os
from pathlib import Path
import cloudinary_storage
import dj_database_url # For the Render database
import cloudinary
import cloudinary.uploader
import cloudinary.api
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY: Use an environment variable for the secret key on Render
SECRET_KEY = os.environ.get('SECRET_KEY', "django-insecure-xz($m)&nbzz!_5yexy_5j(9(xvyeq5n6^(s_#+jbml9xkyk%tk")

# SECURITY: Set to False in production
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# Add your Render URL here once you create the service
ALLOWED_HOSTS = ['.onrender.com', 'localhost', '127.0.0.1']
# Application definition

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    'cloudinary_storage',
    'cloudinary',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic", # For static files
    "django.contrib.humanize",
    "showroom",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware", # For static files
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "sarkin_mota.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'], # Added to ensure templates are found
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                'django.template.context_processors.debug',
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "sarkin_mota.wsgi.application"


# Database: Uses SQLite locally, PostgreSQL on Render
DATABASES = {
    'default': dj_database_url.config(
       default=f"sqlite:///{os.path.join(BASE_DIR, 'db.sqlite3')}",
        conn_max_age=600
    )
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# Static & Media Files
STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [BASE_DIR / "static"]

# # Static & Media Files
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / "static"]

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

# Temporary fallback to satisfy django-cloudinary-storage in Django 6.x
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
SECRET_KEY = config('SECRET_KEY', default='django-insecure-manual-backup-key-123')
DEBUG = config('DEBUG', default=True, cast=bool)

import cloudinary

# 1. Direct configuration for CloudinaryField
cloudinary.config( 
  cloud_name = "dcrqxoh29", 
  api_key = "251838683361349", 
  api_secret = "vWVr2yHFbii5ESAGjibineIFSdI",
  secure = True
)

# 2. Keep this for the storage engine
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dcrqxoh29',
    'API_KEY': '251838683361349',
    'API_SECRET': 'vWVr2yHFbii5ESAGjibineIFSdI',
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'