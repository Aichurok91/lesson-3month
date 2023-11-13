# Напишите телеграмм бот для ojakkebab.
# Цель телеграмм бота выдавать информацию о заведении (меню, о нас, адрес, заказать еду) Сделайте кнопки (меню, о нас, адрес, заказать еду)
# И также сделайте так при нажатии кнопки запустить чтобы данные пользователей сохранились в базу данных (id, username, first_name, last_name, date_joined)
# При нажатии кнопки меню, пусть ему отправляются меню из этого сайта https://nambafood.kg/ojak-kebap (раздел шашлыки)
# При нажатии кнопки о нас, пусть ему отправится информация с сайта https://ocak.uds.app/c/about
# При нажатии кнопки адрес, пусть ему отправится информация об адресе заведения
# И также при нажатии кнопки заказать еду, то вы должны у пользователя запросить данные как имя, номер телефона, адрес доставки и также после получения данных записать в базу данных
# from concurrent.futures import Executor
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from config_ojakkebab import token
from logging import basicConfig, INFO
from datetime import datetime

bot = Bot(token=token)
storoge = MemoryStorage()
dp = Dispatcher(bot, storage=storoge)
basicConfig(level=INFO)

import sqlite3, time
connection = sqlite3.connect('user_ojakkebab.db')
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS user_ojakkebab(
    id INTEGER,
    username VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    date_joined DATETIME
);
""")
connection.commit()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100),
        title TEXT,
        phone_number VARCHAR(100),
        address VARCHAR(100)
    );
''')
connection.commit()

class OrderFoodState(StatesGroup):
    name = State()
    title = State()
    phone_number = State()
    address = State()

start_buttons = [
    types.KeyboardButton('МЕНЮ'),
    types.KeyboardButton('О нас'),
    types.KeyboardButton('Адрес'),
    types.KeyboardButton('Заказать еду'),
]
start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    cursor=connection.cursor()
    cursor.execute(f"SELECT id FROM user_ojakkebab WHERE id = {message.from_user.id};")
    res = cursor.fetchall()
    if not  res:
        cursor.execute(f"""INSERT INTO user_ojakkebab (id, username, first_name, last_name, date_joined) VALUES (
            {message.from_user.id},
            '{message.from_user.first_name}',
            '{message.from_user.last_name}',
            '{message.from_user.username}',
            '{datetime.now()}'
        );
        """)
        cursor.connection.commit()
    await message.answer(f"Здравствуйте {message.from_user.full_name}, добро пожаловать в Ojak Kebab!", reply_markup=start_keyboard)

@dp.message_handler(text="О нас")
async def about_us(message:types.Message):
    await message.answer("Кафе Ожак Кебап на протяжении 18 лет радует своих гостей с изысканными турецкими блюдами в особенности своим кебабом.Наше кафе отличается от многих кафе своими доступными ценами и быстрым сервисом. В 2016 году по голосованию на сайте Horeca были удостоены Лучшее кафе на каждый день и мы стараемся оправдать доверие наших гостей. Мы не добавляем консерванты, усилители вкуса, красители, ароматизаторы, растительные и животные жиры, вредные добавки с маркировкой «Е». У нас строгий контроль качества: наши филиалы придерживаются норм Кырпотребнадзор и санэпидемстанции. Мы используем только сертифицированную мясную и рыбную продукцию от крупных поставщиков.")

@dp.message_handler(text="Адрес")
async def address(message:types.Message):
    await message.reply("Наш адрес: г. Ош, Курманжан датка, 209")
    await message.answer_location(40.52708, 72.79547)
   
@dp.message_handler(text="Контакты")
async def contacts(message:types.Message):
    await message.answer("Вот наши контакты:\n+996 550 799 012 - Администратор")

menu_buttons = [
    types.KeyboardButton('Салаты'),
    types.KeyboardButton('Супы'),
    types.KeyboardButton('Пиде'),
    types.KeyboardButton('Фастфусд'),
    types.KeyboardButton('Пица'),
    types.KeyboardButton('Шашлыки'),
    types.KeyboardButton('Детское меню'),
    types.KeyboardButton('Соусы'),
    types.KeyboardButton('Десерты'),
    types.KeyboardButton('Гарниры'),
    types.KeyboardButton('Напитки'),
]
menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*menu_buttons)

@dp.message_handler(text="МЕНЮ")
async def menu(message:types.Message):
    await message.reply("Вот наши меню:", reply_markup=menu_keyboard)

@dp.message_handler(text="Салаты")
async def salad(message:types.Message):
    await message.reply("Вот наши салаты:")

@dp.message_handler(text="Супы")
async def soup(message:types.Message):
    await message.reply("Вот наши супы:")

@dp.message_handler(text="Пиде")
async def pide(message:types.Message):
    await message.reply("Вот наши пиде: ")

@dp.message_handler(text="Фастфуды")
async def fastfood(message:types.Message):
    await message.reply("Вот наши Фастфуды: ")

@dp.message_handler(text="Пицы")
async def pissa(message:types.Message):
    await message.reply("Вот наши пицы: ")

@dp.message_handler(text="Шашлыки")
async def kebab(message:types.Message):
    await message.reply("Вот наши шашлыки: https://nambafood.kg/dish_image/163138.png")

@dp.message_handler(text="Детские меню")
async def children_dish(message:types.Message):
    await message.reply("Вот наши детские блюды: ")

@dp.message_handler(text="Соусы")
async def sauces(message:types.Message):
    await message.reply("Вот наши соусы: ")

@dp.message_handler(text="Дессерты")
async def dessert(message:types.Message):
    await message.reply("Вот наши дессерты: ")

@dp.message_handler(text="Гарниры")
async def side_dishes(message:types.Message):
    await message.reply("Вот наши гарниры: ")

@dp.message_handler(text="Напитки")
async def drink(message:types.Message):
    await message.reply("Вот наши напитки: ")





@dp.message_handler(text='Заказать еду')
async def menu(message:types.Message):
    await message.answer('Введите ваше имя')
    await OrderFoodState.name.set()


@dp.message_handler(state=OrderFoodState.name)
async def process_food(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await message.answer("Что хотите заказать?")
    await OrderFoodState.next()

@dp.message_handler(state=OrderFoodState.title)
async def process_food1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['title'] = message.text

    await message.answer("Введите свой номер телефона")
    await OrderFoodState.next()


@dp.message_handler(state=OrderFoodState.phone_number)
async def process_food3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.text

    await message.answer("Введите свой адрес")
    await OrderFoodState.next()


@dp.message_handler(state=OrderFoodState.address)
async def process_food4(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['address'] = message.text


    async with state.proxy() as data:
        name = data['name']
        title = data['title']
        phone_number = data['phone_number']
        address = data['address']

    cursor.execute('''
        INSERT INTO orders (name, title, phone_number, address )
        VALUES (?, ?, ?, ?)
    ''', (name, title, phone_number, address))
    connection.commit()

    await message.answer("Ваш заказ принять.\nЖдите он никогда не приедет")
    await state.finish()

executor.start_polling(dp)



# ДОПЗАДАНИЕ:
# Загрузить код в GitHub и не забудьте использовать файл .gitignor