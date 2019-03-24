# -*- coding: utf-8 -*-

import pytest
import time
from Common.BaseDriver import BaseDriver


@pytest.fixture()
def common_driver():
    driver = BaseDriver().base_driver()
    yield driver
    driver.close_app()
    driver.quit()
