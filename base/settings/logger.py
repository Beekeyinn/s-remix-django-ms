import os
from pathlib import Path

from base.settings.base import PROJECT_APPS

# BASE_DIR = Path(__file__).resolve().parent.parent.parent

# LOGGING_DIR = os.path.join(BASE_DIR, "logs")

# if not os.path.exists(LOGGING_DIR):
#     os.makedirs(LOGGING_DIR)

handlers = {
    "all_logs": {
        "class": "logging.handlers.TimedRotatingFileHandler",
        "level": "INFO",
        "filename": f"logs/all_logs.log",
        "formatter": "file_formatter",
        "when": "midnight",
        "interval": 1,
        "backupCount": 7,
        "encoding": "utf-8",
        "delay": True,
    },
    "console": {
        "class": "logging.StreamHandler",
        "level": "DEBUG",
        "formatter": "console_formatter",
    },
}
loggers = {
    "django": {
        "handlers": ["all_logs", "console"],
        "level": "WARNING",
        "propagate": False,
    },
    "": {
        "handlers": ["all_logs", "console"],
        "level": "INFO",
        "propagate": False,
    },
}

for app in PROJECT_APPS:
    handlers[f"{app.split('.')[1]}_file_handler"] = {
        "class": "logging.handlers.TimedRotatingFileHandler",
        "level": "INFO",
        "filename": f"logs/apps/{app.split('.')[1]}.log",
        "formatter": "file_formatter",
        "when": "midnight",
        "interval": 1,
        "backupCount": 7,
        "encoding": "utf-8",
        "delay": True,
    }
    loggers[f"{app.split('.')[1]}"] = {
        "handlers": [f"{app.split('.')[1]}_file_handler", "console"],
        "level": "DEBUG",
        "propagate": False,
    }

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console_formatter": {"format": "{message}", "style": "{"},
        "file_formatter": {
            "format": "{levelname}:{asctime} \n\tModule: {module} \n\tFilePath: {pathname} \n\tFunction Name: {funcName} \n\tLine No: {lineno} \n\tMessage: {message}",
            "style": "{",
        },
    },
    "handlers": handlers,
    "loggers": loggers,
}
