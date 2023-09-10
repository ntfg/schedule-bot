from aiogram.dispatcher.filters.state import StatesGroup, State

class ChooseClass(StatesGroup):
    user_class = State()