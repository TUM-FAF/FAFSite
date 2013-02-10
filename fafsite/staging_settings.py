# Django settings for fafsite project.
import os
gettext = lambda s: s
PROJECT_PATH = os.path.join( os.path.abspath(os.path.dirname(__file__)), '..').replace( '\\', '/' )

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

GRAPPELLI_ADMIN_TITLE = 'FAF website'

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'fafdb',
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'dev',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

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
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join( PROJECT_PATH ,"media" ).replace('\\', '/')

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
    os.path.join( PROJECT_PATH, 'static' ).replace( '\\', '/' ),
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
SECRET_KEY = 'fk-c@o%hyc9!p_nmf$9bnhe^(7qorpe+ug$yvagao#rd9k_jh^'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.i18n",
    'django.contrib.messages.context_processors.messages',
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
    os.path.join( PROJECT_PATH, 'templates' ).replace( '\\', '/' ),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    'django.contrib.messages.context_processors.messages',
)

GRAPPELLI_INDEX_DASHBOARD = 'fafsite.dashboard.CustomIndexDashboard'

# Email Service
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'faf.utm@gmail.com'
EMAIL_HOST_PASSWORD = 'vlad123qw'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'academics',
    'tinymce',
    'blog',
    'fafemail',
    # Uncomment the next line to enable the admin:
    'grappelli.dashboard',
    'grappelli',
    'filebrowser',
    'django.contrib.admin',
    'south',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
import sys
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console':{
            'level':'INFO',
            'class':'logging.StreamHandler',
            'stream': sys.stdout
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

TINYMCE_JS_URL = STATIC_URL + 'jscripts/tiny_mce/tiny_mce.js'

TINYMCE_JS_ROOT = STATIC_URL + 'jscripts/tiny_mce/'

TINYMCE_DEFAULT_CONFIG = { 
    'mode': "textareas", 
    'plugins': "advimage,media,advhr", 
    'theme': "advanced", 
    'convert_urls' : False, 
    'relative_urls' : False, 
    'cleanup_on_startup': True, 
    'force_p_newlines' : True, 
    'remove_linebreaks' : True, 
    'remove_trailing_nbsp' : True, 
    'theme_advanced_buttons1' : "bold,italic,underline,strikethrough,|,sub,sup,|,formatselect,|,bullist,numlist,link,unlink,code", 
    'theme_advanced_buttons1_add': 'image, media',
    'theme_advanced_buttons2' : 'undo,redo,preview,zoom,|,advhr,removeformat,visualaid', 
    'theme_advanced_buttons3' : '', 
    'theme_advanced_toolbar_align' : "center", 
    'valid_elements' : "a,sup,sub,strong,b,br,i,u,p,ul,ol,li,h1,h2,h3,h4,h5,@[align],object[data|type|align|width|height],param[name|value],embed[src|type|wmode|width|height,img[src|alt]],img[!src|border:0|alt|title|width|height|style],a[name|href|target|title|onclick]",
    'editor_deselector' : "mceNoEditor",
    'extended_valid_elements': "hr[class|width|size|noshade],img[!src|border:0|alt|title|width|height|style]"
    } 



try:
    from local_settings import *
except ImportError:
    print pass