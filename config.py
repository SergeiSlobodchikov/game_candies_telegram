from aiogram import Bot, Dispatcher
import os

# bot = Bot(os.environ['PYTHONUNBUFFERED'])
bot = Bot(os.getenv('Token_candies'))
dp = Dispatcher(bot)