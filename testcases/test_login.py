#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from testcases.base_Testcase import BaseTestcase
from business.login import Login
from parameterized import parameterized
import allure
import time

class TestLogin(BaseTestcase):

    def setUp(self) -> None:
        self.basePage.open_home("http://129.211.69.116:4070/login")

    def tearDown(self) -> None:
        self.basePage.delete_cookies()

    @parameterized.expand([
        ("001","admin","admin123")
    ])
    def test_login_correct(self,num,uname,pwrod):
        Login(self.driver).login(uname,pwrod)
        time.sleep(2)
        title = self.driver.title
        self.assertEqual_new(title,"管理系统首页","正常登录异常",self.driver)

    @parameterized.expand([
        ("001", "administrator", "administrator123")
    ])
    def test_login_wrong(self, num, uname, pwrod):
        Login(self.driver).login(uname, pwrod)
        title = self.driver.title
        self.assertEqual_new(title, "管理系统", "错误登录异常", self.driver)

