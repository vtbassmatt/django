# This is the MySQL test settings file for use with Azure Pipelines.
import os

CONTAINER_IP = os.environ['CONTAINER_IP']
BUILD_ID = os.environ['BUILD_BUILDID']
PY_VERSION = os.environ['PYTHON_VERSION']

MEMCACHED_PORT = '11211'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangoci',
        'USER': 'root',
        'PASSWORD': 'super-secret',
        'HOST': CONTAINER_IP,
        'PORT': '3306',
    },
    'other': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangociother',
        'USER': 'root',
        'PASSWORD': 'super-secret',
        'HOST': CONTAINER_IP,
        'PORT': '3306',
    }
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'memcached': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:%s' % MEMCACHED_PORT,
        'KEY_PREFIX': '%s_mysql_%s_memcached' % (PY_VERSION, BUILD_ID),
    },
    'pylibmc': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': '127.0.0.1:%s' % MEMCACHED_PORT,
        'KEY_PREFIX': '%s_mysql_%s_pylibmc' % (PY_VERSION, BUILD_ID),
    },
}

SECRET_KEY = "django_tests_secret_key"

# Use a fast hasher to speed up tests.
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

TEST_RUNNER = 'xmlrunner.extra.djangotestrunner.XMLTestRunner'
