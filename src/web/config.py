from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()

bot = Bot(config("BOT_TOKEN"))
dp = Dispatcher(bot=bot, storage=MemoryStorage())
