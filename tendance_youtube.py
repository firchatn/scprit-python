from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
browser.get('http://youtube.com/feed/trending')

time.sleep(10)

top = browser.find_element_by_xpath("//a[contains(@class, 'yt-simple-endpoint style-scope ytd-video-renderer')]")
last_top = top	.get_attribute("title")
print(last_top)
browser.close()


