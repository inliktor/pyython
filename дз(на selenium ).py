#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By
#driver = webdriver.Firefox()
#driver.get("http://www.python.org")
#assert "Python" in driver.title
#elem = driver.find_element(By.NAME, value="q")
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source


#афывафывфыв расфыв




from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sqlite3
import fake_useragent




option = webdriver.FirefoxOptions()
option.set_preference('dom.webdriver.enabled',False)
option.set_preference('dom.webnotifications.enabled',False)
option.set_preference('media.volune_scale', '0.0')


sel=webdriver.Firefox(options=option)
try:
    def getddglinks(qtext):
        links = []
        sel.get('https://duckduckgo.com/?q=' + qtext.replace(' ', '+'))
        elements = sel.find_elements_by_css_selector('.nrn-react-div')   
        xpath = '/html/body/div[2]/div[5]/div[3]/div/div[1]/div[1]/div/div[3]/a'
        button = sel.find_element_by_xpath(xpath).click()
        xpath = '/html/body/div[7]/div[2]/div/div[1]/ol/li[3]/a'
        button = sel.find_element_by_xpath(xpath).click()
        for element in elements:
            links.append(element.get_attribute('href'))
        return links
    links=getddglinks(input("Введите запрос: "))
    for link in links:
        print(link)
except:
    pass



    