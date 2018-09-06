from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'easy2make',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'db', 
        'PORT': '3306'
    }
}