import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, CommandStart
from dotenv import load_dotenv
from os import getenv
import logging
from random import choice

load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()
users_uniq = []

@dp.message(CommandStart())
async def message(message: types.Message):
    await message.reply(f'Hi! {message.from_user.first_name}, is that you?!')
    user_id = message.from_user.id
    if user_id not in users_uniq:
        users_uniq.append(user_id)
    await message.answer(f"Наш бот обслуживает {len(users_uniq)}-кол пользователей!")

@dp.message(Command('pic'))
async def send_pic(message: types.Message):
    tett = '/Users/arsenij/PycharmProjects/PROBNIK/image'
    tett_list = os.listdir(tett)
    tett_path = os.path.join(tett, choice(tett_list))
    file = types.FSInputFile(tett_path)
    await message.answer_photo(photo=file)

@dp.message(Command('myinfo'))
async def myinfo(message: types.Message):
    tett = '/Users/arsenij/PycharmProjects/PROBNIK/image'
    tett_list = os.listdir(tett)
    tett_path = os.path.join(tett, choice(tett_list))
    file = types.FSInputFile(tett_path)
    await message.answer_photo(photo=file, caption=f"I found you )"
                                                   f" You're {message.from_user.first_name}"
                                                   f"\n@{message.from_user.username}"
                                                   f"\nid : {message.from_user.id}")


@dp.message(Command('help'))
async def help(message: types.Message):
    await message.reply('/myinfo - will introduce you.'
                        '\n/pic - to see nice image.')

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

