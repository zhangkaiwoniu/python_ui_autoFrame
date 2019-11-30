#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import pytest
import allure
from util.common import *
import os

if __name__ == '__main__':
    allure_report = get_allure_dir()
    pytest.main(['-s','-v',"--reruns","1",'testcases','--alluredir',"./report/xml"])
    os.system("allure generate report/xml -o %s"%(allure_report))



