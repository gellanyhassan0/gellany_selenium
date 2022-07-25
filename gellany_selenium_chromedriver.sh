#!/bin/bash

RUN apt-get install -y libglib2.0-0 libnss3 libgconf-2-4 libfontconfig1
apt-get install chromium -y
#wget https://chromedriver.storage.googleapis.com/102.0.5005.61/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
cp -r chromedriver /usr/bin/

#python3 gellany_selenium_chromedriver_test.py
