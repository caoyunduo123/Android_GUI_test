# -*- coding: utf-8 -*-

from appium import webdriver


def base_driver():
    # server 启动参数
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = '坚果 R1'
    desired_caps['udid'] = '464f9dde'
    desired_caps['appPackage'] = 'com.cubic.autohome'
    desired_caps['appActivity'] = '.LogoActivity'
    desired_caps['automationName'] = 'UiAutomator2'

    # 声明driver对象
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver
