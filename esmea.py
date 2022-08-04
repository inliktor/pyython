import fake_useragent
from bs4 import BeautifulSoup
import requests

user = fake_useragent.UserAgent().random

url = r"https://www.kinopoisk.ru/lists/movies/top-250-2020/"

request = requests.get(url)
request.text

soup = BeautifulSoup(request.text, "lxml")

soup.find('div', class_='styles_root__ti07r')