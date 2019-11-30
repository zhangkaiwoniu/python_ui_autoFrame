#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec
from util.common import  *
from util.logger import Logger
import os


class BasePage:

    """
    page基类，编写常用action，
    """
    logger = Logger()

    def __init__(self,driver):
        self.driver = driver

    def find_element_and_wait(self,locator):
        """
        :param locator: 元组形式(By.ID,"id")
        :return: 返回element
        """
        element = None
        try:
            # element = WebDriverWait(self.driver,30).until(ec.presence_of_element_located(*locator))
            element = WebDriverWait(self.driver,30).until(lambda driver:self.driver.find_element(*locator))
        except TimeoutException as e:
            #后期改为logger
            self.logger.erro(f"寻找{locator}元素时间超时")
            self.get_screenShot()
            # print("寻找元素时间超时")
        return element

    def find_elements_and_wait(self,locator):
        """
        :param locator: 元组形式(By.ID,"id")
        :return: 返回element
        """
        elements = None
        try:
            # element = WebDriverWait(self.driver,30).until(ec.presence_of_element_located(*locator))
            elements = WebDriverWait(self.driver,30).until(lambda driver:self.driver.find_elements(*locator))
        except TimeoutException as e:
            #后期改为logger
            self.logger.erro(f"寻找{locator}元素时间超时")
            self.get_screenShot()
            # print("寻找元素时间超时")
        return elements

    def open_home(self,url):
        self.logger.info(f"打开{url}")
        self.driver.get(url)

    def click_element(self,locator):
        self.logger.info(f"点击{locator}元素")
        self.find_element_and_wait(locator).click()

    def send_text(self,locator,text):
        self.logger.info(f"在{locator}上输入{text}")
        element = self.find_element_and_wait(locator)
        element.clear()
        element.send_keys(text)

    def execute_js_click(self,locator):
        self.logger.info(f"使用js点击{locator}")
        element = self.find_element_and_wait(locator)
        self.driver.execute_script("arguments[0].click();",element)

    def is_exist(self,locator):
        flag = True
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException as e:
            flag = False
        return flag

    def delete_cookies(self):
        self.logger.info("清除cookies")
        self.driver.delete_all_cookies()

    def get_screenShot(self):
        self.logger.info("截图")
        save_screen_shot(self.driver)

    def switch_frame(self,locator):
        iframe = self.find_element_and_wait(locator)
        self.logger.info(f"进入{locator}iframe")
        self.driver.switch_to.frame(iframe)

    def switch_to_default(self):
        self.logger.info("退出iframe")
        self.driver.switch_to.default_content()

    def quit(self):
        self.logger.info("关闭浏览器")
        self.driver.quit()



