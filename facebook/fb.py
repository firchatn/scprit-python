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
finder_pass.send_keys(Keys.RETURN)
ch = str(input('search : '))
time.sleep(5)

finder_find = browser.find_element_by_name('q')
#finder_find.send_keys('otc fss start with python!')
finder_find.send_keys(ch)
finder_find.send_keys(Keys.RETURN)
time.sleep(10)
finder_find.clear()
list = browser.find_elements(By.XPATH, "//a[contains(@class, '_1ii5 _2yez')]")
for i in list:
    print(i.text)
name = browser.find_element_by_xpath("//a[contains(@class, '_1ii5 _2yez')]").text
#browser.find_element_by_xpath("//a[contains(@class, '_1ii5 _2yez')]").click()
print(name)
