from loguru import logger
from aiogram.types import ParseMode
from os import environ

API_TOKEN: str = environ.get('API_TOKEN')    # 'AAABBBCCC:12345'
ADMIN_ID: list = list(map(int, environ.get('ADMIN_ID').split()))    # [123, 456]
BAN_LIST: list = list(map(int, environ.get('BAN_LIST').split()))    # [321, 654]

# HIDE_SOURCE = True
DB_PATH = '_bot.db'

PM = ParseMode.MARKDOWN

"""Set log settings
loguru.loger.add(*args, **kwargs)
"""
LOG_FILE_NAME = "_bot.log"
LOG_MODE = "DEBUG"
MAX_LOG_FILE_SIZE = "10Mb"
COMPRESSION = "zip"

LOG = logger.add(LOG_FILE_NAME, level=LOG_MODE, rotation=MAX_LOG_FILE_SIZE, compression=COMPRESSION)
