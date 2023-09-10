import timework 
import textwork
from loader import dp, db, FSMContext
from aiogram import types
from aiogram.dispatcher.filters import Text
from states import *
from keyboards import *


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    if db.user_exists(message.from_id):
        await message.answer("Добро пожаловать!",
                             reply_markup=menu_keyboard)
    else:
        await message.answer("Добро пожаловать в бот с раписанием!\nВыберите свой класс")
        await ChooseClass.user_class.set()
        

@dp.message_handler(state=ChooseClass.user_class)
async def choose_class(message: types.Message, state: FSMContext):
    user_class = message.text.strip()
    
    if db.class_exists(user_class):
        db.update_class(message.from_id, user_class)
        await message.answer("Отлично! Можете смотреть расписание",
                             reply_markup=menu_keyboard)
        await state.finish()
    else:
        await message.answer("Вы ошиблись, такого класса не найдено\n" +
                              "Правильное написание: КлассБуква (к примеру, 7А")


@dp.message_handler(Text(equals="Поменять класс🔄"))
async def change_class(message: types.Message):
    await ChooseClass.user_class.set()
    await message.answer("Выберите класс, расписание которого вы желаете видеть",
                         reply_markup=remove_keyboard)


@dp.message_handler(Text(equals="Сегодня⤵️"))
async def today(message: types.Message):
    schedule = db.get_schedule(message.from_id, timework.get_weekday())
    if schedule:
        textwork.format_schedule(schedule)
    else:
        await message.answer("Выходной😴")
        

@dp.message_handler(Text(equals="Завтра➡️"))
async def tomorrow(message: types.Message):
    schedule = db.get_schedule(message.from_id, timework.get_weekday(tomorrow=True))
    if schedule:
        await message.answer(textwork.format_schedule(schedule))
    else:
        await message.answer("Выходной😴")

        
    
    