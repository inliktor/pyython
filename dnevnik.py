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
    'login': '',
    'password': ''

}
login="tsyganokmikhail"
passwd="0010085070Misha'"
data['login']= login
data['password']=passwd
session= requests.Session()
shh="https://dnevnik.ru/userfeed"
Auto=session.post(url, data=data, headers=header).text
ahsf=session.get(shh).text
#tsyganokmikhail
#0010085070Misha
