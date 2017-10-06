from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
browser.get('http://instagram.com')

time.sleep(10)

browser.find_element_by_xpath("//a[contains(@class, '_b93kq')]").click()


user_name = browser.find_element_by_name('username')
user_name.clear()
user_name.send_keys('-----')

password_el = browser.find_element_by_name('password')
password_el.clear()
password_el.send_keys('*******')

password_el.send_keys(Keys.RETURN)
time.sleep(10)
browser.find_element_by_xpath("//a[contains(@class, '_8scx2 _gvoze coreSpriteDesktopNavProfile')]").click()
time.sleep(10)
#browser.find_element_by_xpath("//a[contains(@class, '_t98z6')]").click()
following = browser.find_elements(By.XPATH, "//a[contains(@class, '_t98z6')]")
following[1].click()
while True:
    time.sleep(1)
    list = browser.find_elements(By.XPATH, "//button[contains(@class, '_qv64e _t78yp _4tgw8 _njrw0')]")
    for i in range(5):
        time.sleep(1)
        list[i].click()
        print(list[i].text)

