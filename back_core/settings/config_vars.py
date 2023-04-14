from dotenv import load_dotenv

from pathlib import Path
from os import path,getenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()


SECRET_KEY = str(getenv('SECRET_KEY'))


if not(SECRET_KEY):
    exit(1)


ALLOWED_HOSTS = [
]

ROOT_URLCONF = 'back_core.urls'

WSGI_APPLICATION = 'back_core.wsgi.application'



# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
