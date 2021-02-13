import os
# import dj_database_url
from .core import PROJECT_DIR, gettext

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DEBUG_TEMPLATE = True

# Allow all host headers
ALLOWED_HOSTS = ['*']

MIDDLEWARE = (
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'heroku_demo.urls'

WSGI_APPLICATION = 'heroku_demo.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Parse database configuration from $DATABASE_URL
#DATABASES['default'] =  dj_database_url.config()

# Enable Connection Pooling (if desired)
#DATABASES['default']['ENGINE'] = 'django_postgrespool'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# WHITENOISE_USE_FINDERS = True

# *************************************************************************
# *************************************************************************
# *************************** Fobi setup added ****************************
# *************************************************************************
# *************************************************************************

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = PROJECT_DIR('media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

LANGUAGES = (
    ('en', gettext("English")), # Main language!
    ('hy', gettext("Armenian")),
    ('nl', gettext("Dutch")),
    ('ru', gettext("Russian")),
    ('de', gettext("German")),
)

SITE_ID = 1

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'APP_DIRS': True,
        'DIRS': [PROJECT_DIR(os.path.join('..', 'templates'))],
        'OPTIONS': {
            'context_processors': [
                "django.template.context_processors.debug",
                'django.template.context_processors.request',
                "django.contrib.auth.context_processors.auth",
                # "django.core.context_processors.i18n",
                # "django.core.context_processors.media",
                # "django.core.context_processors.static",
                # "django.core.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                # 'django.template.loaders.eggs.Loader',
            ],
            'debug': DEBUG_TEMPLATE,
        }
    },
]

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # ***********************************************************************
    # ***********************************************************************
    # ********************** django-elasticsearch-dsl-drf *******************
    # ***********************************************************************
    # ***********************************************************************
    'rest_framework',  # REST framework
    'django_elasticsearch_dsl',  # Elasticsearch integration
    'corsheaders',  # For React demo
    # This app
    'django_elasticsearch_dsl_drf',
    'books',  # Test app
    'search_indexes',  # Search app
]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,
    'ORDERING_PARAM': 'ordering',
}


# Name of the Elasticsearch index
ELASTICSEARCH_INDEX_NAMES = {
    'search_indexes.documents.address': 'address',
    'search_indexes.documents.author': 'author',
    'search_indexes.documents.book': 'book',
    'search_indexes.documents.tag': 'tag',
    'search_indexes.documents.city': 'city',
    'search_indexes.documents.journal': 'journal',
    'search_indexes.documents.publisher': 'publisher',
    'search_indexes.documents.location': 'location',
}

ELASTICSEARCH_DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

try:
    from .local_settings import *
except ImportError as e:
    pass
