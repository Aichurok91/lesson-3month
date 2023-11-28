# tiktok_downloader.py
import requests, os

input_url = input("URL: ")
print(input_url)
#https://www.tiktok.com/@geeks_osh/video/7300822128192916743
#https://www.tiktok.com/@geeks_osh/video/7300822128192916743?is_from_webapp=1&sender_device=pc&web_id=7289042945105217029
id_video = input_url.split("/")[5].split("?")[0]
print(id_video)
video_api = requests.get(f"https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/feed/?aweme_id={id_video}").json()
# print(video_api)
if video_api:
    print("Скачиваем видео...")
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
        except:
            with open(f"video/{id_video}.mp4", 'wb') as video_file:
                video_file.write(requests.get(video_url).content)
        print("Видео успешно скачан")
    except Exception as error:
        print(f"Error: {error}")