from aiogram import types


# Главная клавиатура
main_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.add(types.KeyboardButton("Сегодня⤵️"),
        types.KeyboardButton("Завтра➡"),
        types.KeyboardButton("Поменять класс🔄"))