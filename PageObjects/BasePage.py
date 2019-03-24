# -*- coding: utf-8 -*-

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver

        # 等待元素可见

    def wait_eleVisisble(self, locator, by=MobileBy.ANDROID_UIAUTOMATOR, wait_time=30):
        WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located((by, locator)))

    # 等待元素存在
    def wait_elePresence(self, locator, by=MobileBy.ANDROID_UIAUTOMATOR, wait_time=15):
        WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located((by, locator)))

    # 查找并返回一个元素
    def get_element(self, locator, by=MobileBy.ANDROID_UIAUTOMATOR, wait_time=15):
        if by not in By.__dict__.values() and by not in MobileBy.__dict__.values():
            print("你要找的元素定位不存在！")
            raise Exception
        self.wait_eleVisisble(locator, by, wait_time)
        ele = self.driver.find_element(by, locator)
        return ele

    # 查找并返回多个元素
    def get_elements(self, locator, by=MobileBy.ANDROID_UIAUTOMATOR, wait_time=15):
        if by not in By.__dict__.values() and by not in By.__dict__.values():
            print("你要找的元素定位不存在！")
            raise Exception
        eles = self.driver.find_elements(by, locator)
        return eles
