from aiogram import types
from data import dbworks 
from misc import dp
from states import FirstTime
from keyboards.keyboards import main_kb as kb

@dp.message_handler(lambda msg: "Сегодня⤵️" in msg.text)
async def today(message: types.Message):
    await message.answer(dbworks.today(message["from"]["id"]))

@dp.message_handler(lambda msg: "Завтра➡" in msg.text)
async def tomorrow(message: types.Message):
    await message.answer(dbworks.tomorrow(message["from"]["id"]))
    
@dp.message_handler(lambda msg: "Поменять класс🔄" in msg.text)
async def change_class(message: types.Message):
    await FirstTime.which_class.set()
    await message.reply("Как скажете! Введите расписание какого класса желаете видеть")

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await FirstTime.which_class.set()
    await message.reply("Здравствуйте!\nВведите расписание какого класса вы желаете видеть")
    
@dp.message_handler(state=FirstTime.which_class)
async def which_class(message: types.Message()):
    if dbworks.change_class(message.text.strip("\n"), message["from"]["id"]):
        await FirstTime.next()
        await message.answer("Класс успешно выбран!", reply_markup=kb)
    else:
        await message.answer("Похоже, вы ошиблись")

@dp.message_handler()
async def tomorrow(message: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(types.KeyboardButton("Сегодня⤵️"),
           types.KeyboardButton("Завтра➡"),
           types.KeyboardButton("Поменять класс🔄"))
    
    await message.answer("Хм, лучше нажми на кнопку", reply_markup=kb)