from dotenv import load_dotenv

from pathlib import Path
from os import path,getenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


load_dotenv()


SECRET_KEY = str(getenv('SECRET_KEY'))


#Django all auth

#Auth django-allauth
SITE_ID = 1

SOCIALACCOUNT_LOGIN_ON_GET=True

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'login'

SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_HTTPONLY = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_SAVE_EVERY_REQUEST = True



if not(SECRET_KEY):
    exit(1)


ALLOWED_HOSTS = [
    "localhost",
]

#RENDER_EXTERNAL_HOSTNAME = environ.get('RENDER_EXTERNAL_HOSTNAME')if RENDER_EXTERNAL_HOSTNAME:    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


ROOT_URLCONF = 'back_core.urls'

WSGI_APPLICATION = 'back_core.wsgi.application'



# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_TZ = True

#CORS_ORIGIN_ALLOW_ALL =False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



SESSION_COOKIE_SECURE = True  # Asegurar que las cookies solo se envíen en conexiones HTTPS
SESSION_COOKIE_HTTPONLY = True  # Asegurar que las cookies solo sean accesibles a través de HTTP y no desde el cliente (Javascript)
CSRF_COOKIE_SECURE = True  # Asegurar que las cookies CSRF solo se envíen en conexiones HTTPS
CSRF_COOKIE_HTTPONLY = True  # Asegurar que las cookies CSRF solo sean accesibles a través de HTTP y no desde el cliente (Javascript)
