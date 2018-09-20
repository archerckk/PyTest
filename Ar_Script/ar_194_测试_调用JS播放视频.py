from selenium import webdriver
from time import sleep
import os

driver=webdriver.Chrome()
driver.implicitly_wait(15)
driver.get('http://videojs.com')
# driver.implicitly_wait(15)
video=driver.find_element_by_id('preview-player_html5_api')

url=driver.execute_script('return arguments[0].currentSrc;',video)
print(url)

'播放视频'
print('start')
driver.execute_script('return arguments[0].play()',video)

sleep(15)

'视频暂停'
print('stop')
driver.execute_script('return arguments[0].pause()',video)

driver.get_screenshot_as_file(os.getcwd()+os.sep+'视频播放截图.png')

sleep(3)

driver.quit()