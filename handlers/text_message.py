from misc import dp
from aiogram.types import ContentTypes, Message


@dp.message_handler(state='*', content_types=ContentTypes.TEXT)
async def any_message(message: Message):
    pass
