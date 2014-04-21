# coding=utf-8

DEBUG = TEMPLATE_DEBUG = True
ROOT_URLCONF = 'urls'

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        }
}
DEFAULT_INDEX_TABLESPACE = 'index'
SECRET_KEY = '123'
INSTALLED_APPS = (
    'notifier'
)
