#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import unittest,os
from util.common import get_report_path
from util.HTMLTestRunner_cn import HTMLTestRunner

def run():
    test_path = os.path.dirname(__file__) + os.sep + "testcases"
    report_name = get_report_path()
    suite = unittest.defaultTestLoader.discover(test_path,"test_*",top_level_dir=None)
    with open(report_name,"wb") as f:
        runner  =HTMLTestRunner(
            stream= f,
            title= "UI report",
            description= "自动化测试报告",
            retry= 1,
            save_last_try= True
        )
        runner.run(suite)

if __name__ == '__main__':
    run()
