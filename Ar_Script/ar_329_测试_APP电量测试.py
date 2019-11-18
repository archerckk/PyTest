import time,csv,os,json
from appium import webdriver

class Control(object):

    def __init__(self,count):
        self.count=count
        self.battery=0
        self.current_time=0


    def operate(self):


    def get_time(self):
        self.current_time=time.strftime("%Y-%m-%d %H:%M:%s",time.localtime())
        return self.current_time

    def test_once(self):


    def run(self):

    def save_data(self):


