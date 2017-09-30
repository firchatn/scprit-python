from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


browser = webdriver.PhantomJS("/home/firas/git/scripts-python/phantomjs-2.1.1-linux-x86_64/bin/phantomjs",  service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])
browser.set_window_size(1120, 550)
try:
	print(browser.current_url)
	browser.get("https://youtube.com/feed/trending/")
	time.sleep(10)
	browser.maximize_window()
	print(browser.current_url)
	print('ok0')

	top10 = browser.find_elements(By.XPATH, "//a[contains(@class, 'yt-simple-endpoint style-scope ytd-video-renderer')]")
	print(top10)
	print('ok')
	top = browser.find_element_by_id('video-title')
	print('ok2')
	about = top.get_attribute("aria-label")
	print('ok3')
	print(about)
except Exception :
	browser.save_screenshot('screenshot.png')

