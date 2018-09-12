# This is the MySQL test settings file for use with VSTS CI.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangoci',
        'USER': 'root',
        'PASS': 'super-secret',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    },
    'other': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangociother',
        'USER': 'root',
        'PASS': 'super-secret',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

SECRET_KEY = "django_tests_secret_key"

# Use a fast hasher to speed up tests.
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

TEST_RUNNER = 'xmlrunner.extra.djangotestrunner.XMLTestRunner'
