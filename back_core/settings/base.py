from .config_vars  import *
from .local import *
from itertools import chain


# Application definition

DJANGO_APPS=[
     'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
]

LOCAL_APPS=[
    'apps.administration_sc',
]

THIRDS_APPS=[
    'rest_framework',
    'dotenv',
]



INSTALLED_APPS = list(chain(DJANGO_APPS,LOCAL_APPS,THIRDS_APPS))

ALLOWED_HOSTS = ['administration-sc.onrender.com']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',#-Aqui lo elimina y no bloquea angular note
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
#    'django.contrib.sessions.middleware.SessionMiddleware',
#    'django.contrib.auth.middleware.AuthenticationMiddleware',  
    'corsheaders.middleware.CorsMiddleware',
    "corsheaders.middleware.CorsPostCsrfMiddleware",
]




               
CORS_ORIGIN_ALLOW_ALL = False



#CORS_ORIGIN_ALLOW = True

CORS_ORIGIN_WHITELIST = [
    'http://localhost:4200',
]



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


AUTHENTICATION_BACKENDS = [
'django.contrib.auth.backends.ModelBackend',
]