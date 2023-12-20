from config.settings.base import *  # NOQA

SECRET_KEY = "django-insecure-7rgppp1rbtvq)^ox*m=ngi4p=r@@8-pkw8g7b!#a-nac*mush+"

DEBUG = False

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # NOQA
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
