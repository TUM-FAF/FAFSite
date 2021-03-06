# Django settings for fafsite project.
import os

gettext = lambda s: s
PROJECT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                            '..').replace('\\', '/')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
# ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'fafdb.sqlite',
    },
    'test': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test_fafdb.sqlite',
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Chisinau'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, "..", "media").replace('\\', '/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static').replace('\\', '/'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '78z34cm8gu-kaup)y0at9amy7qk-xb=@fc&8jkkpr7z95yw6$i'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'fafsite.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'fafsite.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates').replace('\\', '/'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# GRAPPELLI_INDEX_DASHBOARD = 'fafsite.dashboard.CustomIndexDashboard'

# Email Service
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'faf.utm@gmail.com'
EMAIL_HOST_PASSWORD = ''

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'general',
    'academics',
    'tinymce',
    'blog',
    'fafemail',
    'fafauth',
    'fafside',
    'faflabs',
    'grappelli',
    'django_pdb',
    'django.contrib.admin',
    'django_nose',
    'south',
    'social_auth',
    'crispy_forms',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Google Auth Keys
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)
SOCIAL_AUTH_ENABLED_BACKENDS = ('google-oauth2')
GOOGLE_OAUTH2_CLIENT_ID = '419507287308-orkvgvpjrpv76j426k7avcr4smgvcg1a.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET = 'brbZFaFSfTRgQQcx7XjT1cq2'
GOOGLE_OAUTH2_USE_UNIQUE_USER_ID = True
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/'




TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# TINYMCE_JS_URL = STATIC_URL + 'jscripts/tiny_mce/tiny_mce.js'

# TINYMCE_JS_ROOT = STATIC_URL + 'jscripts/tiny_mce/'

# TINYMCE_DEFAULT_CONFIG = {
#     'mode': "textareas",
#     'plugins': "advimage,media,advhr",
#     'theme': "advanced",
#     'convert_urls' : False,
#     'relative_urls' : False,
#     'cleanup_on_startup': True,
#     'force_p_newlines' : True,
#     'remove_linebreaks' : True,
#     'remove_trailing_nbsp' : True,
#     'theme_advanced_buttons1' : "bold,italic,underline,strikethrough,|,sub,sup,|,formatselect,|,bullist,numlist,link,unlink,code",
#     'theme_advanced_buttons1_add': 'image, media',
#     'theme_advanced_buttons2' : 'undo,redo,preview,zoom,|,advhr,removeformat,visualaid',
#     'theme_advanced_buttons3' : '',
#     'theme_advanced_toolbar_align' : "center",
#     'valid_elements' : "a,sup,sub,strong,b,br,i,u,p,ul,ol,li,h1,h2,h3,h4,h5,@[align],object[data|type|align|width|height],param[name|value],embed[src|type|wmode|width|height,img[src|alt]],img[!src|border:0|alt|title|width|height|style],a[name|href|target|title|onclick]",
#     'editor_deselector' : "mceNoEditor",
#     'extended_valid_elements': "hr[class|width|size|noshade],img[!src|border:0|alt|title|width|height|style]"
#     }
