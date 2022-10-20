#!/bin/bash

RUN apt-get install -y libglib2.0-0 libnss3 libgconf-2-4 libfontconfig1
apt-get install chromium -y
apt-get install chromium-driver -y
cp -r chromedriver /usr/bin/

apt-get install python3 -y
apt-get install python3-pip -y
yes|pip install selenium
#yes | pip install -r requirements.txt

python3 gellany_selenium_chromedriver_test.py
