from aiogram import Bot, Dispatcher, types, executor
from config import token 
import requests, os, logging

bot = Bot(token=token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands = 'start')
async def start(message:types.Message):
    await message.answer("Привет {message.from_user.full_name}. Я помогу тебе видео из тик тока без водяных знаков")

@dp.message_handler()
async def get_url_video(message:types.Message):
    if 'https://www.tiktok.com/' in message.text:
        await message.answer("Начинаю скачивать видео...")
        id_video = message.text.split("/")[5].split("?")[0]
        print(id_video)
        video_api = requests.get(f"https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/feed/?aweme_id={id_video}").json()
        # print(video_api)
        if video_api:
            await message.answer("Скачиваем видео...")
            desc_video = video_api.get('aweme_list')[0].get('desc')
            print(desc_video)
            try:
                os.mkdir('video')
                print("Папка video создана")
            except:
                print("Папка video есть")
            try:
                video_url = video_api.get('aweme_list')[0].get('video').get('play_addr').get('url_list')[0]
                try:
                    with open(f"video/{desc_video}.mp4", 'wb') as video_file:
                        video_file.write(requests.get(video_url).content)
                    await message.answer("Видео скачалось, отправляю...")
                    with open(f"video/{desc_video}.mp4", 'rb') as read_video:
                        await message.answer_video(read_video)
                except:
                    with open(f"video/{id_video}.mp4", 'wb') as video_file:
                        video_file.write(requests.get(video_url).content)
                    await message.answer("Видео скачалось, отправляю...")
                    with open(f"video/{id_video}.mp4", 'rb') as read_video:
                        await message.answer_video(read_video)
            except Exception as error:
                print(f"Error: {error}")
    else:
        await message.answer("Неверная ссылка на видео, попробуйте еще раз")
executor.start_polling(dp)