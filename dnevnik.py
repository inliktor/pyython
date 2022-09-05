import fake_useragent
import requests
from bs4 import BeautifulSoup as Soup
from bs4 import BeautifulSoup
import pandas as pd

url='https://login.dnevnik.ru/login'
user= fake_useragent.UserAgent().random

header={
'user-agent':user
}
data = {
    'login': 'def',
    'password': 'def'

}
login=input('Введите свой логин поязя: ')
passwd= input('Пороль плиз: ')
data['login']= login
data['password']=passwd
session= requests.Session()
Auto=session.post(url,data,header).text
