# Создайте телеграмм бот для Визион Групп для получения информации о строительной компании
# Что должны быть в боте: /start приветствует пользователя и выдает 3 кнопки (о нас, объекты, контакты)
# Если пользователь нажимает о нас выходит информация с сайта https://vg-stroy.com/about/
# Если пользователь нажимает объекты, то выходит информация о всех объектах
# Если пользователь нажимает контакты, то выходит информация с сайта https://vg-stroy.com/contacts/

from aiogram import Bot, Dispatcher, types, executor 
from configs import token

bot = Bot(token)
dp=Dispatcher(bot)

from logging import basicConfig, INFO

bot = Bot(token=token)
dp = Dispatcher(bot)
basicConfig(level=INFO)

start_buttons = [
    types.KeyboardButton('О нас'),
    types.KeyboardButton('Объекты'),
    types.KeyboardButton('Контакты'),
    types.KeyboardButton('Адрес'),
  ]
start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f"Здравствуйте {message.from_user.full_name}, добро пожаловать в строительная компания Визион Групп", reply_markup=start_keyboard)
    print(message)

@dp.message_handler(text="О нас")
async def about_us(message:types.Message):
    await message.answer("Строительная компания «ВИЗИОН ГРУПП» работает на территории города Ош и Джалал-Абад, строя современные жилые комплексы в стильном и качественном исполнении. Дома строятся по индивидуальным архитектурным проектам, представлены в разных ценовых категориях и рассчитаны каждый на определенную целевую аудиторию покупателей. Новостройки застройщика «ВИЗИОН ГРУПП» не похожи друг на друга. Каждая из них самобытна и индивидуальна. Объединяет проекты только неизменно высокое качество строительства, современный облик и качественное инженерное оснащение домов. Компания сотрудничает с несколькими банками, которые готовы на льготных условиях предоставлять кредиты покупателям квартир этого застройщика. Также, продажа квартир возможна в рассрочку, условия которой подробно готовы озвучить сотрудники отдела продаж компании")

@dp.message_handler(text="Объекты")
async def object(message:types.Message):
    await message.answer("Если вы хотите получить подробную информацию о наших объектах, обращайтесь по телефонам в Контакте. Они предоставят вам обширную информацию")

@dp.message_handler(text="Контакты")
async def contact(message:types.Message):
    await message.reply("Телефон:\n+996 (312) 97 98 45, Телефон: \n+996 (990) 00 61 22")

@dp.message_handler(text="Адрес")
async def address(message:types.Message):
    await message.reply("Наш адрес: ул. Абдрахманова 191, офис 119")
    await message.answer_location(42.879660, 74.612795)

executor.start_polling(dp)

# ДОПЗАДАНИЕ:
# Загрузить код в GitHub с .gitginore и config.py файлами