from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def checkout_valid():
    LOGIN_BUTTON = '//*[@id="root"]/div/div[2]/div/section/nav/div/div[2]/a'
    TEL_NUMBER = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div'
    ENTER_NUMBER = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div/input'
    REMEMBER_ME = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[2]/span/span/span/i'
    ENTER_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[4]/input'
    CODE_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input'
    PLUS_BUTTON = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/section/div/div/div[1]/div[1]/div/div[2]/div/div/span[1]'
    GO_TO_CART = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div[3]/div[2]'
    BUSI_NAME = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[1]/div[1]/div[1]/input'
    EMAIL = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[1]/div[1]/div[4]/input'
    CITY = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[1]/div[2]/div[1]/input'
    STREET = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[1]/div[2]/div[2]/input'
    HOME_NUMBER = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[1]/div[2]/div[3]/input'
    ENTRANCE = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[1]/div[2]/div[5]/input'
    FLOOR = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[1]/div[2]/div[6]/input'
    ZIP_CODE = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[1]/div[2]/div[7]/input'
    UNIT = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[1]/div[2]/div[8]/input'
    FIRST_NAME = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[2]/div[2]/div[2]/input'
    LAST_NAME = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[2]/div[2]/div[3]/input'
    SOCIAL_ID = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[3]/div/div[1]/input'
    BANK = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[3]/div/div[2]/select'
    BRANCH = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[3]/div/div[3]/input'
    BANK_ACC_NUMBER = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[3]/div/div[4]/input'
    ID_DATE = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[3]/div/div[6]/input'
    BD_DATE = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[3]/div/div[7]/input'
    PAYMENT = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[4]/div[3]/button/input'

    driver = webdriver.Chrome()
    driver.get("https://qa.trado.ai/")
    driver.maximize_window()
    time.sleep(2)

    driver.find_element(by=By.XPATH, value=LOGIN_BUTTON).click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=TEL_NUMBER).click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=ENTER_NUMBER).send_keys('527009095')
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=REMEMBER_ME).click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=ENTER_BUTTON).click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=CODE_BUTTON).send_keys('12345')
    time.sleep(2)

    driver.get('https://qa.trado.ai/product/TT221')
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=PLUS_BUTTON).click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=GO_TO_CART).click()
    time.sleep(2)

    driver.find_element(by=By.XPATH, value=BUSI_NAME).send_keys('אהבה בשחקים')
    driver.find_element(by=By.XPATH, value=EMAIL).send_keys('trado.final@gmail.com')
    driver.find_element(by=By.XPATH, value=CITY).send_keys('תל אביב')
    driver.find_element(by=By.XPATH, value=STREET).send_keys('הרצל')
    driver.find_element(by=By.XPATH, value=HOME_NUMBER).send_keys('35')
    driver.find_element(by=By.XPATH, value=ENTRANCE).send_keys('2')
    driver.find_element(by=By.XPATH, value=FLOOR).send_keys('18')
    driver.find_element(by=By.XPATH, value=ZIP_CODE).send_keys('899745')
    driver.find_element(by=By.XPATH, value=UNIT).send_keys('3')
    driver.find_element(by=By.XPATH, value=FIRST_NAME).send_keys('Final')
    driver.find_element(by=By.XPATH, value=LAST_NAME).send_keys('Trado')
    driver.find_element(by=By.XPATH, value=SOCIAL_ID).send_keys('628411686')
    driver.find_element(by=By.XPATH, value=BANK).send_keys('12')
    driver.find_element(by=By.XPATH, value=BRANCH).send_keys('588')
    driver.find_element(by=By.XPATH, value=BANK_ACC_NUMBER).send_keys('1188888')
    driver.find_element(by=By.XPATH, value=ID_DATE).send_keys('15052020')
    driver.find_element(by=By.XPATH, value=BD_DATE).send_keys('09121997')
    time.sleep(2)

    driver.find_element(by=By.XPATH, value=PAYMENT).click()
    time.sleep(2)

    driver.quit()



def checkout_invalid():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    LOGIN_BUTTON = '//*[@id="root"]/div/div[2]/div/section/nav/div/div[2]/a'
    TEL_NUMBER = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div'
    ENTER_NUMBER = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div/input'
    REMEMBER_ME = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[2]/span/span/span/i'
    ENTER_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[4]/input'
    CODE_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input'
    PLUS_BUTTON = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/section/div/div/div[1]/div[1]/div/div[2]/div/div/span[1]'
    GO_TO_CART = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div[3]/div[2]'
    BUSI_NAME = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[1]/div[1]/div[1]/input'
    EMAIL = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[1]/div[1]/div[4]/input'
    CITY = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[1]/div[2]/div[1]/input'
    STREET = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[1]/div[2]/div[2]/input'
    HOME_NUMBER = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[1]/div[2]/div[3]/input'
    ENTRENCE = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[1]/div[2]/div[5]/input'
    FLOOR = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[1]/div[2]/div[6]/input'
    ZIP_CODE = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[1]/div[2]/div[7]/input'
    UNIT = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[1]/div[2]/div[8]/input'
    FIRST_NAME = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[2]/div[2]/div[2]/input'
    LAST_NAME = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[2]/div[2]/div[3]/input'
    SOCIAL_ID = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[3]/div/div[1]/input'
    BANK = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[3]/div/div[2]/select'
    BRANCH = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[3]/div/div[3]/input'
    BANK_ACC_NUMBER = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[3]/div/div[4]/input'
    ID_DATE = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[3]/div/div[6]/input'
    BD_DATE = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[3]/div/div[7]/input'
    PAYMENT = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[4]/div[3]/button/input'

    driver = webdriver.Chrome()
    driver.get("https://qa.trado.ai/")
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=LOGIN_BUTTON).click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=TEL_NUMBER).click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=ENTER_NUMBER).click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=ENTER_NUMBER).send_keys('0532731452')
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=REMEMBER_ME).click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=ENTER_BUTTON).click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=CODE_BUTTON).send_keys('12345')
    time.sleep(2)
    driver.get('https://qa.trado.ai/product/TT221')
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=PLUS_BUTTON).click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=GO_TO_CART).click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=BUSI_NAME).click()
    driver.find_element(by=By.XPATH, value=BUSI_NAME).send_keys('אהבה בשחקים')
    driver.find_element(by=By.XPATH, value=EMAIL).click()
    driver.find_element(by=By.XPATH, value=EMAIL).send_keys('trado.final@gmail.com')
    driver.find_element(by=By.XPATH, value=CITY).click()
    driver.find_element(by=By.XPATH, value=CITY).send_keys('תל אביב')
    driver.find_element(by=By.XPATH, value=STREET).click()
    driver.find_element(by=By.XPATH, value=STREET).send_keys('הרצל')
    driver.find_element(by=By.XPATH, value=HOME_NUMBER).click()
    driver.find_element(by=By.XPATH, value=HOME_NUMBER).send_keys('35')
    driver.find_element(by=By.XPATH, value=ENTRENCE).click()
    driver.find_element(by=By.XPATH, value=ENTRENCE).send_keys('2')
    driver.find_element(by=By.XPATH, value=FLOOR).click()
    driver.find_element(by=By.XPATH, value=FLOOR).send_keys('18')
    driver.find_element(by=By.XPATH, value=ZIP_CODE).click()
    driver.find_element(by=By.XPATH, value=ZIP_CODE).send_keys('899745')
    driver.find_element(by=By.XPATH, value=UNIT).click()
    driver.find_element(by=By.XPATH, value=UNIT).send_keys('3')
    driver.find_element(by=By.XPATH, value=FIRST_NAME).click()
    driver.find_element(by=By.XPATH, value=FIRST_NAME).send_keys('Final')
    driver.find_element(by=By.XPATH, value=LAST_NAME).click()
    driver.find_element(by=By.XPATH, value=LAST_NAME).send_keys('Trado')
    driver.find_element(by=By.XPATH, value=SOCIAL_ID).click()
    driver.find_element(by=By.XPATH, value=SOCIAL_ID).send_keys('628411686')
    driver.find_element(by=By.XPATH, value=BANK).click()
    driver.find_element(by=By.XPATH, value=BANK).send_keys('12')
    driver.find_element(by=By.XPATH, value=BRANCH).click()
    driver.find_element(by=By.XPATH, value=BRANCH).send_keys('588')
    driver.find_element(by=By.XPATH, value=BANK_ACC_NUMBER).click()
    driver.find_element(by=By.XPATH, value=BANK_ACC_NUMBER).send_keys()
    driver.find_element(by=By.XPATH, value=ID_DATE).click()
    driver.find_element(by=By.XPATH, value=ID_DATE).send_keys('15052020')
    driver.find_element(by=By.XPATH, value=BD_DATE).click()
    driver.find_element(by=By.XPATH, value=BD_DATE).send_keys('09121997')
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=PAYMENT).click()
    time.sleep(2)



    c=driver.find_element(by=By.CLASS_NAME, value='checkout').get_attribute('innerText')
    print(c)

   

  
checkout_valid()
checkout_invalid()
