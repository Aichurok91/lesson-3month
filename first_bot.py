from aiogram import Bot, Dispatcher, types, executor
from config import token 

bot = Bot(token = '6805857244:AAHpDZuoiG3-CGoNgxcYB923l35notWlX0s')
dp = Dispatcher(bot)

@dp.message_handler(commands = 'start')
async def star(message:types.Message):
    await message.answer("Привет Гикс!!!")

@dp.message_handler(commands='help')
async def help(message:types.Message):
    await message.answer("Чем я могу вам помочь?")

@dp.message_handler(text='Привет')
async def hello(message:types.Message):
    await message.answer("Привет как дела?")

@dp.message_handler(commands='test')
async def test(message:types.Message):
    await message.reply("Тест бота?")
    await message.answer_location(40.51930909205171, 72.80296442030333)
    await message.answer_photo('https://geeks.kg/back_media/main_block/2023/06/22/96425634-e4e2-44ae-8f86-243519f735f3.webp')
    await message.answer_dice()
    await message.answer_sticker('https://geeks.kg/back_media/main_block/2023/06/22/96425634-e4e2-44ae-8f86-243519f735f3.webp')
    await message.answer_contact('+996778493732', 'Aichurok', 'Backend')
    with open('test.jpg', 'rb') as test_jpg:
        await message.answer_photo(test_jpg)

executor.start_polling(dp)