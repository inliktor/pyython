import fake_useragent
import requests
from bs4 import BeautifulSoup as Soup
from bs4 import BeautifulSoup
import pandas as pd

session = requests.Session()


url='http://stat.prtcom.ru/?mode=auth'
user=fake_useragent.UserAgent().random

header ={
    'user-agent': user
}
data={
    'user': 'CiganokMS',
    'passw': 'On4amKSE'
}

responce = session.post(url, data=data, headers=header).text
soup = BeautifulSoup(responce, 'lxml') 
