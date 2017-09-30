from .base import *

SECRET_KEY = '-o^f2!yq436m=&+*_gcbhv^gs4sp5r--2x!hc4_))f68u!=ffd'
DEBUG = True
ALLOWED_HOSTS = []
DATABASES = {'default': {'ENGINE': 'django.db.backends.postgresql_psycopg2',
                         'NAME': 'goodreads',
                         'USER': 'new_role',
                         'PASSWORD': 'goodreads123',
                         'HOST': 'localhost',
                         'PORT': '5432'
                         }
             }
