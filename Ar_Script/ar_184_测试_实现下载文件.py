from selenium import webdriver
import os
import time
cp=webdriver.ChromeOptions()

"""
profile.default_content_settings.popups  0   设置为禁止弹出下载窗口

download.default_directory    设置为文件下载路径
"""

prefs={'profile.default_content_settings.popups':0,'download.default_directory':os.getcwd()}
cp.add_experimental_option('prefs',prefs)

driver=webdriver.Chrome(chrome_options=cp)
driver.implicitly_wait(10)
driver.get('https://pypi.org/project/selenium/#files')


driver.find_element_by_link_text('selenium-3.14.0.tar.gz').click()

