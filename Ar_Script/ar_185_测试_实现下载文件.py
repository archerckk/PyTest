from selenium import webdriver
import os
import time
cp=webdriver.ChromeOptions()

prefs={'profile.default_content_settings.popups':0,'download.default_directory':os.getcwd()}
cp.add_experimental_option('prefs',prefs)

driver=webdriver.Chrome(chrome_options=cp)
driver.implicitly_wait(10)
driver.get('https://pypi.org/project/selenium/#files')


driver.find_element_by_link_text('selenium-3.13.0.tar.gz').click()

