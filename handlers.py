from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from config import dp
import text
import game_candies
import random


@dp.message_handler(commands=['start'])
async def on_start(message: Message):
    await message.answer(text=f"{message.from_user.first_name}" + f'{text.greeting}')


@dp.message_handler(commands=['set'])
async def set_total(message: Message):
    count = message.text.split()[1]
    if not game_candies.check_game():
        if count.isdigit():
            game_candies.set_total(int(count))
            await message.answer(f'Конфет теперь будет {count}')
        else:
            await message.answer(f'{message.from_user.first_name} напиши цифрами')
    else:
        await message.answer(f'{message.from_user.first_name} не меняй правила во время игры')


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
            take_candies = int(message.text)
            total = game_candies.get_total()
            if (0 < take_candies < 29) and take_candies <= total:
                game_candies.take_candies(take_candies)
                total = game_candies.get_total()
                if await who_won(message, take_candies, 'player'):
                    return
                await message.answer(f'{name} взял {take_candies} {text.take_people} '
                                     f'{total} {text.robot}')
                await bot_turn(message)
            else:
                if total <= 28:
                    await message.answer(text.error_total(total))
                else:
                    await message.answer(text.error)
        else:
            pass


async def bot_turn(message):
    total = game_candies.get_total()
    if 28 >= total:
        take_candies = total
    elif total > 56:
        take_candies = random.randint(15, 28)
    elif 56 >= total > 29:
        take_candies = total - 29
    else:
        take_candies = random.randint(1, 28)
    game_candies.take_candies(take_candies)
    if await who_won(message, take_candies, 'bot'):
        return
    await message.answer(text.take_bot(take_candies, int(game_candies.get_total())))
    await player_turn(message)


async def who_won(message, take_candies: int, player: str):
    if game_candies.get_total() == 0:
        if player == 'player':
            await message.answer(f'{message.from_user.first_name} {text.win_people}')
        else:
            await message.answer(text.win_bot)
        game_candies.new_game()
        return True
    else:
        return False
