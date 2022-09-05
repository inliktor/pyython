import time
import fake_useragent
import requests
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

option = webdriver.FirefoxOptions()
option.set_preference('dom.webdriver.enabled',False)
option.set_preference('dom.webnotifications.enabled',False)
option.set_preference('media.volune_scale', '0.0')

sel=webdriver.Firefox(options=option)

links = []
elements = []
sel.get('https://login.dnevnik.ru/login')
xpath='/html/body/div/div/div/div/div/form/div[2]/div[3]/div[1]/div[1]/label/input'
sel.find_element_by_xpath(xpath).send_keys('tsyganokmikhail')

wor_xpath='/html/body/div/div/div/div/div/form/div[2]/div[3]/div[2]/div[1]/label/input'
sel.find_element_by_xpath(wor_xpath).send_keys('0010085070Misha')

But_xpath='/html/body/div/div/div/div/div/form/div[2]/div[3]/div[4]/div[1]/input'
button = sel.find_element_by_xpath(But_xpath).click()