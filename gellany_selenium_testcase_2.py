import unittest
import os
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


    def __init__(self, driver = webdriver.Chrome(chrome_options=options, executable_path="/usr/bin/chromedriver")):

        self.driver = driver

    def main(self):
       
        self.driver.get("http://www.python.org")
        print(self.driver.title)
        #self.assertIn("Python", driver.title)
        elem = self.driver.find_element(By.NAME, "q")
        print(elem.get_attribute("name"))
        print(elem.tag_name)


        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        print(self.driver.page_source)
        #self.assertNotIn("No results found.", driver.page_source)
        self.tearDown()


    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        os.system("killall chromium")


PythonOrgSearch().main()
