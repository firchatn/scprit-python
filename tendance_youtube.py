from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
browser.get('http://youtube.com/feed/trending')

time.sleep(10)

top = browser.find_element_by_xpath("//a[contains(@class, 'yt-simple-endpoint style-scope ytd-video-renderer')]")
last_top = top.get_attribute("title")

list = browser.find_elements(By.XPATH, "//span[contains(@class, 'style-scope ytd-video-meta-block')]")
last_vue = list[0].text
last_date_title = list[1].text

#vue = browser.find_element_by_xpath("//span[contains(@class, 'style-scope ytd-video-meta-block')]")
#last_vue = vue.text

print('title : ',last_top)
print('nombre vue : ',last_vue)
print('poster le : ',last_date_title)

browser.close()
