import requests 
from bs4 import BeautifulSoup


url = 'https://www.nbkr.kg/index.jsp?lang=RUS'
respons = requests.get(url=url)
print(respons.text)
soup = BeautifulSoup(respons.text, 'lxml')
all_currency = soup.find_all('a',class_ = '_blank')
print(all_currency)
n = 0 
for currency in all_currency:
    n += 1
    with open ('currency.txt','a+', encoding='utf-8') as currency_file:
        currency_file.write(f"{n}) {currency.text}\n")
    print(f'{n}.', currency.text)