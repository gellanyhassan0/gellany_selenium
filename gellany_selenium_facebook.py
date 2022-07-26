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


    def __init__(self, driver = webdriver.Chrome(chrome_options=options, executable_path="/usr/bin/chromedriver"), username_var= None, password_var=None):

        self.driver = driver
        self.username_var = username_var
        self.password_var = password_var

    def main(self):
        try :
             
             self.driver.get("http://www.facebook.com")
             username = self.driver.find_element(By.ID, "email")
             password = self.driver.find_element(By.ID, "pass")
             submit   = self.driver.find_element(By.NAME, "login")
             username.send_keys(self.username_var)
             password.send_keys(self.password_var)
             submit.click()
             time.sleep(0.5)
             #confirm = self.driver.find_element(By.XPATH, "//*[@class=\"_42ft _4jy0 _9kpt _4jy5 _4jy1 selected _51sy\"]")
             #confirm.click()
             time.sleep(0.5)
             
             source = self.driver.page_source
             if "Find friends" in source:
                  Regex = re.compile(r'.{10}Find.friends.{10}', re.IGNORECASE)
                  print(Regex.findall(source))
                  #print(source)
             else:
                 print("not found it") 
             print(self.driver.find_element(By.XPATH, "//div[2]").text)
             self.tearDown()

        except : 
             self.tearDown()


    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        os.system("killall chromium")



PythonOrgSearch(username_var="test1234@gmail.com", password_var="123456789").main()
os.system("killall chromium")
