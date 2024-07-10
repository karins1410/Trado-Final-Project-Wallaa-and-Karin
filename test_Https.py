
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)
website = "https://qa.trado.co.il"

def check_site_security():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://qa.trado.co.il')

    time.sleep(5)
    url = 'https://qa.trado.co.il'

    not_secure = 'https://' in url

    if not_secure:
        print("SITE NOT SECURE ")
    else:
        print("THE SITE IS SECURE ")

    driver.quit()

check_site_security()









