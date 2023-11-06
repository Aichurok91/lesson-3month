# 1) Напишите телеграмм бот который загадывает случайное число с помощью библиотеки random и вы должны угадать его.
# Бот: Я загадал число от 1 до 3 угадайте
# Пользователь: Вводит число 2, если число правильное то выводит “Правильно вы отгадали”
# 2) Если пользователь выиграл отправляете данную фотографию https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg
# 3) Если пользователь проиграл, то отправляете данную фотографию https://media.makeameme.org/created/sorry-you-lose.jpg

from aiogram import Bot, Dispatcher, types, executor
import random
from config_random import token 

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands = 'start')
async def star(message:types.Message):
    await message.answer("Я загадал число от 1 до 3 угадайте!!!")

@dp.message_handler(text = ['1', '2', '3'])
async def num(message:types.Message):
    number = random.randint(1,3)
    if int(message.text) == number:

        await message.answer(f"Вы угадали, Бот выбрал: {number}")
        await message.answer_photo("https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg")
    else:
        await message.answer(f"Вы неугадали, Бот выбрал: {number}")
        await message.answer_photo("https://media.makeameme.org/created/sorry-you-lose.jpg")
    
executor.start_polling(dp)



# # ДОПЗАДАНИЕ:
# # 4) Загрузить файлы в GitHub с .gitignore