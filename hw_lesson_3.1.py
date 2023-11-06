# 1) Напишите телеграмм бот который загадывает случайное число с помощью библиотеки random и вы должны угадать его.
# Бот: Я загадал число от 1 до 3 угадайте
# Пользователь: Вводит число 2, если число правильное то выводит “Правильно вы отгадали”
# 2) Если пользователь выиграл отправляете данную фотографию https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg
# 3) Если пользователь проиграл, то отправляете данную фотографию https://media.makeameme.org/created/sorry-you-lose.jpg

from aiogram import Bot, Dispatcher, types, executor
from configs import token 

bot = Bot(token = '6240537582:AAG5YYtba435dpm_d7X3U36OhnZG1Cs5GHw')
dp = Dispatcher(bot)

@dp.message_handler(commands = 'start')
async def star(message:types.Message):
    await message.answer("Я загадал число от 1 до 3 угадайте!!!")

# import random
# def guess(update, context):
#     user_number = int(update.message.text)
#     bot_number = random.randint(1, 3)
    
#     if user_number == bot_number:
#         context.bot.send_message(chat_id=update.effective_chat.id, text='Правильно, вы отгадали!')
#         context.bot.send_photo(chat_id=update.effective_chat.id, photo='https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg')
#     else:
#         context.bot.send_message(chat_id=update.effective_chat.id, text=f'Извините, вы не угадали. Я загадал число {bot_number}')
#         context.bot.send_photo(chat_id=update.effective_chat.id, photo='https://media.makeameme.org/created/sorry-you-lose.jpg')

# # Создание объекта Updater и передача токена бота
# updater = Updater(token='YOUR_BOT_TOKEN', use_context=True)

# # Создание диспетчера и привязка обработчиков команд и сообщений
# dispatcher = updater.dispatcher
# dispatcher.add_handler(CommandHandler('start', start))
# dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, guess))

# # Запуск бота
executor.start_polling(dp)



# # ДОПЗАДАНИЕ:
# # 4) Загрузить файлы в GitHub с .gitignore