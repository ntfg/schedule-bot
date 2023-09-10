from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
menu_keyboard.add(KeyboardButton("Сегодня⤵️"))
menu_keyboard.add(KeyboardButton("Завтра➡️"))
menu_keyboard.add(KeyboardButton("Поменять класс🔄"))

remove_keyboard = ReplyKeyboardRemove()