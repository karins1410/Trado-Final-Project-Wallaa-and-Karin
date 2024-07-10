from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def add_to_cart_valid():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    LOGIN_BUTTON = '//*[@id="root"]/div/div[2]/div/section/nav/div/div[2]/a'
    TEL_NUMBER = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div/input'
    REMEMBER_ME = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[2]/span/span/span/i'
    ENTER_BUTTON = 'form_submitBtn'
    CODE_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input'
    ADD_PLUS_BUTTON = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/section/div/div/div[1]/div[1]/div/div[2]/div/div/span[1]/i'
    CART_AREA = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div[3]/div[2]'

    driver = webdriver.Chrome()
    driver.get("https://qa.trado.ai/")
    driver.maximize_window()
    time.sleep(2)

    driver.find_element(By.XPATH, value=LOGIN_BUTTON).click()
    time.sleep(2)

    driver.find_element(By.XPATH, value=TEL_NUMBER).click()
    driver.find_element(By.XPATH, value=TEL_NUMBER).send_keys('0532731452')
    time.sleep(2)

    driver.find_element(By.XPATH, value=REMEMBER_ME).click()
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, value=ENTER_BUTTON).click()
    time.sleep(20)

    driver.find_element(By.XPATH, value=CODE_BUTTON).send_keys('12345')
    time.sleep(2)

    driver.get("https://qa.trado.ai/product/Isra")
    time.sleep(5)

    driver.find_element(By.XPATH, value=ADD_PLUS_BUTTON).click()
    time.sleep(5)

    driver.find_element(By.XPATH, value=CART_AREA).click()
    time.sleep(2)

    cart_items = driver.find_elements(By.XPATH,
                                      value='//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div/div[2]/div')
    if cart_items:
        print("FAILED TO ADD ITEM")
    else:
        print("ITEM ADDED TO CART")

    driver.quit()



def add_tocart_valid():
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
    checkout = driver.find_element(by=By.CLASS_NAME, value='orderTimeline_name').get_attribute('innerHTML')
    if checkout == 'פרטי משלוח':
        print('Test passed')
    else:
        print('Test failed')


add_to_cart_valid()
add_tocart_valid()