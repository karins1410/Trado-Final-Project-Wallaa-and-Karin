

def while_loop_login_test_valid():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    LOGIN_BUTTON = '//*[@id="root"]/div/div[2]/div/section/nav/div/div[2]/a'
    TEL_NUMBER = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div'
    ENTER_NUMBER = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div/input'
    REMEMBER_ME = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[2]/span/span/span/i'
    ENTER_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[4]/input'
    CODE_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input'

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

    right_code = 12345
    guess = int(input('Enter your code: '))

    while guess != right_code:
        print('The code you entered is not correct.')
        guess = int(input('Try again: '))
        time.sleep(5)
        driver.find_element(by=By.XPATH, value=CODE_BUTTON).send_keys('12345')
        time.sleep(2)

    print('Test passed')

def for_loop_login_test_valid():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    LOGIN_BUTTON = '//*[@id="root"]/div/div[2]/div/section/nav/div/div[2]/a'
    TEL_NUMBER = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div'
    ENTER_NUMBER = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div/input'
    REMEMBER_ME = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[2]/span/span/span/i'
    ENTER_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[4]/input'
    CODE_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input'

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
    driver.find_element(by=By.XPATH, value=ENTER_NUMBER).send_keys('525428670')
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=REMEMBER_ME).click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=ENTER_BUTTON).click()
    time.sleep(2)

    right_code = 12345

    for x in range(2):
        guess = int(input('Enter your code: '))
        if guess == right_code:
            time.sleep(5)
            driver.find_element(by=By.XPATH, value=CODE_BUTTON).send_keys('12345')
            time.sleep(2)
            print('Test passed')
            break
        else:
            print('The code you entered is not correct.')
            guess = int(input('Try again: '))
            print('Test failed')


def login_test_invalid():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    driver = webdriver.Chrome()
    driver.get("https://qa.trado.ai/")
    driver.maximize_window()
    time.sleep(2)

    LOGIN_BUTTON = '//*[@id="root"]/div/div[2]/div/section/nav/div/div[2]/a'
    TEL_NUMBER = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div'
    ENTER_NUMBER = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div/input'
    REMEMBER_ME = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[2]/span/span/span/i'
    ENTER_BUTTON = 'form_submitBtn'
    VERIFY_BUTTON = 'form_submitBtn'

    driver.find_element(By.XPATH, LOGIN_BUTTON).click()
    time.sleep(2)

    driver.find_element(By.XPATH, TEL_NUMBER).click()
    time.sleep(2)

    driver.find_element(By.XPATH, ENTER_NUMBER).send_keys('053273145')
    time.sleep(2)

    driver.find_element(By.XPATH, REMEMBER_ME).click()
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, ENTER_BUTTON).click()
    time.sleep(20)

    driver.find_element(By.CLASS_NAME, VERIFY_BUTTON).click()
    time.sleep(2)

    error_message_elements = driver.find_elements(By.XPATH,
                                                  '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[3]/span')
    error_found = False

    for error_element in error_message_elements:
        if "no such user please register" in error_element.text.lower():
            print("NO SUCH USER")
            error_found = True
            break

    if not error_found:
        print("Login succeeded .")

    driver.quit()

def wrong_code_login_invalid():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    LOGIN_BUTTON = '//*[@id="root"]/div/div[2]/div/section/nav/div/div[2]/a'
    TEL_NUMBER = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div'
    ENTER_NUMBER = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div/input'
    REMEMBER_ME = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[2]/span/span/span/i'
    ENTER_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[4]/input'
    CODE_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input'

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
    driver.find_element(by=By.XPATH, value=CODE_BUTTON).send_keys('1245')
    time.sleep(2)
    wrong_sms = '1245'

    if wrong_sms != '12345':
        print('wrong code, please try again')
    else:
        print('welcome')


while_loop_login_test_valid()
for_loop_login_test_valid()
login_test_invalid()
wrong_code_login_invalid()