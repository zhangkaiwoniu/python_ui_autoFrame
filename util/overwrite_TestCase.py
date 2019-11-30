#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import unittest
from util.logger import Logger
from util.common import *


class NewTestcase(unittest.TestCase):

    logger = Logger()

    def assertEqual_new(self, first, second, msg,driver):
        try:
            self.assertEqual(first,second,msg)
        except Exception as e:
            self.input_log_and_save_screenshot(str(e),driver)
            raise

    def asserIn_new(self, first, second, msg, driver):
        try:
            self.assertIn(first,second,msg)
        except Exception as e:
            self.input_log_and_save_screenshot(str(e), driver)
            raise

    def assertIs_new(self, first, second, msg, driver):
        try:
            self.assertIs(first,second,msg)
        except Exception as e:
            self.input_log_and_save_screenshot(str(e), driver)
            raise

    def assertisNone_new(self,exp,msg,driver):
        try:
            self.assertIsNone(exp,msg)
        except Exception as e:
            self.input_log_and_save_screenshot(str(e), driver)
            raise

    def input_log_and_save_screenshot(self,exc,driver):
        self.logger.erro(f"断言失败" + exc)
        save_screen_shot(driver)






