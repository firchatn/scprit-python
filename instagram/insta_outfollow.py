from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
browser.get('http://instagram.com')

time.sleep(10)

phone_email = browser.find_element_by_name('emailOrPhone')
phone_email.clear()
phone_email.send_keys('mohsenijkel@gmail.com')

full_name = browser.find_element_by_name('fullName')
full_name.clear()
full_name.send_keys('mohsenrt')

user_name = browser.find_element_by_name('username')
user_name.clear()
user_name.send_keys('mohseniju8547')

password_el = browser.find_element_by_name('password')
password_el.clear()
password_el.send_keys('azertycom')

password_el.send_keys(Keys.RETURN)
time.sleep(10)
browser.find_element_by_xpath("//a[contains(@class, '_8scx2 _gvoze coreSpriteDesktopNavProfile')]").click()
time.sleep(10)
#browser.find_element_by_xpath("//a[contains(@class, '_t98z6')]").click()
following = browser.find_elements(By.XPATH, "//a[contains(@class, '_t98z6')]")
following[1].click()
for j in range(8):
    time.sleep(5)
    list = browser.find_elements(By.XPATH, "//button[contains(@class, '_qv64e _t78yp _4tgw8 _njrw0')]")
    for i in range(5):
        time.sleep(1)
        list[i].click()
        print(list[i].text)

