from .config_vars import BASE_DIR

DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'bd/db.sqlite3',
    }
}
