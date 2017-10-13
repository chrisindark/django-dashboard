from mysite.settings.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wt!abdx2&^w_dh+$$ah*#hkz&ey+-7flz(je+m9qy*zb-n63n4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'salty-ridge-21622.herokuapp.com'
]

INSTALLED_APPS += (
    'django_extensions',
)

DATABASES = {}
if os.environ.get('HEROKU_ENV'):
    import dj_database_url

    DATABASES['default'] = dj_database_url.config(conn_max_age=500)
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, '../../db.sqlite3'),
        }
    }
