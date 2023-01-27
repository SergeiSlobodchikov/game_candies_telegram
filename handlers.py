from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from config import dp
import text
import game_candies
import random

@dp.message_handler(commands=['start'])
async def on_start(message: Message):
   await message.answer(text=f"{message.from_user.first_name}" + f'{text.greeting}')

@dp.message_handler(commands='new_game')
async def start_new_game(message: Message):
  game_candies.new_game()
  if game_candies.check_game():
    toss = random.choice([False, True])
    if toss: 
      await player_turn(message)
    else:
      await bot_turn(message)

async def player_turn(message: Message):
  await message.answer(f'{message.from_user.first_name} {text.step}')

@dp.message_handler()
async def take(message: Message):
  name = message.from_user.first_name
  if game_candies.check_game():
    if message.text.isdigit():
      take = int(message.text)
      if (0 < take < 29) and take <= game_candies.get_total() :
        game_candies.take_candies(take)
        if await who_won(message, take,'player'):
          return
        await message.answer(f'{name} взял {take} {text.take_people} '
                             f'{int(game_candies.get_total())} {text.robot}')
        await bot_turn(message)
      else:
        await message.answer(text.error)
    else:
      pass

async def bot_turn(message):
  total = game_candies.get_total()
  if 28 >= total:
    take = total
  elif total > 56:
    take = random.randint(15, 28)
  elif 56 >= total > 29:
    take = total - 29
  else: 
    take = random.randint(1, 28)
  game_candies.take_candies(take)
  if await who_won(message, take,'bot'):
    return
  await message.answer(text.take_bot(take, int(game_candies.get_total())))
  await player_turn(message)

async def who_won(message, take: int, player: str):
  if game_candies.get_total() == 0:
    if player == 'player':
      await message.answer(f'{message.from_user.first_name} {text.win_people}')
    else:
      await message.answer(text.win_bot)
    game_candies.new_game()
    return True
  else:
    return False