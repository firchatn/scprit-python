from selenium import webdriver
driver = webdriver.PhantomJS("/home/firas/git/scripts-python/phantomjs-2.1.1-linux-x86_64/bin/phantomjs", service_args=['--ssl-protocol=any'])
driver.set_window_size(1120, 550)
driver.get("https://duckduckgo.com/")
driver.find_element_by_id('search_form_input_homepage').send_keys("realpython")
driver.find_element_by_id("search_button_homepage").click()
print(driver.current_url)
driver.quit()

