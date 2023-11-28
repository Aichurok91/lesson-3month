# Описание:
# Сделать ToDo List Bot (Список дел) с использованием библиотек aiogram
# Пользователь:
# Пользователь может добавлять список своих дел (title, datetime) и данные должны
# попасть в базу данных
# И также пользователь может удалять свои дела из нашей базы данных
# ДОП ЗАДАНИЕ:
# Использовать inline кнопки
# Загрузить код в GitHub c .gitignore

import logging 
from aiogram import Bot, Dispatcher, types 
from aiogram.contrib.fsm_storage.memory import MemoryStorage 
from aiogram.dispatcher import FSMContext 
from aiogram.dispatcher.filters import Command, CommandHelp 
from aiogram.dispatcher.filters.state import State, StatesGroup 
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from aiogram.utils import executor 
import sqlite3
logging.basicConfig(level=logging.INFO)
token = "6431883695:AAEQ1mNR_i5XbRZcs6wFx6KwC1UHVbR9efU"
bot = Bot(token=token) 
storage = MemoryStorage() 
dp = Dispatcher(bot, storage=storage)
class TasksState(StatesGroup): 
    add_task = State() 
    delete_task = State()

def create_tasks_table(): 
    conn = sqlite3.connect("tasks.db") 
    cursor = conn.cursor() 
    cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, title TEXT, datetime TEXT) """) 
    conn.commit() 
    conn.close()
def add_task_to_db(user_id, title, datetime): 
    conn = sqlite3.connect("tasks.db") 
    cursor = conn.cursor() 
    cursor.execute("INSERT INTO tasks (user_id, title, datetime) VALUES (?, ?, ?)", (user_id, title, datetime)) 
    conn.commit() 
    conn.close()
def delete_task_from_db(task_id): 
    conn = sqlite3.connect("tasks.db") 
    cursor = conn.cursor() 
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,)) 
    conn.commit() 
    conn.close()
@dp.message_handler(Command("start")) 
async def start(message: types.Message): 
    await message.answer("Привет! Я ToDo List Bot. Чтобы добавить задачу, просто напиши ее в формате:\n" "Заголовок: Дата и время\n" "Например:\n" "Купить продукты: 01.01.2022 18:00\n" "Чтобы посмотреть список задач, введи команду /tasks")

@dp.message_handler(CommandHelp()) 
async def help_command(message: types.Message): 
    await message.answer("Команды:\n" "/start - начать использование бота " "/tasks - посмотреть список задач " "/add_task - добавить задачу " "/delete_task - удалить задачу")

@dp.message_handler(Command("tasks")) 
async def view_tasks(message: types.Message): 
    create_tasks_table() 
    user_id = message.from_user.id 
    conn = sqlite3.connect("tasks.db") 
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM tasks WHERE user_id=?", (user_id,)) 
    tasks = cursor.fetchall() 
    conn.close() 
    if tasks: 
        tasks_str = "Список задач:\n" 
        for task in tasks: 
            tasks_str += f"\nЗадача {task[0]}:\n" 
            tasks_str += f"Заголовок: {task[2]}\n" 
            tasks_str += f"Дата и время: {task[3]}\n" 
            tasks_str += f"/delete_task_{task[0]}\n" 
            await message.answer(tasks_str, parse_mode=types.ParseMode.HTML) 
    else: 
        await message.answer("У вас пока нет задач.")

@dp.message_handler(Command("add_task")) 
async def add_task_start(message: types.Message): 
    await TasksState.add_task.set() 
    await message.answer("Введите задачу в формате:\n" "Заголовок: Дата и время\n" "Например:\n" "Купить продукты: 01.01.2022 18:00")

@dp.message_handler(state=TasksState.add_task)
async def process_add_task(message: types.Message, state: FSMContext): 
    try: 
        title, datetime = message.text.split(":") 
        title = title.strip() 
        datetime = datetime.strip() 
        user_id = message.from_user.id 
        add_task_to_db(user_id, title, datetime) 
        await state.finish() 
        await message.answer("Задача добавлена!") 
    except ValueError: 
        await message.answer("Некорректный формат задачи. Попробуйте снова.")

@dp.message_handler(Command("delete_task")) 
async def delete_task_start(message: types.Message): 
    await TasksState.delete_task.set() 
    create_tasks_table() 
    user_id = message.from_user.id 
    conn = sqlite3.connect("tasks.db") 
    cursor = conn.cursor() 
    cursor.execute("SELECT id, title FROM tasks WHERE user_id=?", (user_id,)) 
    tasks = cursor.fetchall() 
    conn.close() 
    if tasks: 
        keyboard = InlineKeyboardMarkup(row_width=1) 
        for task in tasks: 
            task_id = task[0] 
            task_title = task[1] 
            keyboard.add(InlineKeyboardButton(f"Удалить задачу {task_id}: {task_title}", callback_data=f"delete_task_{task_id}")) 
            await message.answer("Выберите задачу для удаления:", reply_markup=keyboard) 
    else: 
        await message.answer("У вас нет задач для удаления.")

@dp.callback_query_handler(lambda c: c.data.startswith("delete_task_"), state=TasksState.delete_task) 
async def process_delete_task(callback_query: types.CallbackQuery, state: FSMContext): 
    task_id = callback_query.data.split("_")[2] 
    delete_task_from_db(task_id) 
    await state.finish() 
    await callback_query.answer("Задача удалена!")


executor.start_polling(dp)