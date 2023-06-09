from pathlib import Path

from decouple import config as env
from decouple import Csv as csv

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECRET_KEY
SECRET_KEY = env("SECRET_KEY")

# ALLOWED_HOSTS
ALLOWED_HOSTS = env("ALLOWED_HOSTS", cast=csv())

# DEBUG
DEBUG = env("DEBUG", default=False, cast=bool)

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
