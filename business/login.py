#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from pages.login_page import LoginPage


class Login:

    def __init__(self,driver):
        self.driver = driver
        self.loginpage = LoginPage(self.driver)

    def login(self,uname,pword):
        self.loginpage.send_uname(uname)
        self.loginpage.send_pword(pword)
        self.loginpage.click_button()
