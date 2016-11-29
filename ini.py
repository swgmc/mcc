from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import os
from bs4 import BeautifulSoup
import re
import bs4
import time
import MySQLdb as mdb
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
from pyvirtualdisplay import Display
import sys

#drivers = webdriver.Firefox()
#drivers.get("www.danielquinn.org")

def djobs():
    display = Display(visible=0, size=(800, 600))
    display.start()
    #driver = webdriver.Firefox()
    for retry in range(3):
        try:
            driver = webdriver.Firefox()
            break
        except:
            time.sleep(3)
    driver.get("https://id.wikipedia.org/wiki/A_Rugrats_Chanukah")
    html = driver.page_source
    soup = BeautifulSoup(html, 'html5lib')
    #print soup
    listt = soup.find_all(class_="mw-headline")

    for a in listt:
        print (a.text)

    print ("================================================================================================")
    driver.quit()
    display.stop()

djobs()
scheduler = BlockingScheduler()
scheduler.add_job(djobs, 'interval', minutes=1)