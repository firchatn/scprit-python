from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#browser = webdriver.Firefox()


browser = webdriver.PhantomJS("/home/firas/git/scripts-python/phantomjs-2.1.1-linux-x86_64/bin/phantomjs",  service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])
browser.set_window_size(1120, 550)


browser.get('http://instagram.com')

time.sleep(10)

browser.find_element_by_xpath("//a[contains(@class, '_b93kq')]").click()


user_name = browser.find_element_by_name('username')
user_name.clear()
user_name.send_keys('alalala')

password_el = browser.find_element_by_name('password')
password_el.clear()
password_el.send_keys('testtttt')

password_el.send_keys(Keys.RETURN)

time.sleep(10)
error = browser.find_element_by_id('slfErrorAlert')
print(error.text)
"""
while True:
    time.sleep(10)
    browser.find_element_by_xpath("//a[contains(@class, '_8scx2 _gvoze coreSpriteDesktopNavExplore')]").click()
    time.sleep(5)
    browser.find_element_by_xpath("//a[contains(@class, '_3f3gc _fkers')]").click()
    time.sleep(10)
    list = browser.find_elements(By.XPATH, "//button[contains(@class, '_qv64e _gexxb _4tgw8 _njrw0')]")
    for i in range(5):
        time.sleep(1)
        if list[i].text == 'Follow':
            list[i].click()
        print(list[i].text)
"""


