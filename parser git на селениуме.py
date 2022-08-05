from ast import Global
from codecs import ignore_errors
import sqlite3
from unicodedata import name
#import time
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
try:
    def getddglinks(qtext):
        links = []
        elements = []
        sel.get('https://duckduckgo.com/?q=' + qtext.replace(' ', '+'))
        elements = sel.find_elements_by_css_selector('.dropdown__switch')  
        xpath='/html/body/div[2]/div[5]/div[3]/div/div[1]/div[1]/div/div[1]/div'
        button = sel.find_element_by_xpath(xpath).click()
        elements = sel.find_elements_by_css_selector('#r1-0 > div:nth-child(2)')  
        xpath='/html/body/div[2]/div[5]/div[3]/div/div[1]/div[5]/div[1]/article/div[2]'
        button = sel.find_element_by_xpath(xpath).click()
        elements = sel.find_elements_by_css_selector('div.Box-row:nth-child(2) > div:nth-child(2) > span:nth-child(1) > a:nth-child(1)')
        for element in elements:
            links.append(element.get_attribute('title'))
            links.append(element.get_attribute('href'))
        elements = sel.find_elements_by_css_selector('div.Box-row:nth-child(3) > div:nth-child(2) > span:nth-child(1) > a:nth-child(1)')
        for element in elements:
            links.append(element.get_attribute('title'))
            links.append(element.get_attribute('href'))
        return links 
except:
    pass
links=getddglinks("https://github.com/inliktor/pyython")
for link in links:
    print(link)

sel.close



        
























    
    
    