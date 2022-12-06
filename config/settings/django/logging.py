"""
Logging in Django:
* https://docs.djangoproject.com/en/dev/topics/logging/
* https://docs.djangoproject.com/en/dev/howto/logging/
* https://docs.djangoproject.com/en/dev/ref/logging/
"""
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "formatters": {
        "django": {
            "()": "django.utils.log.ServerFormatter",
            "datefmt": "%Y-%m-%d %H:%M:%S %z",
            "format": "{asctime} | {levelname:8} | {module}:<{funcName}>:{lineno} {message}",
            "style": "{",
        }
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "django",
        },
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "mail_admins"],
            "level": "INFO",
        },
    },
}
