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
             source = self.driver.page_source

             if self.search_var in source:
                  Regex = re.compile(r'<img role="presentation".{,1000}aria-label', re.IGNORECASE)
                  final = Regex.findall(source)
                  for x in final:
                             print(x.split(" "), sep = "\n")
                             

             self.tearDown()

        except : 
             self.tearDown()


    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        os.system("killall chromium")



PythonOrgSearch(search_var="redwings").main()
os.system("killall chromium")
