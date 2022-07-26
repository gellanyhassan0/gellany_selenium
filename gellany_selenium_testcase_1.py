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


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(chrome_options=options, executable_path="/usr/bin/chromedriver")

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)


    def tearDown(self):
        self.driver.quit()
        os.system("killall chromium")


unittest.main()
