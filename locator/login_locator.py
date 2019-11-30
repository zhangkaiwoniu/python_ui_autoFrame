#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from selenium.webdriver.common.by import By


login_locator = {
    "username" : (By.CSS_SELECTOR,'input[name="username"] '),
    "password" : (By.CSS_SELECTOR,'.pword'),
    "login_button" : (By.ID,"btnSubmit")
}


