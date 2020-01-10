from appium import webdriver
import json

class AutoClick(object):

    def __init__(self):
        with open('./resources/phone.json')as f:
            desired_caps=json.load(f)

        self.driver=webdriver.Remote()