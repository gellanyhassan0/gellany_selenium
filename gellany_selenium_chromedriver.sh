#!/bin/bash

apt-get install chromium -y
wget https://chromedriver.storage.googleapis.com/102.0.5005.61/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
cp -r chromedriver /usr/bin/chromedriver

python3 selenium_chromedriver_test.py
