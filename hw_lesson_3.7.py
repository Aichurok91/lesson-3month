# Задание:
# Создание автоматизированного планировщика запросов с использованием библиотеки
# schedule и выполнение HTTP-запросов с помощью библиотеки requests.
# Описание:
# В этом домашнем задании вам предстоит разработать автоматизированный
# планировщик задач, который будет выполнять HTTP-запросы с заданной
# периодичностью. Для достижения этой цели, вы будете использовать две популярные
# библиотеки: schedule для планирования задач и requests для выполнения
# HTTP-запросов.
# Задачи:
# Установка библиотек:
# Убедитесь, что у вас установлены библиотеки schedule и requests. Если они не
# установлены, выполните следующие команды:
# pip install schedule
# pip install requests
# Создание скрипта:
# Создайте Python-скрипт с именем http_request_scheduler.py.
# Импорт библиотек:
# В начале скрипта импортируйте необходимые библиотеки:
# Функция выполнения запроса:
# Создайте функцию perform_request(url), которая будет выполнять GET-запрос по
# заданному URL и выводить результат на экран. Обработайте возможные ошибки при
# выполнении запроса:
# Главная функция:
# Создайте главную функцию main(), в которой задайте URL для запросов, начальную
# задержку и интервал между запросами. Используйте библиотеку schedule для
# планирования задач:
# Тестирование:
# Запустите ваш скрипт http_request_scheduler.py и убедитесь, что запросы выполняются
# с заданной периодичностью. Проверьте обработку возможных ошибок, таких как
# недоступный URL.
# Дополнительные задания:
# Вместо вывода результатов на экран, сохраните их в файл с логами.
# Добавьте возможность задавать URL, начальную задержку и интервал через
# аргументы командной строки при запуске скрипта.
# Обработайте ситуацию, когда интернет-соединение пропадает, и скрипт пытается
# переподключиться и продолжить выполнение.
# Срок выполнения: до следующего урока
# Оценка:
# Оценка будет выставляться на основе следующих критериев:
# Корректность и работоспособность скрипта.
# Правильная настройка и использование библиотек schedule и requests.
# Обработка ошибок при выполнении запросов.
# Дополнительные задания (по желанию) могут повлиять на баллы за задание.

import schedule 
import time 
import requests
import argparse
def perform_request(url): 
    try: 
        response = requests.get(url) 
        if response.status_code == 200: 
            print(f"Request to {url} successful") 
        else: 
            print(f"Request to {url} failed with status code {response.status_code}") 
    except requests.exceptions.RequestException as e: 
        print(f"Request to {url} failed: {e}")

def main(url, initial_delay, interval):
    schedule.every(initial_delay).seconds.do(perform_request, url)


    schedule.every(interval).seconds.do(perform_request, url)

    while True: 
        schedule.run_pending() 

time.sleep(1)


parser = argparse.ArgumentParser(description='HTTP Request Scheduler') 
parser.add_argument('url', type=str, help='URL for the HTTP request') 
parser.add_argument('initial_delay', type=int, help='Initial delay in seconds') 
parser.add_argument('interval', type=int, help='Interval between requests in seconds') 
args = parser.parse_args()

main(args.url, args.initial_delay, args.interval)