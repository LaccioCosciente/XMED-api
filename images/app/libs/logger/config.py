
import sys
import os
import logging
from typing import Any, Dict
from datetime import datetime
from secrets import token_hex
from etc.config import Settings, PREFIX
from pythonjsonlogger import jsonlogger
from logging.handlers import WatchedFileHandler


class LogSettings(Settings):
    LOG_LEVEL: str = 'DEBUG'
    LOG_FILE: str = os.path.join(PREFIX, "var", "log", "main.log")



class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request_id = token_hex(8)

    def add_fields(
        self,
        log_record: Dict[str, Any],
        record: logging.LogRecord,
        message_dict: Dict[str, Any]
    ) -> None:
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        
        if not log_record.get('timestamp'):

            now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            log_record['timestamp'] = now

        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname
        log_record['request_id'] = self.request_id
        # log_record['line'] = f'{os.path.join(record.pathname, record.filename)}:{record.lineno}'
        log_record['line'] = f'{os.path.join(record.filename)}:{record.lineno}'


def get_logger():
    settings = LogSettings()

    if settings.DEVELOP:
        # log to stdout
        json_handler = logging.StreamHandler(sys.stdout)
    else:
        # log to file
        json_handler = WatchedFileHandler(settings.LOG_FILE)

    formatter = CustomJsonFormatter(
        fmt='%(timestamp)s %(request_id)s %(level)s %(message)s %(line)s'
    )
    json_handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(logging.getLevelName(settings.LOG_LEVEL))
    logger.addHandler(json_handler)
    return logger
