from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random, string

def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


while True:

    email_rand = randomword(10) + '@yandex.com'
    user_rand = randomword(5) + '.' + randomword(5) 

    print(email_rand)
    print(user_rand)

    browser = webdriver.Firefox()
    browser.get('http://instagram.com')

    time.sleep(10)

    phone_email = browser.find_element_by_name('emailOrPhone')
    phone_email.clear()
    phone_email.send_keys(email_rand)

    full_name = browser.find_element_by_name('fullName')
    full_name.clear()
    full_name.send_keys('jake guidci')

    user_name = browser.find_element_by_name('username')
    user_name.clear()
    user_name.send_keys(user_rand)

    password_el = browser.find_element_by_name('password')
    password_el.clear()
    password_el.send_keys('azertycom')

    password_el.send_keys(Keys.RETURN)
    time.sleep(5)
    if browser.current_url == 'https://www.instagram.com/challenge/':
        browser.close()
        continue
    browser.get('http://instagram.com/ala.hmida/')
    time.sleep(5)
    browser.find_element_by_xpath("//button[contains(@class, '_qv64e _gexxb _r9b8f _njrw0')]").click()
    time.sleep(5)
    browser.close()


