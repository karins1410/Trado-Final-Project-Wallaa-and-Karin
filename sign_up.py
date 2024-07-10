from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def sign_up_valid():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    LOGIN_BUTTON = '//*[@id="root"]/div/div[2]/div/section/nav/div/div[2]/a'
    REG_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/div[1]/span[2]'
    PHONE_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div/input'
    BUS_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[2]/span/input'
    VERIFY_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[3]/span/span/span/i'
    ENTER_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[4]/input'
    CODE_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input'

    driver = webdriver.Chrome()
    driver.get('https://qa.trado.ai/')
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=LOGIN_BUTTON).click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=REG_BUTTON).click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=PHONE_BUTTON).click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=PHONE_BUTTON).send_keys('0532731457')
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=BUS_BUTTON).click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=BUS_BUTTON).send_keys('90102')
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=VERIFY_BUTTON).click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=ENTER_BUTTON).click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=CODE_BUTTON).send_keys('12345')
    time.sleep(2)


    success_message = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[3]/span'
    success_message_element = driver.find_element(By.XPATH, success_message)
    if "registration successful" in success_message_element.text.lower():
        print("Registration successful")
    else:
        print("Registration failed")




def sign_up_invalid():
    LOGIN_BUTTON = '//*[@id="root"]/div/div[2]/div/section/nav/div/div[2]/a'
    REG_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/div[1]/span[2]'
    PHONE_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div/input'
    BUS_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[2]/span/input'
    VERIFY_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[3]/span/span/span/i'
    ENTER_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[4]/input'
    ERROR_MSG = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[3]'

    driver = webdriver.Chrome()
    driver.get('https://qa.trado.ai/')
    driver.maximize_window()
    time.sleep(2)

    driver.find_element(By.XPATH, LOGIN_BUTTON).click()
    time.sleep(2)

    driver.find_element(By.XPATH, REG_BUTTON).click()
    time.sleep(2)

    driver.find_element(By.XPATH, PHONE_BUTTON).click()
    driver.find_element(By.XPATH, PHONE_BUTTON).send_keys('525428670')
    time.sleep(2)

    driver.find_element(By.XPATH, BUS_BUTTON).click()
    driver.find_element(By.XPATH, BUS_BUTTON).send_keys('558878')
    time.sleep(2)

    driver.find_element(By.XPATH, VERIFY_BUTTON).click()
    time.sleep(2)

    driver.find_element(By.XPATH, ENTER_BUTTON).click()
    time.sleep(2)

    error_message = driver.find_element(By.XPATH, ERROR_MSG).get_attribute('innerHTML')
    if error_message == '<span> אחד או יותר מהשדות אינם ייחודיים</span>':
        print('Test passed')
    else:
        print('Test failed')

    driver.quit()

sign_up_valid()
sign_up_invalid()








