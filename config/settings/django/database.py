"""
Database
https://docs.djangoproject.com/en/4.1/ref/settings/#databases
"""
from ..utils import BASE_DIR, env

DATABASES = {
    "default": env.db_url(
        default=f"sqlite:///{BASE_DIR}/db.sqlite3",
    ),
}
