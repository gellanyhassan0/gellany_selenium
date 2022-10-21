#https://selenium-python.readthedocs.io/locating-elements.html

import unittest
import os
import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("no-sandbox")
options.add_argument("headless")
options.add_argument("start-maximized")
options.add_argument("window-size=1900,1080"); 


class PythonOrgSearch():


    def __init__(self, driver = webdriver.Chrome(chrome_options=options, executable_path="/usr/bin/chromedriver"), search_var=None):

        self.driver = driver
        self.search_var = search_var

    def main(self):
        try :
             
             url = "https://www.olx.com.eg/ads/q-redwings/"
             self.driver.get(url)
             time.sleep(0.5)
             #search = self.driver.find_element(By.CLASS_NAME, "fc60720d")
             #search.send_keys("redwings")
             #submit   = self.driver.find_element(By.CSS_SELECTOR, ".a3e390b5")
             #submit.click()
             #time.sleep(0.5)
             allAdsFromPage = self.driver.find_elements(By.XPATH, "//div[@class='a3d4c532']")
             for ad in allAdsFromPage:
                 allPTags = ad.find_elements(By.TAG_NAME, "li")
                 for onePTag in allPTags:
                     tagPText = onePTag.text
             #time.sleep(0.5)
             #print(results)
             #source = all_Tags.page_source
                     print(tagPText)
             #if self.search_var in source:
                  #Regex = re.compile(r'noscript.*"Fallback listing photo"', re.IGNORECASE)
                  #print(Regex.findall(source))
                  #print(source)
             #else:
                 #print("not found it") 
             #print(self.driver.find_element(By.XPATH, '//*[@id="ad-placement-top"]').text)
             self.tearDown()

        except : 
             self.tearDown()


    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        os.system("killall chromium")



PythonOrgSearch(search_var="redwings").main()
os.system("killall chromium")
