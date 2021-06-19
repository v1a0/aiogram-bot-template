from misc import dp
from branches import Branch
from aiogram import types
from messages import MESSAGES
from settings import BAN_LIST


@dp.message_handler(state=Branch.banned)
async def start(message: types.Message):
    return


@dp.message_handler(state='*', commands=['start', 'about'])
async def start(message: types.Message):
    if message.from_user.id in BAN_LIST:
        return

    await message.reply(MESSAGES['start'], reply=False)




