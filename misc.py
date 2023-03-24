from aiogram import Bot, Dispatcher, executor, types 
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage  
from dotenv import load_dotenv
import os

load_dotenv()  

bot = Bot(token=os.environ["BOT_TOKEN"])
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)