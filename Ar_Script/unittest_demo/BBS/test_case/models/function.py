from selenium import webdriver
import os

def insert_img(driver,file_name):
    base=os.path.dirname(os.getcwd())
    base=base.replace('\\',os.sep)
    #自己忘记了split的存在了，还想着是怎么处理这个多余的文本
    base=str(base.split(os.sep+'test_case')[0])
    file_path=base+os.sep+'report'+os.sep+'image'+os.sep+file_name
    print(file_path)
    driver.get_screenshot_as_file(file_path)



if __name__ == '__main__':
    driver=webdriver.Chrome()
    driver.get('http://www.baidu.com')
    insert_img(driver,'百度.png')
    driver.quit()