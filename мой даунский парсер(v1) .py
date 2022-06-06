import requests
from bs4 import BeautifulSoup as soup
import fake_useragent
import random
user = fake_useragent.UserAgent().random
url = r"https://lenta.ru/"
html = requests.get(url,user).text
soup_page = soup(html, 'html.parser')
items = soup_page.find_all('div',class_="topnews")
for item in items:
    title = item.find('a').get_text(strip=True)
print(title)
print(item.find('span', class_='card-mini__title').get_text(strip=True))
print(url + item.find('a').get('href'))
print('-----')




    




