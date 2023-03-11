import os

ALLOWED_HOSTS = os.environ['DJANGO_ALLOWED_HOSTS'].split(' ')
CSRF_TRUSTED_ORIGINS = ['https://negrucoin.ru']

CORS_ORIGIN_WHITELIST = [
    'http://localhost:5173',
]

CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS'
]
