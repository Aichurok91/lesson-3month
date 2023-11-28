from aiogram import Bot, Dispatcher, types, executor
import logging
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv('token')

bot =Bot(token=token)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands =['start'])
async def star(message:types.Message):
    await message.answer("Привет !!!")

executor.start_polling(dp)
