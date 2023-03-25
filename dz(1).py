from time import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
 

option = webdriver.FirefoxOptions()
option.set_preference('dom.webdriver.enabled',False)
option.set_preference('dom.webnotifications.enabled',False)
option.set_preference('media.volune_scale', '0.0')
sel=webdriver.Firefox(options=option)

log=input()
passw=input()
def register(log,passw):
    sel.get('https://login.dnevnik.ru/login')
    xpath='/html/body/div/div/div/div/div/form/div[2]/div[3]/div[1]/div[1]/label/input'
    Login=log
    sel.find_element_by_xpath(xpath).send_keys(Login)
    #Регистрация
    wor_xpath='/html/body/div/div/div/div/div/form/div[2]/div[3]/div[2]/div[1]/label/input'
    Password=passw
    sel.find_element_by_xpath(wor_xpath).send_keys(Password)
    #Нажатие кнопки войти
    But_xpath='/html/body/div/div/div/div/div/form/div[2]/div[3]/div[4]/div[1]/input'
    button = sel.find_element_by_xpath(But_xpath).click()
    return(register)
assa=register
