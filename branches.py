from aiogram.dispatcher.filters.state import State, StatesGroup


class Branch(StatesGroup):
    default = State()
    banned = State()
    admin = State()
