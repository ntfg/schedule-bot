from aiogram.dispatcher.filters.state import StatesGroup, State

class FirstTime(StatesGroup):
    which_class = State()