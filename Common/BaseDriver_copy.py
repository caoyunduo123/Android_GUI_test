# -*- coding: utf-8 -*-

import yaml
from appium import webdriver
import os


class BaseDriver:

    def base_driver(self):
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        fs = open(os.path.join(cur_dir, "Caps.yaml"))
        caps_data = yaml.load(fs)
        # 连接appium server，并告诉其要操作的对象
        server = 'http://{0}:{1}/wd/hub'.format(caps_data[1]["server_ip"], caps_data[1]["server_port"])
        driver = webdriver.Remote(server, caps_data[0])
        return driver
