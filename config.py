from aiogram import Bot, Dispatcher
import os

bot = Bot(os.getenv('Token_candies'))
dp = Dispatcher(bot)
