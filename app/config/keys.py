# Make this unique, and don't share it with anybody.
import os

SECRET_KEY = '^!6u6xecse2k@t7&3^q#k^erm$nnhu+wj!jf0=)m#244a-!b@&'

# Celery settings. For additional settings see bunnylove/celery.py
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER", "redis://redis:6379/0")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_BROKER", "db+postgresql://scott:tiger@localhost/mydatabase")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bot_db',
        'USER': 'postgres',
        'PASSWORD': 'GpvH0PF1aG',
        'HOST': 'db',
        'PORT': '5432',
        'OPTIONS': {
            'connect_timeout': 0,
        }
    },
}

