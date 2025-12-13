from pathlib import Path
import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================
# CORE SETTINGS
# ==============================
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-defaultkey')
DEBUG = os.getenv('DEBUG', 'False').lower() in ['true', '1', 't']
PROJECT_MODE = os.getenv('PROJECT_MODE', 'local')

# ==============================
# ALLOWED HOSTS
# ==============================
allowed_hosts_str = os.getenv('ALLOWED_HOSTS', '')
ALLOWED_HOSTS = [host.strip() for host in allowed_hosts_str.split(',') if host.strip()]

# ==============================
# TIMEZONE & LANGUAGE
# ==============================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = os.getenv('TIME_ZONE', 'UTC')
USE_I18N = True
USE_TZ = True

# ==============================
# APPLICATIONS
# ==============================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'web',
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

ROOT_URLCONF = 'ecocraft.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'ecocraft.wsgi.application'

# ==============================
# DATABASE CONFIGURATION (SUPABASE)
# ==============================
DATABASES = {
    'default': {
        'ENGINE': os.getenv('ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT', 5432),
        'OPTIONS': {
            'sslmode': os.getenv('DATABASE_SSL_MODE', 'require'),  # Enforce SSL
        },
    }
}

# ==============================
# PASSWORD VALIDATION
# ==============================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ==============================
# STATIC & MEDIA FILES
# ==============================
if PROJECT_MODE == 'production':
    STATIC_ROOT = BASE_DIR / "static"
    MEDIA_ROOT = BASE_DIR / "media"
else:
    STATICFILES_DIRS = [BASE_DIR / "static"]
    MEDIA_ROOT = BASE_DIR / "media"

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# ==============================
# DEFAULT AUTO FIELD
# ==============================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ==============================
# REST FRAMEWORK & JWT
# ==============================
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=365),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=365),
}

# ==============================
# EMAIL CONFIGURATION
# ==============================
EMAIL_BACKEND = os.getenv('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 465))
EMAIL_USE_SSL = os.getenv('EMAIL_USE_SSL', 'True').lower() in ['true', '1', 't']
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

# ==============================
# SECURITY SETTINGS
# ==============================
CSRF_TRUSTED_ORIGINS = [f"https://{host}" for host in ALLOWED_HOSTS if host not in ('localhost', '127.0.0.1')]
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# ==============================
# CORS
# ==============================
CORS_ORIGIN_ALLOW_ALL = True
