# -*- coding: utf-8 -*-

import pytest
import allure
from PageObjects.app_recommend_page import AppRecommendPage
from PageObjects.chejiahao_index_page import ChejiahaoIndexPage
from Common.BaseDriver import base_driver


class TestChejiahaoIndex:

    def setup(self):
        self.driver = base_driver()
        self.app_index = AppRecommendPage(self.driver)
        self.chejiahao_index = ChejiahaoIndexPage(self.driver)

    def test_index_open_success(self):
        self.app_index.click_appNav_Chejiahao()
        index_ball_ranklist_content = self.chejiahao_index.get_indexBall_content_ranklist()
        assert index_ball_ranklist_content == "排行榜"

    def teardown(self):
        self.driver.quit()
