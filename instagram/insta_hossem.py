from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
browser.get('http://instagram.com')

time.sleep(10)

browser.find_element_by_xpath("//a[contains(@class, '_b93kq')]").click()
compte = ''
password = ''
follow = 'css'

user_name = browser.find_element_by_name('username')
user_name.clear()
user_name.send_keys(compte)

password_el = browser.find_element_by_name('password')
password_el.clear()
password_el.send_keys(password)

password_el.send_keys(Keys.RETURN)


time.sleep(5)
search = browser.find_element_by_xpath("//input[contains(@class, '_avvq0 _o716c')]")
time.sleep(5)
search.send_keys(follow)
time.sleep(5)
browser.find_element_by_xpath("//span[contains(@class, '_sgi9z')]").click()

time.sleep(5)
browser.find_element_by_xpath("//div[contains(@class, '_mck9w _gvoze _f2mse')]").click()
time.sleep(5)
browser.find_element_by_xpath("//a[contains(@class, '_nzn1h _gu6vm')]").click()
time.sleep(3)
print("list now")
list = browser.find_elements(By.XPATH, "//button[contains(@class, '_qv64e _gexxb _4tgw8 _njrw0')]")
time.sleep(3)
for i in range(5):
    if list[i].text == 'Follow':
        list[i].click()
        
 

