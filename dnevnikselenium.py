from time import *
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


sel.get('https://login.dnevnik.ru/login')
xpath='/html/body/div/div/div/div/div/form/div[2]/div[3]/div[1]/div[1]/label/input'
Login=""
sel.find_element_by_xpath(xpath).send_keys(Login)

wor_xpath='/html/body/div/div/div/div/div/form/div[2]/div[3]/div[2]/div[1]/label/input'
Password=""
sel.find_element_by_xpath(wor_xpath).send_keys(Password)

But_xpath='/html/body/div/div/div/div/div/form/div[2]/div[3]/div[4]/div[1]/input'
button = sel.find_element_by_xpath(But_xpath).click()

xpath="/html/body/div[6]/div/div[2]/div[2]/div[2]"
score=sel.find_element_by_xpath(xpath).text
print(score)

day = "/html/body/div[6]/div/div[2]/div[4]/div[3]/div[1]/div[2]"
days=sel.find_element_by_xpath(day) 

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

for p in range(0,1):
    ssxpath="/html/body/div[6]/div/div[2]/div[4]/div[3]/div[1]/div[3]"
    us = sel.find_element_by_xpath(ssxpath).click()

    raspis="._1vjpx"
    raspiss=sel.find_element_by_css_selector(raspis).text
    
    sleep(2)
    print("| | | ",raspiss)
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

for p in range(0,1):
    ssxpath="/html/body/div[6]/div/div[2]/div[4]/div[3]/div[1]/div[3]"
    us = sel.find_element_by_xpath(ssxpath).click()

    raspis="._1vjpx"
    raspiss1=sel.find_element_by_css_selector(raspis).text
    
    sleep(2)
    print("| | | ",raspiss1)
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

for p in range(0,1):
    ssxpath="/html/body/div[6]/div/div[2]/div[4]/div[3]/div[1]/div[3]"
    us = sel.find_element_by_xpath(ssxpath).click()

    raspis="._1vjpx"
    raspiss2=sel.find_element_by_css_selector(raspis).text
    
    sleep(2)
    print("| | | ",raspiss2)

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
for p in range(0,1):
    ssxpath="/html/body/div[6]/div/div[2]/div[4]/div[3]/div[1]/div[3]"
    us = sel.find_element_by_xpath(ssxpath).click()

    raspis="._1vjpx"
    raspiss3=sel.find_element_by_css_selector(raspis).text
    
    sleep(2)
    print("| | | ",raspiss3)

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
for p in range(0,1):
    ssxpath="/html/body/div[6]/div/div[2]/div[4]/div[3]/div[1]/div[3]"
    us = sel.find_element_by_xpath(ssxpath).click()

    raspis="._1vjpx"
    raspiss4=sel.find_element_by_css_selector(raspis).text
    
    sleep(2)
    print("| | | ",raspiss4)

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
for p in range(0,1):
    ssxpath="/html/body/div[6]/div/div[2]/div[4]/div[3]/div[1]/div[3]"
    us = sel.find_element_by_xpath(ssxpath).click()

    raspis="._1vjpx"
    raspiss5=sel.find_element_by_css_selector(raspis).text
    
    sleep(2)
    print("| | | ",raspiss5)
sel.close()
