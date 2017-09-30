from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
browser.get('http://youtube.com/feed/trending')

time.sleep(10)
"""
top10 = browser.find_elements(By.XPATH, "//a[contains(@class, 'yt-simple-endpoint style-scope ytd-video-renderer')]")
for top in top10[:10]:

    last_top = top.get_attribute("title")

    list = browser.find_elements(By.XPATH, "//span[contains(@class, 'style-scope ytd-video-meta-block')]")
    last_vue = list[0].text
    last_date_title = list[1].text


    print('title : ',last_top)
    print('nombre vue : ',last_vue)
    print('poster le : ',last_date_title)
"""

top10 = browser.find_elements(By.XPATH, "//a[contains(@class, 'yt-simple-endpoint style-scope ytd-video-renderer')]")
print("\n \n")
i = 1
for top in top10[:10]:
    about = top.get_attribute("aria-label")
    print("top ",i)
    print(about)
    print("\n \n")
    i = i + 1
    
browser.close()
