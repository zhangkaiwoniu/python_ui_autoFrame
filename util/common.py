#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import os
import time
from datetime import date

def get_date_by_type(type):
    return time.strftime(type,time.localtime(time.time()))

def get_time():
    return time.strftime("%y-%m-%d--%H-%M-%S",time.localtime(time.time()))

def get_date():
    return str(date.today())

def save_screen_shot(driver):
    """
    浏览器截图方法
    :return:
    """
    sub_dir_path = create_dir_path("screenShot")
    screnn_name = os.path.join(sub_dir_path, (get_time() + "_screenShot.png"))
    driver.get_screenshot_as_file(screnn_name)

def get_allure_dir():
    dir_report_path = create_dir_path("report")
    allure_dir = os.path.join(dir_report_path,(get_time() + "_allure_report"))
    # create_dir(allure_dir)
    return allure_dir

def get_report_path():
    """
    返回report文件夹
    :return:
    """
    dir_report_path = create_dir_path("report")
    report_name = os.path.join(dir_report_path, (get_time() + "_report.html"))
    return report_name

def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def create_dir_path(dir):
    root_dir_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), dir)
    sub_dir_path = os.path.join(root_dir_path, get_date())
    create_dir(sub_dir_path)
    return sub_dir_path


if __name__ == '__main__':
    # print(os.path.join(os.path.dirname(os.path.dirname(__file__)),"screenShot"))
    # print(get_date(),type(str(get_date())),sep="----")
    print(get_allure_dir())
    print(get_time())





