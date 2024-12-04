from pathlib import Path
from os import getenv, path

from django.conf.global_settings import DEFAULT_FROM_EMAIL
from dotenv import load_dotenv

from .base import * #noqa

from .base import BASE_DIR

local_env_file = path.join(BASE_DIR, '.envs', ".env.local")

if path.isfile(local_env_file):
    load_dotenv(local_env_file)

SECRET_KEY = getenv(
    'DJANGO_SECRET_KEY',
)

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = []

ADMIN = [('Gene higgins', 'hi@genehiggins.com'), ]
