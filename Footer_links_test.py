from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def q_a_footer_links():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    LOGIN_BUTTON = '//*[@id="root"]/div/div[2]/div/section/nav/div/div[2]/a'
    TEL_NUMBER = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div'
    ENTER_NUMBER = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div/input'
    REMEMBER_ME = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[2]/span/span/span/i'
    ENTER_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[4]/input'
    CODE_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input'
    FREQUENT_Q_A_BUTTON = '//*[@id="root"]/div/div[2]/div[3]/div/div[2]/a[1]'
    FREQUENT_Q_A_LINK = 'https://qa.trado.ai/questions'

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
    driver.find_element(by=By.XPATH, value=FREQUENT_Q_A_BUTTON).click()
    time.sleep(2)

    current_url = driver.current_url
    if current_url == FREQUENT_Q_A_LINK:
        print('Test passed')
    else:
        print('Test failed')


q_a_footer_links()


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def shipment_footer_links():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    LOGIN_BUTTON = '//*[@id="root"]/div/div[2]/div/section/nav/div/div[2]/a'
    TEL_NUMBER = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div'
    ENTER_NUMBER = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div/input'
    REMEMBER_ME = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[2]/span/span/span/i'
    ENTER_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[4]/input'
    CODE_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input'
    SHIPPING_BUTTON = '//*[@id="root"]/div/div[2]/div[3]/div/div[2]/a[2]'
    SHIPPING_LINK = 'https://qa.trado.ai/shipment'

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
    driver.find_element(by=By.XPATH, value=SHIPPING_BUTTON).click()
    time.sleep(2)

    current_url = driver.current_url
    if current_url == SHIPPING_LINK:
        print('Test passed')
    else:
        print('Test failed')


shipment_footer_links()


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def etrado_footer_link():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    LOGIN_BUTTON = '//*[@id="root"]/div/div[2]/div/section/nav/div/div[2]/a'
    TEL_NUMBER = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div'
    ENTER_NUMBER = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div/input'
    REMEMBER_ME = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[2]/span/span/span/i'
    ENTER_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[4]/input'
    CODE_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input'
    ETRADO_BUTTON = '//*[@id="root"]/div/div[2]/div[3]/div/div[1]/a[3]'
    ETRADO_LINK = 'https://qa.trado.ai/etrado'

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
    driver.find_element(by=By.XPATH, value=ETRADO_BUTTON).click()
    time.sleep(2)

    current_url = driver.current_url
    if current_url == ETRADO_LINK:
        print('Test passed')
    else:
        print('Test failed')


etrado_footer_link()


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def contact_us_link():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    LOGIN_BUTTON = '//*[@id="root"]/div/div[2]/div/section/nav/div/div[2]/a'
    TEL_NUMBER = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div'
    ENTER_NUMBER = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div/input'
    REMEMBER_ME = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[2]/span/span/span/i'
    ENTER_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[4]/input'
    CODE_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input'
    CONTACT_US_BUTTON = '//*[@id="root"]/div/div[2]/div[3]/div/div[1]/a[4]'
    CONTACT_US_LINK = 'https://qa.trado.ai/contact'

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
    driver.find_element(by=By.XPATH, value=CONTACT_US_BUTTON).click()
    time.sleep(2)

    current_url = driver.current_url
    if current_url == CONTACT_US_LINK:
        print('Test passed')
    else:
        print('Test failed')


contact_us_link()


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def terms_conditions_link():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    LOGIN_BUTTON = '//*[@id="root"]/div/div[2]/div/section/nav/div/div[2]/a'
    TEL_NUMBER = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div'
    ENTER_NUMBER = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div/input'
    REMEMBER_ME = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[2]/span/span/span/i'
    ENTER_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[4]/input'
    CODE_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input'
    TERMS_CONDS_BUTTON = '//*[@id="root"]/div/div[2]/div[3]/div/div[5]/div/a[1]'
    TERMS_CONDS_LINK = 'https://qa.trado.ai/info/%D7%AA%D7%A7%D7%A0%D7%95%D7%9F'

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
    driver.find_element(by=By.XPATH, value=TERMS_CONDS_BUTTON).click()
    time.sleep(2)

    current_url = driver.current_url
    if current_url == TERMS_CONDS_LINK:
        print('Test passed')
    else:
        print('Test failed')


terms_conditions_link()


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def my_account():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    LOGIN_BUTTON = '//*[@id="root"]/div/div[2]/div/section/nav/div/div[2]/a'
    TEL_NUMBER = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div'
    ENTER_NUMBER = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div/input'
    REMEMBER_ME = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[2]/span/span/span/i'
    ENTER_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[4]/input'
    CODE_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input'
    PER_AREA_BUTTON = '//*[@id="root"]/div/div[2]/div[3]/div/div[1]/a[2]'
    PER_AREA_LINK = 'https://qa.trado.ai/user/personalArea'

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
    driver.find_element(by=By.XPATH, value=PER_AREA_BUTTON).click()
    time.sleep(2)

    current_url = driver.current_url
    if current_url == PER_AREA_LINK:
        print('Test passed')
    else:
        print('Test failed')


my_account()

def privacy_link():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    LOGIN_BUTTON = '//*[@id="root"]/div/div[2]/div/section/nav/div/div[2]/a'
    TEL_NUMBER = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div'
    ENTER_NUMBER = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div/input'
    REMEMBER_ME = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[2]/span/span/span/i'
    ENTER_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[4]/input'
    CODE_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input'
    PRIVACY_PO_BUTTON = '//*[@id="root"]/div/div[2]/div[3]/div/div[5]/div/a[2]'
    PRIVACY_PO_LINK = 'https://qa.trado.ai/info/Privacy%20Policy'

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
    driver.find_element(by=By.XPATH, value=PRIVACY_PO_BUTTON).click()
    time.sleep(2)

    current_url = driver.current_url
    if current_url == PRIVACY_PO_LINK:
        print('Test passed')
    else:
        print('Test failed')

privacy_link()

def max_buss_link():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    LOGIN_BUTTON = '//*[@id="root"]/div/div[2]/div/section/nav/div/div[2]/a'
    TEL_NUMBER = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div'
    ENTER_NUMBER = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div/input'
    REMEMBER_ME = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[2]/span/span/span/i'
    ENTER_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[4]/input'
    CODE_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input'
    MAX_BUSI_BUTTON = '//*[@id="root"]/div/div[2]/div[3]/div/div[2]/a[4]'
    MAX_BUSI_LINK = 'https://www.max.co.il/cards/card/8649'

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
    driver.find_element(by=By.XPATH, value=CODE_BUTTON).send_keys('12345')
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=MAX_BUSI_BUTTON).click()
    time.sleep(10)

    current_url = driver.current_url
    if current_url == MAX_BUSI_LINK:
        print('Test passed')
    else:
        print('Test failed')
max_buss_link()


def payments_link():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    LOGIN_BUTTON = '//*[@id="root"]/div/div[2]/div/section/nav/div/div[2]/a'
    TEL_NUMBER = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div'
    ENTER_NUMBER = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div/input'
    REMEMBER_ME = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[2]/span/span/span/i'
    ENTER_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[4]/input'
    CODE_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input'
    PAYMENT_BUTTON = '//*[@id="root"]/div/div[2]/div[3]/div/div[2]/a[3]'
    PAYMENT_LINK = 'https://www.max.co.il/cards/card/8649'

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
    driver.find_element(by=By.XPATH, value=CODE_BUTTON).send_keys('12345')
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=PAYMENT_BUTTON).click()
    time.sleep(10)

    current_url = driver.current_url
    if current_url == PAYMENT_LINK:
        print('Test passed')
    else:
        print('Test failed')

payments_link()


def buss_interface_link():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    LOGIN_BUTTON = '//*[@id="root"]/div/div[2]/div/section/nav/div/div[2]/a'
    TEL_NUMBER = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div'
    ENTER_NUMBER = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div[1]/div/input'
    REMEMBER_ME = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[2]/span/span/span/i'
    ENTER_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[4]/input'
    CODE_BUTTON = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input'
    PAYMENT_BUTTON = '//*[@id="root"]/div/div[2]/div[3]/div/div[2]/a[3]'
    PAYMENT_LINK = 'https://www.max.co.il/cards/card/8649'

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
    driver.find_element(by=By.XPATH, value=PAYMENT_BUTTON).click()
    time.sleep(10)

    current_url = driver.current_url
    if current_url == PAYMENT_LINK:
        print('Test passed')
    else:
        print('Test failed')


buss_interface_link()