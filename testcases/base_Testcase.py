#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from util.overwrite_TestCase import NewTestcase
from webDriver.driver_factory import DriverFactory
from util.logger import Logger
from pages.basepage import BasePage

class BaseTestcase(NewTestcase):

    driver = None
    logger = Logger()

    @classmethod
    def setUpClass(cls) -> None:
        cls.logger.info("-----开始执行测试-----")
        cls.driver = DriverFactory.get_driver()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.basePage = BasePage(cls.driver)


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        cls.logger.info("-----测试结束-----")



