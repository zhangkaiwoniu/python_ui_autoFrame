#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import os
from selenium import webdriver
from util.logger import Logger

class DriverFactory:

    """
        # singleton
        单例模式，保证全局只有有一个driver
    """
    _instance = None
    _dirver = None
    Chrome_driver_path = os.path.join(os.path.dirname(__file__),"drivers" + os.sep + "chromedriver.exe")
    logger = Logger()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def get_driver(cls,browers="chrome"):
        if cls._dirver is None:
            cls._dirver = cls.create_driver(browers)
            cls.logger.info("创建" + browers + "浏览器")
        return cls._dirver

    @classmethod
    def create_driver(cls,browers):
        driver = None
        if browers.lower() == "chrome":
            driver = webdriver.Chrome(executable_path=cls.Chrome_driver_path)
        elif browers.lower() == "firfox":
            driver = webdriver.Chrome()
        elif driver.lower() == "ie":
            driver = webdriver.Ie()
        elif driver.lower() == "Safari":
            driver = webdriver.Safari()
        else:
            #后期此处改为logger
            cls.logger.warn("您传入的参数browers异常")
            # print("您传入的参数browers异常")
        return driver

if __name__ == '__main__':
    print(DriverFactory.Chrome_driver_path)
    driver = DriverFactory.get_driver()
    driver.get("http://www.baidu.com")
    from time import sleep
    sleep(2)
    driver.quit()
















