from loguru import logger
from aiogram.types import ParseMode

API_TOKEN = ''

ADMIN_ID = []
BAN_LIST = []

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
