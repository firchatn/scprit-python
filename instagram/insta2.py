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
user_name.send_keys('compte')

password_el = browser.find_element_by_name('password')
password_el.clear()
password_el.send_keys('pass')

password_el.send_keys(Keys.RETURN)

while True:
    time.sleep(5)
    browser.find_element_by_xpath("//a[contains(@class, '_8scx2 _gvoze coreSpriteDesktopNavExplore')]").click()
    time.sleep(5)
    browser.find_element_by_xpath("//a[contains(@class, '_3f3gc _fkers')]").click()
    time.sleep(5)
    list = browser.find_elements(By.XPATH, "//button[contains(@class, '_qv64e _gexxb _4tgw8 _njrw0')]")
    list_name = browser.find_elements(By.XPATH, "//a[contains(@class, '_2g7d5 notranslate _o5iw8')]")
    for i in range(5):
        time.sleep(1)
        if list[i].text == 'Follow':
            list[i].click()
            print(list[i].text, " ", list_name[i].text)



