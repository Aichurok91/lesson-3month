# from aiogram import Bot, Dispatcher, types, executor
# from config import token 
# from logging import basicConfig, INFO

# bot = Bot(token=token)
# dp = Dispatcher(bot)
# basicConfig(level=INFO)

# start_buttons = [
#     types.KeyboardButton('О нас'),
#     types.KeyboardButton('Курсы'),
#     types.KeyboardButton('Контакты'),
#     types.KeyboardButton('Адрес'),
# ]
# start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

# @dp.message_handler(commands='start')
# async def start(message:types.Message):
#     await message.answer(f"Здравствуйте {message.from_user.full_name}, добро пожаловать в Geeks!", reply_markup=start_keyboard)
#     print(message)

# @dp.message_handler(text="О нас")
# async def about_us(message:types.Message):
#     await message.answer("Geeks Osh - это айти курсы в Оше, которая открылась в 2021 году")

# @dp.message_handler(text="Контакты")
# async def contacts(message:types.Message):
#     await message.answer("Вот наши контакты:\n+996772343206 - Нурболот")

# @dp.message_handler(text="Адрес")
# async def address(message:types.Message):
#     await message.reply("Наш адрес: Мырзалы Аматова 1Б (БЦ Томирис)")
#     await message.answer_location(40.51930909205171, 72.80296442030333)
#     with open('first_bot.py', 'rb') as python_file:
#         await message.answer_document(python_file)

# courses_buttons = [
#     types.KeyboardButton('Backend'),
#     types.KeyboardButton('Frontend'),
#     types.KeyboardButton('Android'),
#     types.KeyboardButton('iOS'),
#     types.KeyboardButton('UX/UI'),
# ]
# courses_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*courses_buttons)

# @dp.message_handler(text="Курсы")
# async def courses(message:types.Message):
#     await message.reply("Вот наши курсы:", reply_markup=courses_keyboard)

# executor.start_polling(dp)