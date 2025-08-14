import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

load_dotenv()  # reads .env if present

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY", "dev-please-change")
DEBUG = os.getenv("DEBUG", "0").lower() in ("1", "true", "yes")
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split(",")

# Apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # your apps…
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # serve static
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
WSGI_APPLICATION = "backend.wsgi.application"

# Database (Postgres in prod, SQLite fallback locally/build)
default_sqlite_url = "sqlite:///" + str(BASE_DIR / "db.sqlite3")
db_url = os.getenv("DATABASE_URL", default_sqlite_url)

is_postgres = db_url.startswith(("postgres://", "postgresql://"))
ssl_require_flag = os.getenv("DB_SSL_REQUIRE", "0").lower() in ("1", "true", "yes")

if is_postgres:
    DATABASES = {
        "default": dj_database_url.parse(
            db_url,
            conn_max_age=600,
            ssl_require=ssl_require_flag,  # only for Postgres
        )
    }
else:
    # SQLite path without sslmode
    DATABASES = {"default": dj_database_url.parse(db_url)}

# Static files
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Security (production hardening; safe defaults)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
CSRF_TRUSTED_ORIGINS = os.getenv("CSRF_TRUSTED_ORIGINS", "").split(",") if os.getenv("CSRF_TRUSTED_ORIGINS") else []
