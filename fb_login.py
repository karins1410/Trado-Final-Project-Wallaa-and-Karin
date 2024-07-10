def login_through_fb_vaild():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    driver = webdriver.Chrome()
    driver.get("https://qa.trado.co.il")
    driver.maximize_window()
    time.sleep(2)

    ADVANCE = '//*[@id="details-button"]'
    driver.find_element(By.XPATH, ADVANCE).click()
    time.sleep(2)

    PROCEED = '//*[@id="proceed-link"]'
    driver.find_element(By.XPATH, PROCEED).click()
    time.sleep(5)

    REGISTER = '//*[@id="root"]/div/div[2]/div/section/nav/div/div[2]/a'
    driver.find_element(By.XPATH, REGISTER).click()
    time.sleep(2)

    window_before = driver.window_handles[0]
    print(window_before)

    FACEBOOK = '//*[@id="root"]/div/div[4]/div/div/div/div/div[3]/div[1]/span/button/img'
    driver.find_element(By.XPATH, FACEBOOK).click()
    time.sleep(4)

    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    print(window_after)

    FBMAIL = '//*[@id="email"]'
    FBPASSWORD = '//*[@id="pass"]'
    LOGIN_BUTTON = 'loginbutton'
    driver.find_element(By.XPATH, FBMAIL).send_keys('kinder.bueno.w94@hotmail.com')
    time.sleep(1)
    driver.find_element(By.XPATH, FBPASSWORD).click()
    time.sleep(1)
    driver.find_element(By.XPATH, FBPASSWORD).send_keys('summersalmostgone09876')
    time.sleep(1)

    driver.find_element(By.ID, LOGIN_BUTTON).click()
    time.sleep(10)

    if driver.title == "Facebook":
        print("TEST PASSED")
    else:
        print("TEST FAILED")





def login_through_fb_invalid():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    driver = webdriver.Chrome()
    driver.get("https://qa.trado.co.il")
    driver.maximize_window()
    time.sleep(2)

    advance_btn = driver.find_element(By.ID, 'details-button')
    advance_btn.click()
    time.sleep(2)
    proceed_link = driver.find_element(By.ID, 'proceed-link')
    proceed_link.click()
    time.sleep(5)

    register_link = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/section/nav/div/div[2]/a')
    register_link.click()
    time.sleep(2)

    fb_button = driver.find_element(By.XPATH,
                                    '//*[@id="root"]/div/div[4]/div/div/div/div/div[3]/div[1]/span/button/img')
    fb_button.click()
    time.sleep(4)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)

    fb_email = driver.find_element(By.XPATH, '//*[@id="email"]')
    fb_email.send_keys('kinder@hotma.com')
    time.sleep(1)
    fb_password = driver.find_element(By.XPATH, '//*[@id="pass"]')
    fb_password.click()
    time.sleep(1)
    fb_password.send_keys('summersalmostgone09876')
    time.sleep(1)
    login_btn = driver.find_element(By.ID, 'loginbutton')
    login_btn.click()
    time.sleep(10)

    error_message = "כתובת דואר שגויה"
    if error_message != driver.title:
        print(" כתובת דואר שגויה")
    else:
        print("התחברות בוצעה בהצלחה")

    driver.quit()


login_through_fb_vaild()
login_through_fb_invalid()