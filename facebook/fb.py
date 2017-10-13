from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
browser.get('http://facebook.com')
finder_email = browser.find_element_by_name('email')
finder_email.clear()
finder_email.send_keys('firaschaaben00@gmail.com')
finder_pass = browser.find_element_by_name('pass')
finder_pass.clear()
finder_pass.send_keys('nitro2010')
time.sleep(5)
finder_pass.send_keys(Keys.RETURN)
time.sleep(5)

finder_find = browser.find_element_by_name('q')
finder_find.send_keys('otc fss start with python!')
finder_find.send_keys(Keys.RETURN)
time.sleep(10)
finder_find.clear()

