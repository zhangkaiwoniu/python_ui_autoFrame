#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from pages.basepage import BasePage
from locator.login_locator import login_locator


class LoginPage(BasePage):

    def send_uname(self,uname):
        self.send_text(login_locator.get("username"), uname)

    def send_pword(self,pword):
        self.send_text(login_locator.get("password"),pword)

    def click_button(self):
        self.click_element(login_locator.get("login_button"))
