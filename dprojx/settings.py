from pathlib import Path
import os
# import sweetify
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR1 = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')
STATIC_DIR = os.path.join(BASE_DIR,'static')
MEDIA_DIR = os.path.join(BASE_DIR,'media')

SECRET_KEY = 'fg!)o@gunopk6&%-_$xi*xu*97cm&@!x8klug4^kq$-nx5jl9^'

DEBUG = True

ALLOWED_HOSTS = ['172.19.18.130','172.19.4.12','172.19.13.42','127.0.0.1', '192.168.43.35','cilbmrdt70823.cairnenergy.com',]
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'iapapp',
    'reset_migrations',
    'sweetify',
    'rest_framework',
    'widget_tweaks',
    'budget',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'iapapp.current_user.CurrentUserMiddleware',

]
# MIDDLEWARE_CLASSES = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

ROOT_URLCONF = 'dprojx.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,MEDIA_DIR,],
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

WSGI_APPLICATION = 'dprojx.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        # SQLITE
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR1 / 'IAP_DBase',
        'OPTIONS': {
            'timeout': 10,  # in seconds
            # see also
            # https://docs.python.org/3.7/library/sqlite3.html#sqlite3.connect
        }
        # ------------------------

        # 'ENGINE': 'django.db.backends.mysql', 
        # 'NAME': 'cairn_iap_tool',
        # 'USER': 'cmsans',
        # 'PASSWORD': 'Cairn_cmms',
        # 'HOST': '172.19.18.130',   # Or an IP Address that your DB is hosted on
        # 'PORT': '3306',
        # default-character-set = utf8,

    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'


STATICFILES_DIRS = [STATIC_DIR,]
MEDIA_ROOT = MEDIA_DIR
# STATIC_ROOT = STATIC_DIR
MEDIA_URL = '/media/'
LOGIN_URL = '/iapapp/user_login/'

AUTH_PROFILE_MODULE = 'accounts.UserProfileInfo'
# userprofileinfo.role

# APPEND_SLASH=False

# possible options: 'sweetalert', 'sweetalert2' - default is 'sweetalert2'
SWEETIFY_SWEETALERT_LIBRARY = 'sweetalert2'

# sweetify.DEFAULT_OPTS = {
#     'showConfirmButton': True,
#     'timer': 200,
#     'allowOutsideClick': True,
#     'confirmButtonText': 'OxxK',
# }


SESSION_SECURITY_EXPIRE_AFTER=6000   #1800
SESSION_SECURITY_WARN_AFTER=500      #1740

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 6000 # set just 10 seconds to test
SESSION_SAVE_EVERY_REQUEST = True


# SERIALIZATION_MODULES = {
#     'json': 'wadofstuff.django.serializers.json'
# }

MIDDLEWARE_CLASSES = (
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'current_user.CurrentUserMiddleware',
)