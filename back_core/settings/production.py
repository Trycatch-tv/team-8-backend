DEBUG = True

#Database Production

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'administration_sc',
        'USER': 'postgresql',
        'PASSWORD': 'dentreaca1',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}