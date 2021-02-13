import os
# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': os.environ['DATABASE_HOST'],
    }
}

# Elasticsearch configuration
ELASTICSEARCH_DSL = {
    'default': {
        'hosts': [os.environ['ELASTICSEARCH_HOST']],
        'timeout': 30,
    },
}
