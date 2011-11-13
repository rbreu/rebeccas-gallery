from settings import *
import logging

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'test.sqlite'),
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

LETTUCE_SERVER_PORT = 7000

INSTALLED_APPS += (
    'lettuce.django',
)

GLOBAL_LOG_LEVEL = logging.ERROR
